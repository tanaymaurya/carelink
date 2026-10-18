"""Symptom triage through the approved gateway. A nurse confirms every suggestion."""
from lib.llm_gateway import chat


def build_prompt(patient, symptoms):
    return [
        {"role": "system", "content": "Suggest an urgency level: emergency, urgent, routine."},
        {"role": "user", "content": f"Age band: {patient.age_band}\nSymptoms: {symptoms}"},
    ]


def triage_symptoms(patient, symptoms):
    return chat(model="gpt-4o", messages=build_prompt(patient, symptoms), feature="symptom-triage")
