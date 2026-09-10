"""
Data tier models (Figure 3.1, "SQLite Database").

Stores user accounts, hashed passwords, TOTP secrets, and authentication logs.
Passwords are never stored in plain text; only a salted hash is kept.
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A registered account. Holds the knowledge factor (password hash) and
    the possession factor (TOTP secret) described in Chapter 3."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    # Possession factor: the shared secret used to generate/verify one-time codes.
    totp_secret = db.Column(db.String(64), nullable=False)
    totp_confirmed = db.Column(db.Boolean, default=False)

    # Failed-login handling / rate limiting (Figure 3.2, "Record failed attempt; lock after N tries")
    failed_attempts = db.Column(db.Integer, default=0)
    locked_until = db.Column(db.DateTime, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def is_locked(self) -> bool:
        return bool(self.locked_until and self.locked_until > datetime.utcnow())


class AuthLog(db.Model):
    """Authentication logging (Figure 3.1, "Authentication Logging").

    Every login attempt is recorded here, whether it succeeds or fails, and at
    which stage it failed. This is the data source for the security-testing
    results described in 06_Results_or_Expected_Output/.
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    event = db.Column(db.String(32), nullable=False)
    # event values: "password_success", "password_fail", "totp_success",
    # "totp_fail", "locked_out", "login_granted"
    detail = db.Column(db.String(255), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
