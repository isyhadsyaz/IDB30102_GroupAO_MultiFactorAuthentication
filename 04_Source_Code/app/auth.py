"""
Authentication routes (Figure 3.2, "Authentication Process Flowchart").

Implements the two-stage login: password check, then one-time code check.
A correct password alone never grants access; both stages must pass.
"""
from datetime import datetime, timedelta

from flask import Blueprint, render_template, request, redirect, url_for, session, flash, current_app
from werkzeug.security import generate_password_hash, check_password_hash

from .models import db, User, AuthLog
from . import totp

bp = Blueprint("auth", __name__)


def log(username: str, event: str, detail: str = "") -> None:
    db.session.add(AuthLog(username=username, event=event, detail=detail))
    db.session.commit()


@bp.route("/register", methods=["GET", "POST"])
def register():
    """Registration Module (Figure 3.1)."""
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        if User.query.filter_by(username=username).first():
            flash("That username is already taken.")
            return redirect(url_for("auth.register"))

        secret = totp.generate_secret()
        user = User(
            username=username,
            password_hash=generate_password_hash(password),
            totp_secret=secret,
        )
        db.session.add(user)
        db.session.commit()

        # In the full build this renders a QR code; the prototype shows the
        # provisioning URI directly so it can be tested without a phone.
        uri = totp.provisioning_uri(username, secret)
        return render_template("register.html", uri=uri, secret=secret)

    return render_template("register.html")


@bp.route("/login", methods=["GET", "POST"])
def login():
    """Stage 1: password check (Figure 3.2, "Password valid?")."""
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()

        if user and user.is_locked():
            log(username, "locked_out")
            flash("This account is temporarily locked. Try again later.")
            return redirect(url_for("auth.login"))

        if user and check_password_hash(user.password_hash, password):
            log(username, "password_success")
            user.failed_attempts = 0
            db.session.commit()
            session["pending_user"] = username
            return redirect(url_for("auth.verify_totp"))

        # Failed-login handling and rate limiting
        if user:
            user.failed_attempts += 1
            if user.failed_attempts >= current_app.config["MAX_FAILED_ATTEMPTS"]:
                user.locked_until = datetime.utcnow() + timedelta(
                    minutes=current_app.config["LOCKOUT_MINUTES"]
                )
                log(username, "locked_out", "too many failed attempts")
            db.session.commit()
        log(username, "password_fail")
        flash("Incorrect username or password.")
        return redirect(url_for("auth.login"))

    return render_template("login.html")


@bp.route("/verify", methods=["GET", "POST"])
def verify_totp():
    """Stage 2: one-time code check (Figure 3.2, "Code valid and not expired?")."""
    username = session.get("pending_user")
    if not username:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        code = request.form["code"].strip()
        user = User.query.filter_by(username=username).first()
        window = current_app.config["TOTP_VALID_WINDOW"]

        if user and totp.verify_code(user.totp_secret, code, valid_window=window):
            log(username, "totp_success")
            log(username, "login_granted")
            session.pop("pending_user", None)
            session["user"] = username
            return redirect(url_for("auth.dashboard"))

        log(username, "totp_fail")
        flash("Invalid or expired code.")
        return redirect(url_for("auth.verify_totp"))

    return render_template("verify_totp.html")


@bp.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("auth.login"))
    return render_template("dashboard.html", username=session["user"])


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
