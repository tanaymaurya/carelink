"""Access log for patient records."""


def log_access(user, patient_id):
    return f"{user} read {patient_id}"
