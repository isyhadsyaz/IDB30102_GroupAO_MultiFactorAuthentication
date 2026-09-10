# 02_Literature_Review

## Purpose

This folder holds the synthesis of the papers listed in `01_Research_Papers/`, organised into the four themes used in Chapter 2 of the Research Proposal, together with the research gap that motivates this project.

## Table 2.1: Summary of the Reviewed Authentication Studies

| Author (Year) | Theme | Setting | Method or Factors | Key Finding | Limitation |
|---|---|---|---|---|---|
| Wang & Wang (2023) | Security weaknesses | Mobile schemes | Analysis of security proofs | Formal proofs can fail in practice | Models miss practical attacks |
| Ang et al. (2025) | Security weaknesses | Authentication protocols | Systematic review and security analysis | Hidden vulnerabilities remain in common schemes | Only selected protocols analysed |
| Morais et al. (2023) | Adaptive and risk-based | Web applications | Adaptive authentication using clustering | Precision 0.934 and F-score 0.96 | Weaker on rare browser and network cases |
| Banerjee & Singh (2025) | Adaptive and risk-based | Online banking | Risk scoring with device check | 96% spoofing and 100% phishing detection | Simulated environment only |
| Sharp et al. (2026) | Adaptive and risk-based | General login | Context-aware adaptive model | F1-score 0.985 with better anomaly detection | Still needs real-world testing |
| Arpitha et al. (2024) | Biometric and user-centred | Healthcare devices | Password, smart card and biometric | Mutual authentication, up to 71% lower cost | Tied to one environment |
| Marasco et al. (2022) | Biometric and user-centred | Usability study | Evaluation of the FingerPIN scheme | Security improves but the interface causes friction | Subjective, small sample |
| Vincenzo et al. (2026) | Biometric and user-centred | Web and desktop login | File activity method vs. commercial product | Higher perceived security, similar usability | Slower completion in some cases |
| Le et al. (2025) | Cryptographic and lightweight | Healthcare devices | Enhanced device authentication protocol | 3.14 ms cost between device and cloud | Specific to healthcare |
| Kantipudi et al. (2024) | Cryptographic and lightweight | Web login | Password, social login and one-time code | Cuts unauthorised access, keeps usability | No measured results reported |
| Mishra et al. (2025) | Cryptographic and lightweight | General web and app login | Time-based one-time password | Roughly 99.9% fewer unauthorised logins | No dataset or real-world test |

## Research Gap

Most of the advanced schemes above target specialised environments, such as healthcare devices or vehicular networks, rather than an ordinary web application, and many are judged only through simulation or formal analysis rather than a running system. The stronger designs usually need extra hardware or behavioural data collection, which conflicts with the cost and complexity barriers that limit real-world MFA adoption (Cisco Duo, 2024). Very few studies measure security, speed, and usability together on one working system.

**This project responds to that gap** by building a small web-based MFA prototype using tools that are freely available (Flask, SQLite, a standard TOTP mechanism), and evaluating it on measured security, authentication time, and usability against an explicit password-only baseline. See `03_Architecture_and_Flowchart/` for the resulting design and `06_Results_or_Expected_Output/` for how that evaluation is planned.

## Relationship to Research Objectives

- **RO1** (study the weaknesses of password-based and existing MFA methods) is answered directly by this synthesis.
- **RO2** and **RO3** build on the gap identified here; see the proposal report Chapter 3 for the full methodology.
