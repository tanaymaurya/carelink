"""Patient-facing API."""
import httpx
from fastapi import FastAPI

from services.api import audit
from services.api.records import load_patient, save_note
from services.api.triage import triage_symptoms
from services.billing.charge import charge_visit

app = FastAPI()


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/triage")
def triage(req: dict):
    patient = load_patient(req["patient_id"])
    audit.record_event("triage", req["patient_id"])
    return triage_symptoms(patient, req["symptoms"])


@app.post("/visits/{visit_id}/notes")
def add_note(visit_id: str, req: dict):
    save_note(req["patient_id"], req["body"])
    httpx.post("https://verify.insurer.example/v1/coverage", json={"patient": req["patient_id"]})
    return charge_visit(visit_id, req["amount_cents"])
