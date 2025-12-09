#!/usr/bin/env python3
# main.py - Unified CLI for all automation tools

import argparse
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent))

def run_file_organizer(args):
    """Run file organizer with specified directory."""
    from file_organizer.organizer import organize_directory
    from file_organizer.config import DEFAULT_SOURCE_DIR
    
    source_dir = Path(args.source_dir) if args.source_dir else DEFAULT_SOURCE_DIR
    print(f"📂 Organizing files in: {source_dir}")
    
    try:
        organize_directory(source_dir)
    except FileNotFoundError:
        print(f"❌ Directory not found: {source_dir}")
        sys.exit(1)

def run_mcq_evaluator(args):
    """Run MCQ evaluator with specified CSV."""
    from mcq_evaluator.evaluator import evaluate_quiz
    
    csv_path = Path(args.csv_file)
    if not csv_path.exists():
        print(f"❌ CSV file not found: {csv_path}")
        sys.exit(1)
    
    print(f"📋 Evaluating quiz: {csv_path.name}")
    evaluate_quiz(csv_path)

def run_email_notifier(args):
    """Run email notifier."""
    from email_notifier.notifier import send_notification_email
    import os
    
    # Validate environment variables
    if not os.getenv("EMAIL_ADDRESS") or not os.getenv("EMAIL_PASSWORD"):
        print("❌ Environment variables EMAIL_ADDRESS and EMAIL_PASSWORD must be set!")
        print("💡 Set them using: export EMAIL_ADDRESS='your@email.com'")
        sys.exit(1)
    
    success = send_notification_email(
        recipient=args.recipient,
        subject=args.subject,
        message=args.message
    )
    
    if not success:
        print("❌ Failed to send email. Check credentials and network.")
        sys.exit(1)

def interactive_menu():
    """Interactive menu for users who don't use CLI arguments."""
    print("\n🤖 Python Automation Tools")
    print("=" * 30)
    print("1. File Organizer")
    print("2. MCQ Evaluator") 
    print("3. Email Notifier")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        source = input("Enter directory to organize (press Enter for Downloads): ").strip()
        args = argparse.Namespace(source_dir=source if source else None)
        run_file_organizer(args)
    elif choice == "2":
        csv_file = input("Enter CSV file path: ").strip()
        args = argparse.Namespace(csv_file=csv_file)
        run_mcq_evaluator(args)
    elif choice == "3":
        recipient = input("Recipient email: ").strip()
        subject = input("Subject: ").strip()
        message = input("Message: ").strip()
        args = argparse.Namespace(
            recipient=recipient, subject=subject, message=message
        )
        run_email_notifier(args)
    elif choice == "4":
        print("👋 Goodbye!")
        sys.exit(0)
    else:
        print("❌ Invalid choice. Try again.")
        interactive_menu()

def main():
    parser = argparse.ArgumentParser(
        description="Python Automation Toolkit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --tool organizer --source-dir ~/Downloads
  %(prog)s --tool mcq --csv-file quiz.csv
  %(prog)s --tool email --recipient user@domain.com --subject "Test" --message "Hello"
        """
    )
    
    parser.add_argument(
        "--tool", "-t",
        choices=["organizer", "mcq", "email"],
        help="Choose which tool to run"
    )
    
    # File Organizer args
    parser.add_argument("--source-dir", help="Directory to organize (default: ~/Downloads)")
    
    # MCQ Evaluator args
    parser.add_argument("--csv-file", help="Quiz CSV file path")
    
    # Email Notifier args
    parser.add_argument("--recipient", help="Recipient email address")
    parser.add_argument("--subject", help="Email subject")
    parser.add_argument("--message", help="Email message body")
    
    # Parse arguments
    args = parser.parse_args()
    
    # If no arguments provided, show interactive menu
    if not any(vars(args).values()):
        interactive_menu()
        return
    
    # Validate required arguments for each tool
    if args.tool == "organizer":
        run_file_organizer(args)
    elif args.tool == "mcq":
        if not args.csv_file:
            print("❌ --csv-file is required for MCQ evaluator")
            sys.exit(1)
        run_mcq_evaluator(args)
    elif args.tool == "email":
        if not all([args.recipient, args.subject, args.message]):
            print("❌ --recipient, --subject, and --message are required for email notifier")
            sys.exit(1)
        run_email_notifier(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()