# email_notifier/templates.py

def get_welcome_email(name: str, subject: str = "Welcome!") -> str:
    """Template for welcome emails."""
    return f"""
    <html>
        <body>
            <h2 style="color: #2c3e50;">{subject}</h2>
            <p>Hi <strong>{name}</strong>,</p>
            <p>Thank you for connecting with us. We're excited to have you!</p>
            <br>
            <p>Best regards,<br>
            <em>Your Python Automation Tool</em></p>
        </body>
    </html>
    """

def get_notification_email(title: str, message: str) -> str:
    """Template for generic notifications."""
    return f"""
    <html>
        <body>
            <h3 style="color: #3498db;">{title}</h3>
            <p>{message}</p>
            <hr>
            <small>This is an automated notification from your Python tool.</small>
        </body>
    </html>
    """

def get_default_template(message: str) -> str:
    """Basic fallback template."""
    return f"""
    <html>
        <body>
            <p>{message}</p>
        </body>
    </html>
    """