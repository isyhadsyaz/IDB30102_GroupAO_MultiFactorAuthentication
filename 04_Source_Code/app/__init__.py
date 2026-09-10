"""
Application factory for the MFA prototype.

This is a PRELIMINARY implementation built to accompany the Research Proposal.
It demonstrates the architecture described in Chapter 3 (Figure 3.1) and is not
a finished product. Security-sensitive defaults (e.g. SECRET_KEY) must be
replaced before any real deployment.
"""
from flask import Flask
from .models import db


def create_app(test_config: dict | None = None) -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev-secret-key-change-before-deployment",
        SQLALCHEMY_DATABASE_URI="sqlite:///mfa_prototype.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        # Failed-login handling / rate limiting (Figure 3.1, "Failed-login Handling & Rate Limiting")
        MAX_FAILED_ATTEMPTS=5,
        LOCKOUT_MINUTES=15,
        # One-time code validity window (Figure 3.2, "TOTP valid & not expired?")
        TOTP_VALID_WINDOW=1,
    )
    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    with app.app_context():
        db.create_all()

    return app
