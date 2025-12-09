# email_notifier/notifier.py

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from .templates import get_default_template

class EmailNotifier:
    def __init__(self, smtp_server: str = "smtp.gmail.com", port: int = 587):
        self.smtp_server = smtp_server
        self.port = port
        self.sender_email = os.getenv("EMAIL_ADDRESS")
        self.sender_password = os.getenv("EMAIL_PASSWORD")
        
        if not self.sender_email or not self.sender_password:
            raise ValueError("Set EMAIL_ADDRESS and EMAIL_PASSWORD in environment variables!")
    
    def send_email(self, recipient: str, subject: str, body: str = None, 
                   html_body: str = None, template_type: str = "default"):
        """
        Send email with optional HTML formatting.
        """
        if not body and not html_body:
            html_body = get_default_template("This is an automated notification.")
        elif not html_body:
            html_body = get_default_template(body)
        
        # Create message
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = self.sender_email
        msg["To"] = recipient
        
        # Attach HTML part
        html_part = MIMEText(html_body, "html")
        msg.attach(html_part)
        
        try:
            # Connect and send
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Enable encryption
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            
            print(f"✅ Email sent successfully to {recipient}")
            return True
            
        except smtplib.SMTPAuthenticationError:
            print("❌ Authentication failed. Check your email/password.")
            return False
        except smtplib.SMTPException as e:
            print(f"❌ SMTP error: {e}")
            return False
        except Exception as e:
            print(f"❌ Failed to send email: {e}")
            return False

def send_notification_email(recipient: str, subject: str, message: str = None):
    """Convenience function for sending notifications."""
    notifier = EmailNotifier()
    return notifier.send_email(
        recipient=recipient,
        subject=subject,
        body=message
    )

if __name__ == "__main__":
    # Example usage (commented out to prevent accidental execution)
    """
    # Set environment variables before running:
    # export EMAIL_ADDRESS="your_email@gmail.com"
    # export EMAIL_PASSWORD="your_app_password"
    
    send_notification_email(
        recipient="test@example.com",
        subject="Test Notification",
        message="This is a test from your Python automation tool!"
    )
    """
    print("Set EMAIL_ADDRESS and EMAIL_PASSWORD environment variables to use this tool.")