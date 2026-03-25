# Contact List API — Automated Test Suite

Automated API test suite for the [Thinking Tester Contact List API](https://thinking-tester-contact-list.herokuapp.com), built as a QA portfolio project.

Covers authentication, full CRUD operations, negative validation, and an end-to-end contact lifecycle flow.

---

## Tech Stack

| Tool          | Purpose                         |
| ------------- | ------------------------------- |
| Python 3      | Language                        |
| Pytest        | Test framework                  |
| Requests      | HTTP client                     |
| JSONSchema    | Response schema validation      |
| pytest-html   | HTML report generation          |
| python-dotenv | Environment variable management |

---

## Project Structure

```
Contacts_list_API/
│
├── api/
│   ├── auth_api.py                           # Login API wrapper
│   └── contacts_api.py                       # CRUD API wrappers
│
├── schemas/
│   └── contact_schema.py                     # JSONSchema for contact response validation
│
├── tests/
│   ├── auth/
│   │   ├── test_login_positive.py            # Valid login
│   │   └── test_login_negative.py            # Invalid credentials
│   │
│   └── contacts/
│       ├── test_contact_crud.py              # Create, Get, Update, Delete
│       ├── test_contact_negative.py          # Invalid inputs, missing token
│       └── test_contact_positive_flow_E2E.py # Full lifecycle with logging
│
├── utils/
│   └── logger.py                             # Shared file logger
│
├── results/
│   ├── reports/                              # Auto-generated HTML reports (git-ignored)
│   └── logs/                                # Auto-generated log files (git-ignored)
│
├── .env                                      # Credentials — not committed
├── config.py                                 # Loads env vars and base URL
├── conftest.py                               # Shared fixtures + session hooks
├── pytest.ini                                # Pytest config
└── requirements.txt
```

---

## Test Coverage

| Area           | Type     | Tests                                       |
| -------------- | -------- | ------------------------------------------- |
| Login          | Positive | Valid credentials → 200                     |
| Login          | Negative | Invalid password → 401                      |
| Contact CRUD   | Positive | Create, Get, Update, Delete                 |
| Contact Create | Negative | Invalid email → 400                         |
| Contact Create | Negative | Missing token → 401                         |
| Contact Create | Negative | Missing firstName → 400                     |
| Full Lifecycle | E2E      | Create → Get → Update → Delete → Verify 404 |

---

## Setup & Run

**1. Clone the repo**

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd Contacts_list_API
```

**2. Create virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Create `.env` file**

```
EMAIL=your_email@example.com
PASSWORD=yourpassword
```

**5. Run all tests**

```bash
pytest -v
```

**6. Run a specific file**

```bash
pytest tests/contacts/test_contact_positive_flow_E2E.py -v
```

After each run:

- HTML report → `results/reports/report.html`
- Log file → `results/logs/test_run.log` (appended per run, separated by session marker)

---

## Author

Built by **Enay Kumar** as part of a QA automation portfolio.
