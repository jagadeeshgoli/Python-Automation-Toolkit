# Python Automation Toolkit

A collection of 3 practical automation tools built by **Goli Jagadeesh** using Python to simplify daily workflows.  
Includes: File Organizer, MCQ Evaluator, and Email Notifier — used to automate routine tasks efficiently.

##  Developer
**Goli Jagadeesh**  
Python & Backend Developer (Fresher)  
 Lam, Guntur, Andhra Pradesh – 522034  
 7671086404  
 jagadeeshgoli22@gmail.com  
 GitHub: https://github.com/jagadeeshgoli  
 LinkedIn: https://linkedin.com/in/jagadeeshgoli  

---

##  Features

- **File Organizer**  
  Automatically sorts files by type (Documents, Images, Audio, Code, Archives…)

- **MCQ Evaluator**  
  Reads quiz CSVs, checks answers, calculates scores & generates reports

- **Email Notifier**  
  Sends automated emails with HTML formatting + secure authentication

- **Unified CLI Interface**  
  Run all tools using simple command-line options

- **Unit Tests**  
  Full test coverage for reliability and validation

---

##  Prerequisites
- Python 3.7+
- Works on Linux, macOS, Windows (tested on Linux)

---

##  Installation

### Clone the Repository
```bash
git clone <your-repo-url>
cd python-automation-toolkit
````

###  Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate      # Windows → venv\Scripts\activate
```

###  Install Dependencies

```bash
pip install -r requirements.txt
```

###  Set Email Credentials (for Email Notifier)

```bash
export EMAIL_ADDRESS="your_email@gmail.com"
export EMAIL_PASSWORD="your_app_specific_password"
```

---

##  Usage

### **Interactive Mode**

```bash
python main.py
```

### **Command Line Mode**

#### **File Organizer**

```bash
python main.py --tool organizer --source-dir ~/Downloads
```

#### **MCQ Evaluator**

```bash
python main.py --tool mcq --csv-file sample_quiz.csv
```

#### **Email Notifier**

```bash
python main.py --tool email \
    --recipient "friend@example.com" \
    --subject "Hello" \
    --message "Greetings from Python Automation Toolkit!"
```

---

##  Project Structure

```
python-automation-toolkit/
├── main.py                 # CLI entry point
├── requirements.txt        # Dependencies
├── README.md               # Documentation
├── file_organizer/         # File sorting module
├── mcq_evaluator/          # Quiz evaluation module
├── email_notifier/         # Email automation module
└── tests/                  # Unit tests
```

---

##  Email Setup (Gmail)

1. Turn ON 2-Factor Authentication
2. Create **App Password**
3. Export as environment variables:

```bash
export EMAIL_ADDRESS="your_email@gmail.com"
export EMAIL_PASSWORD="your_16_digit_app_password"
```

> Avoid storing credentials inside code.

---

##  Running Tests

```bash
python -m pytest tests/ -v
```

---

##  MCQ CSV Format

```csv
question,correct_answer,user_answer
"What is 2+2?",4,4
"Capital of India?","New Delhi","New Delhi"
```

---

##  Security

* No plain-text passwords in code
* Uses environment variables for credentials
* Input validation in all modules
* Error handling for unsafe operations

---

## Contributing

1. Fork the repository
2. Create a new branch
3. Commit improvements
4. Push & open a Pull Request

---

## License

MIT License — Open for public & commercial use.

---

## Interview Highlights

This project demonstrates:

* Python scripting & automation
* CLI development with `argparse`
* File handling & CSV processing
* Email automation with secure practices
* Clean project structure
* Unit testing

---

Made with ❤️ by **Goli Jagadeesh**
🔗 GitHub: [https://github.com/jagadeeshgoli](https://github.com/jagadeeshgoli)
🔗 LinkedIn: [https://linkedin.com/in/jagadeeshgoli](https://linkedin.com/in/jagadeeshgoli)
