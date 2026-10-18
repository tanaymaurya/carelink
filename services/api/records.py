"""Patient records in Postgres."""
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from services.api.models import Patient

engine = create_engine("postgresql://db/carelink")


def load_patient(patient_id):
    with Session(engine) as session:
        return session.query(Patient).filter_by(id=patient_id).first()


def save_note(patient_id, body):
    with engine.begin() as conn:
        conn.execute(text("INSERT INTO visit_notes (patient_id, body) VALUES (:p, :b)"), {"p": patient_id, "b": body})
