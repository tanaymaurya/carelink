# CareLink (synthetic)

CareLink is a made-up telehealth company. Nothing here runs, and there is no real company, patient or data
behind it. The repository exists to test [ci-curity](https://github.com/tanaymaurya/ci-curity): its scanner
builds a knowledge graph of this code, and its policy verifier turns that graph into review cases.

The code is written so that every kind of node the scanner can produce appears at least once, together with
cases that are easy to get wrong:

- a patient API (FastAPI) with symptom triage that goes through an approved LLM gateway
- visit-note summaries that call a model their feature does not declare
- reminders by SMS, email and Slack, including a Twilio call that looks like an AI call
- billing (Flask, Stripe), a Redis schedule, a Celery worker that exports to S3
- a patient portal (Next.js, Express, NestJS) whose assistant calls models directly
- an undeclared embeddings script and research spikes with Gemini and LangChain
- one call to a function that does not exist

`ai-features.yaml` declares the AI features. `cicurity.yaml` configures the scanner (gateway, offline LLM)
and, under `policy:`, the organisation's approved services and reviewers.

The expected graph and cases (the answer key) live in the ci-curity repository under `eval/`, so this
repository contains only the code under test.

## Layout

```
services/api/        patient API: triage, records, audit
services/notes/      visit-note summaries
services/reminders/  SMS, email, Slack, Redis
services/billing/    Stripe billing
worker/              Celery jobs
lib/                 the approved LLM gateway
scripts/             one-off embeddings backfill (undeclared)
research/            Gemini and LangChain spikes (undeclared)
web/                 patient portal: Next.js, Express, NestJS
```
