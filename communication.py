import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client

class CommunicationHandler:
    def __init__(self, email_config=None, twilio_config=None):
        self.email_config = email_config
        self.twilio_config = twilio_config

    def send_email(self, to_address, subject, message):
        """Send an email using SMTP."""
        if not self.email_config:
            print("Email config not provided.")
            return

        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = self.email_config["from_address"]
        msg["To"] = to_address

        with smtplib.SMTP(self.email_config["smtp_server"], self.email_config["smtp_port"]) as server:
            server.starttls()
            server.login(self.email_config["username"], self.email_config["password"])
            server.sendmail(
                self.email_config["from_address"],
                to_address,
                msg.as_string()
            )

    def send_sms(self, to_number, message):
        """Send an SMS using Twilio."""
        if not self.twilio_config:
            print("Twilio config not provided.")
            return

        client = Client(self.twilio_config["account_sid"], self.twilio_config["auth_token"])
        client.messages.create(
            body=message,
            from_=self.twilio_config["from_number"],
            to=to_number
        )
