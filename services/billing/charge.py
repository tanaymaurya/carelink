"""Visit billing."""
import stripe
from flask import Flask

app = Flask(__name__)


def charge_visit(visit_id, amount_cents):
    return stripe.PaymentIntent.create(amount=amount_cents, currency="eur", metadata={"visit": visit_id})


@app.route("/invoices", methods=["GET"])
def list_invoices():
    return stripe.Invoice.list(limit=20)
