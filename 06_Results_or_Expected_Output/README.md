# 06_Results_or_Expected_Output

## Purpose

The Research Proposal stage does not require completed results. This folder states what the prototype in `04_Source_Code/` is **expected** to produce once the evaluation in Section 3.8 of the proposal is carried out, using the sample inputs in `05_Data_or_Sample_Input/`. It gives the lecturer a concrete, checkable target rather than an open claim.

## Expected Results by Attack Scenario

Each scenario is run against both a password-only version of the application (the baseline) and the two-factor prototype. The `AuthLog` table in `04_Source_Code/app/models.py` is the data source once these are actually executed.

| No. | Scenario | Expected Result: Baseline (Password Only) | Expected Result: Prototype (MFA) |
|---|---|---|---|
| 1 | Password guessing | Access granted once a password is guessed | Blocked; a valid one-time code is still required |
| 2 | Brute force | Access granted eventually, no limit on tries | Blocked by rate limiting and the lockout rule after 5 failed attempts |
| 3 | Stolen credential reuse | Access granted immediately | Blocked; the attacker does not hold a valid one-time code |
| 4 | Invalid one-time code | Not applicable, no second step exists | Access refused and the attempt is logged |
| 5 | Replay of an expired code | Not applicable, no second step exists | Access refused because the time window has closed |
| 6 | Skipping the second factor | Not applicable, no second step exists | Access refused; the session is only created after both checks pass |

This table matches Appendix B of the Research Proposal report.

## Evaluation Plan (Table 3.1 of the Proposal)

| Metric | What is Measured | Baseline | Success Condition |
|---|---|---|---|
| Security effectiveness | Share of unauthorised login attempts blocked across the six scenarios above | Password-only version of the app | A much higher share is stopped, including every password-only-knowledge case |
| Authentication time | Average time for a legitimate user to complete login | Password-only login time | Stays within a reasonable margin of the baseline |
| Success and failure rate | Legitimate logins completed vs. incorrectly rejected | Password-only success rate | No meaningful rise in wrongful rejection of valid users |
| Usability | Ease of use, convenience, perceived security (rating scale) | User rating of password-only login | Acceptable rating, no major reported friction |

## Status

No experiment has been run yet; this document defines the target, not a finding. Once Phase 4 (Demonstration) and Phase 5 (Evaluation) in Figure 3.3 are carried out, the actual results will replace the "expected" values above.
