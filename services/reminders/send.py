"""Appointment reminders by SMS and email, and an ops alert in Slack."""
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from slack_sdk import WebClient
from twilio.rest import Client

sms = Client("ACxxxx", "token")


def remind_by_sms(phone, when):
    return sms.messages.create(to=phone, from_="+15550100", body=f"Your appointment is at {when}.")


def remind_by_email(email, when):
    SendGridAPIClient("SG.key").send(Mail(from_email="care@carelink.example", to_emails=email, subject="Reminder",
                                          plain_text_content=f"Your appointment is at {when}."))


def alert_ops(message):
    WebClient(token="xoxb").chat_postMessage(channel="#ops", text=message)
