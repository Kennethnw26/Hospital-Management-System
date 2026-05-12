# Hospital Management System

A role-based hospital management application built in Python as a group project. The system covers the full lifecycle of a hospital visit — from patient registration and appointment scheduling to diagnosis, billing, and discharge — through dedicated portals for each staff role.

---

## Features

### Role-Based Access Control
Five distinct user roles, each with a dedicated portal and password-protected login:

| Role | Capabilities |
|------|-------------|
| **Administrator** | Manage staff accounts, hospital resources, operational policies, insurance verification, and view occupancy/utilization reports |
| **Doctor** | View patient list, update diagnoses & prescriptions, schedule follow-up appointments, access medical history, approve discharges |
| **Nurse** | Manage patient vitals, service requests, and nursing configurations |
| **Receptionist** | Handle patient registration, check-in/check-out, and billing |
| **Patient** | Access personal records and agreements |

### Core Modules
- **AdminConfig.py** — Full CRUD operations for user accounts, hospital resources (beds, equipment), and operational policies; generates occupancy and usage reports
- **DoctorMenu.py** — Patient management with appointment scheduling (date/time validation, leap year handling), medical history access, and discharge workflow
- **NurseMenu.py / NurseConfig.py** — Nursing-specific patient care operations
- **Recept.py / ReceptConfig.py** — Receptionist workflows including patient intake and billing
- **patient_dictionary.py / patient_title.py** — Patient data utilities

### Data Management
Persistent file-based storage using `.txt` and `.csv` files:
- Patient records, vitals, and medical history
- Appointment scheduling and billing details
- Staff credentials (Doctors, Nurses, Receptionists)
- Insurance data, hospital resources, and payment history

---

## Tech Stack

- **Language:** Python 3
- **Storage:** CSV and plain-text flat files
- **Architecture:** Modular, role-separated scripts with a central entry point

---

## Getting Started

**Prerequisites:** Python 3.x

```bash
git clone https://github.com/Kennethnw26/Hospital-Management-System.git
cd Hospital-Management-System/AZPYP_Group_File
python "Hospital Management System Final.py"
```

**Demo credentials (for testing):**
- Admin password: `admin12345`
- Doctor password: `doctor12345`

---

## Project Structure

```
AZPYP_Group_File/
├── Hospital Management System Final.py   # Main entry point
├── AdminConfig.py                         # Admin portal & config
├── DoctorMenu.py                          # Doctor portal
├── NurseMenu.py / NurseConfig.py          # Nurse portal
├── Recept.py / ReceptConfig.py            # Receptionist portal
├── patient_dictionary.py                  # Patient data utilities
├── patient_title.py                       # Patient title helpers
├── *.csv                                  # Staff & resource data
└── *.txt                                  # Patient records & logs
```

---

## Contributors

Group project — 5 members (IDs: TP078930, TP079348, TP079385, TP077617, TP080151)
