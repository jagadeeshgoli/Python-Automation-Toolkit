# tests/test_email_notifier.py

import unittest
from unittest.mock import patch, MagicMock
from email_notifier.notifier import EmailNotifier

class TestEmailNotifier(unittest.TestCase):
    def setUp(self):
        # Mock environment variables
        import os
        os.environ["EMAIL_ADDRESS"] = "test@gmail.com"
        os.environ["EMAIL_PASSWORD"] = "test_password"
    
    @patch('smtplib.SMTP')
    def test_send_email_success(self, mock_smtp):
        """Test successful email sending."""
        mock_server = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server
        
        notifier = EmailNotifier()
        result = notifier.send_email(
            recipient="recipient@example.com",
            subject="Test Subject",
            body="Test Body"
        )
        
        self.assertTrue(result)
        mock_server.login.assert_called_once_with("test@gmail.com", "test_password")
        mock_server.send_message.assert_called_once()
    
    @patch('smtplib.SMTP')
    def test_send_email_failure(self, mock_smtp):
        """Test email sending failure."""
        mock_server = MagicMock()
        mock_server.login.side_effect = Exception("Auth failed")
        mock_smtp.return_value.__enter__.return_value = mock_server
        
        notifier = EmailNotifier()
        result = notifier.send_email(
            recipient="recipient@example.com",
            subject="Test Subject",
            body="Test Body"
        )
        
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()