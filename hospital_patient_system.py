"""Hospital patient management system with safer operations."""

import hashlib
import secrets
from pathlib import Path

PATIENT_RECORDS = {
    "P101": {
        "name": "John Doe",
        "ward": "ICU",
        "is_admitted": True,
        "bill": 2400.0,
    },
    "P102": {
        "name": "Jane Smith",
        "ward": "General",
        "is_admitted": False,
        "bill": 450.0,
    },
    "P103": {
        "name": "Robert Brown",
        "ward": "Private",
        "is_admitted": True,
        "bill": 1200.0,
    },
}


def admit_patient(p_id, name, ward, intake_log=None):
    """Admit a new patient and optionally record the admission."""
    if p_id in PATIENT_RECORDS:
        return False

    PATIENT_RECORDS[p_id] = {
        "name": name,
        "ward": ward,
        "is_admitted": True,
        "bill": 0.0,
    }

    if intake_log is not None:
        intake_log.append(f"Admitted patient {p_id} into ward {ward}")

    return True


def discharge_patient(p_id):
    """Discharge an existing patient."""
    patient = PATIENT_RECORDS.get(p_id)

    if patient is None:
        return False

    patient["is_admitted"] = False
    return True


def verify_admission_status(p_id):
    """Check whether an existing patient is admitted."""
    patient = PATIENT_RECORDS.get(p_id)
    return patient is not None and patient["is_admitted"]


def calculate_treatment_cost(p_id, multiplier=1.0):
    """Calculate a patient's bill using a numeric multiplier."""
    patient = PATIENT_RECORDS.get(p_id)

    if patient is None:
        raise ValueError(f"Unknown patient ID: {p_id}")

    if isinstance(multiplier, bool) or not isinstance(
        multiplier, (int, float)
    ):
        raise TypeError("Multiplier must be a number.")

    if multiplier < 0:
        raise ValueError("Multiplier must be non-negative.")

    total = patient["bill"] * multiplier
    return round(total, 2)


def generate_patient_hash(p_id):
    """Generate a SHA-256 digest of a patient identifier."""
    return hashlib.sha256(p_id.encode("utf-8")).hexdigest()


def generate_ward_token():
    """Generate a cryptographically secure four-digit token."""
    return secrets.randbelow(9000) + 1000


def export_patient_ledger(filename="patient_records.txt"):
    """Export patient records to a UTF-8 text file."""
    output_path = Path(filename)

    with output_path.open("w", encoding="utf-8") as ledger_file:
        ledger_file.write(str(PATIENT_RECORDS))

    print(f"Patient ledger exported to: {output_path}")


def get_ward_summary(records):
    """Count the currently admitted patients."""
    return sum(
        patient["is_admitted"]
        for patient in records.values()
    )


def main():
    """Demonstrate the hospital patient management functions."""
    admit_patient("P104", "Alice Walker", "General")
    discharge_patient("P101")

    print("Is P103 admitted:", verify_admission_status("P103"))
    print("Cost calculated:", calculate_treatment_cost("P103", 1.12))
    print("Patient Hash:", generate_patient_hash("P103"))
    print("Ward Token:", generate_ward_token())

    export_patient_ledger()
    print("Active admits:", get_ward_summary(PATIENT_RECORDS))


if __name__ == "__main__":
    main()
