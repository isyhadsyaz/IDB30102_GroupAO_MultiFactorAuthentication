# IDB30102_GroupAO_MultiFactorAuthentication

## Research Proposal Overview

**Title:** Design and Evaluation of a Secure Multi-Factor Authentication System for Web Applications

**Course:** IDB30102 Research Methodology (BCSS), Universiti Kuala Lumpur
**Research Area:** Group AO, Identity and Access Management
**Lecturer:** Dr. Delina Beh Mei Yin
**Semester:** July 2026

This repository supports the Research Proposal submitted for Assignment 2, Section A. It provides the research materials, architecture and flowchart files, preliminary source code, sample input, expected output, and reference list that back the proposal report.

## Research Summary

Password-only authentication is still the main login control on most web applications, and stolen credentials are behind a large share of confirmed breaches. This project designs and evaluates a secure Multi-Factor Authentication (MFA) system for web applications, combining a knowledge factor (username and password) with a possession factor (a time-based one-time code). The system is built as a Flask prototype and tested against a fixed set of attack scenarios, measuring security effectiveness, authentication time, and usability against a password-only baseline.

**Research methodology:** Design Science Research (Peffers et al., 2007)
**Development model:** Prototyping

## Group Members

| No. | Name | Student ID | Main Responsibility |
|---|---|---|---|
| 1 | Muhamad Hafizi Bin Urmia | 52215125151 | Chapter 1, README.md |
| 2 | Nur Fathanah Hidayati Binti Rozani | 52215225242 | Chapter 2, `01_Research_Papers/`, `02_Literature_Review/` |
| 3 | Isyhad Syazani Bin Ismail | 52215125615 | Chapter 3 (Part A), `03_Architecture_and_Flowchart/`, `04_Source_Code/` |
| 4 | Zulaila Natasha Binti Zulhelmi | 52215225170 | Chapter 3 (Part B), `05_Data_or_Sample_Input/`, `06_Results_or_Expected_Output/`, `07_References/` |
| 5 | Nabil Haikal Bin Mohd Azlee | 52215225386 | Abstract, consolidated References, formatting |

## Repository Structure

```
IDB30102_GroupAO_MultiFactorAuthentication/
│
├── README.md                            This file
├── 01_Research_Papers/                  Reviewed papers and annotated bibliography
├── 02_Literature_Review/                Literature synthesis, themes, and research gap
├── 03_Architecture_and_Flowchart/       System architecture diagram and process flowchart
├── 04_Source_Code/                      Preliminary Flask prototype (registration, login, TOTP)
├── 05_Data_or_Sample_Input/             Sample accounts and sample login requests
├── 06_Results_or_Expected_Output/       Attack scenarios and expected test outcomes
└── 07_References/                       Consolidated APA reference list
```

## Research Objective to Repository Mapping

| Objective | Addressed In |
|---|---|
| RO1: Study the security weaknesses of password-based and existing MFA methods | `01_Research_Papers/`, `02_Literature_Review/` |
| RO2: Develop a prototype web-based MFA system | `03_Architecture_and_Flowchart/`, `04_Source_Code/` |
| RO3: Test security effectiveness, performance, and usability against password-only authentication | `05_Data_or_Sample_Input/`, `06_Results_or_Expected_Output/` |

## Status

This repository is at the Research Proposal stage. A complete final system is not required at this stage; the materials here demonstrate the technical direction and feasibility of the proposed research, consistent with the assessment brief.

## Related Documents

- Full Research Proposal report (submitted separately in PDF via VLE)
- Section B presentation slides and video (submitted separately via VLE)
