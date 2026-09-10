# 05_Data_or_Sample_Input

## Purpose

Synthetic test data used to exercise the prototype in `04_Source_Code/`. Nothing here is real user data; all values are invented for testing, consistent with the data collection procedures and the ethical considerations described in Chapter 3 of the Research Proposal.

## Contents

- **`sample_users.csv`** — three test accounts (username, plaintext password, TOTP secret) for setting up a local test run of the prototype. The prototype itself only ever stores the hashed password and the TOTP secret; this file exists only so a tester can log in without generating fresh accounts each time.
- **`sample_login_requests.json`** — one request payload for each authentication scenario, including a normal login and every attack scenario listed in `06_Results_or_Expected_Output/`. These map directly to the routes in `04_Source_Code/app/auth.py` (`/login`, `/verify`, `/dashboard`).

## Relationship to the proposal

Section 3.6 (Data Collection Procedures) of the proposal states that testing uses synthetic accounts in a controlled environment, and Appendix B lists the attack scenarios. The files here are the concrete inputs for that plan.
