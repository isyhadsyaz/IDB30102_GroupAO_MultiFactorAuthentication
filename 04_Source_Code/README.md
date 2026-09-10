# 04_Source_Code

## Purpose

This is a **preliminary** implementation of the prototype described in Chapter 3 of the Research Proposal (Figures 3.1 and 3.2). The assessment brief does not require a complete final system at the proposal stage; this code demonstrates that the proposed architecture is feasible to build with the tools named in the proposal (Flask, SQLite, TOTP).

## What is implemented

- User registration with a hashed password (`werkzeug.security`) and a generated TOTP secret (`app/auth.py`, `app/models.py`)
- Stage 1 login: password check against the stored hash
- Failed-login handling: attempts are counted and the account locks for a configurable period after too many failures
- Stage 2 login: one-time code check against the TOTP secret, with a validity window (`app/totp.py`)
- Authentication logging: every attempt (password success/fail, code success/fail, lockout, granted) is written to the `AuthLog` table
- Minimal HTML templates for register, login, code verification, and a post-login page

This directly implements the flow in Figure 3.2: a session is only created after **both** the password and the one-time code are verified.

## What is not implemented yet

These are planned for the next development iteration (Phase 4 onward in Figure 3.3), not for the proposal stage:

- QR code rendering for authenticator app setup (the provisioning URI is currently shown as text)
- HTTPS/TLS configuration (required for any real deployment, not needed for local testing)
- The automated attack-scenario test scripts described in `06_Results_or_Expected_Output/`
- Production-ready configuration (the `SECRET_KEY` in `app/__init__.py` is a placeholder)

## How to run locally

```bash
cd 04_Source_Code
python -m venv venv
source venv/bin/activate        # venv\Scripts\activate on Windows
pip install -r requirements.txt
python run.py
```

Then open `http://127.0.0.1:5000/register` to create a test account. The registration page shows the TOTP secret directly (for testing without a physical phone) as well as the provisioning URI that a real authenticator app would scan.

## Folder structure

```
04_Source_Code/
├── requirements.txt
├── run.py
└── app/
    ├── __init__.py       Flask application factory
    ├── models.py         User and AuthLog database models (SQLite via SQLAlchemy)
    ├── auth.py            Registration and two-stage login routes
    ├── totp.py            One-time code generation and verification
    ├── templates/         Login, registration, code verification, dashboard pages
    └── static/            Stylesheet
```
