# 03_Architecture_and_Flowchart

## Purpose

This folder holds the system design diagrams referenced as Figures 3.1 to 3.4 in Chapter 3 of the Research Proposal. These diagrams are what `04_Source_Code/` implements, at a preliminary level.

## Contents

| File | Corresponds To | Description |
|---|---|---|
| `architecture_diagram.png` | Figure 3.1 | Three-tier system architecture: presentation tier (browser, authenticator app), application tier (Flask server modules), data tier (SQLite database) |
| `authentication_flowchart.png` | Figure 3.2 | Authentication process flow: password check, then one-time code check, with failure paths for each stage |
| `dsr_methodology_phases.png` | Figure 3.3 | The six Design Science Research phases (Peffers et al., 2007) applied to this project, including the feedback loop from evaluation back to design |
| `project_timeline_gantt.png` | Figure 3.4 | Proposed 14-week project timeline, organised by methodology phase rather than report chapter |

## How the architecture maps to the source code

- **Presentation tier** → `04_Source_Code/app/templates/` (login and registration pages)
- **Application tier, password authentication** → `04_Source_Code/app/auth.py`
- **Application tier, one-time code verification** → `04_Source_Code/app/totp.py`
- **Data tier** → `04_Source_Code/app/models.py` (SQLite via SQLAlchemy)

## Notes

These diagrams are also embedded directly in Chapter 3 of the Research Proposal report (PDF). They are duplicated here so the technical design is visible without opening the full report.
