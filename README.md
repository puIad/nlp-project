# AI CV Analyzer

An AI-powered CV (resume) analysis system built with Python, Flask, and NLP technologies.

## Features

- 📄 **Smart PDF Extraction**: Dual-method extraction with Unicode normalization
- 🧠 **NLP-Based Analysis**: spaCy-powered NER and semantic analysis
- 📊 **Comprehensive Scoring**: 5-category scoring system (0-100)
- 💡 **Actionable Recommendations**: Personalized improvement suggestions
- 🎥 **Learning Resources**: YouTube learning suggestions based on weak areas
- 🔒 **Admin Dashboard**: Full-featured admin panel with CSV export

## Technology Stack

- **Backend**: Python 3.11+, Flask, SQLAlchemy
- **Database**: MySQL
- **NLP**: spaCy, Transformers, Sentence-Transformers
- **PDF Processing**: pdfplumber, PyMuPDF
- **Frontend**: HTML/CSS/JS, Tailwind CSS, PDF.js

## Quick Start

### 1. Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install packages
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm
```

### 2. Setup MySQL Database

Create a database named `cv`:

```sql
CREATE DATABASE cv CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 3. Configure Environment

Copy `.env.example` to `.env` and update the values:

```bash
cp .env.example .env
```

### 4. Run the Application

```bash
python run.py
```

The application will be available at:
- **App**: http://127.0.0.1:5000
- **Admin**: http://127.0.0.1:5000/admin

### Default Admin Credentials
- Username: `admin`
- Password: `admin123`

## Project Structure

```
ai cv/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # Database models
│   ├── routes/
│   │   ├── main.py          # Main routes
│   │   ├── api.py           # API endpoints
│   │   └── admin.py         # Admin routes
│   ├── services/
│   │   ├── pdf_extractor.py # PDF text extraction
│   │   ├── nlp_analyzer.py  # NLP analysis pipeline
│   │   └── cv_analyzer.py   # Analysis orchestrator
│   └── templates/           # HTML templates
├── config.py                # Configuration
├── requirements.txt         # Python dependencies
├── run.py                   # Application entry point
└── README.md
```

## CV Sections Detected

1. Professional Summary / Objective
2. Education
3. Work Experience
4. Internship Experience
5. Skills
6. Projects
7. Certifications
8. Achievements
9. Hobbies / Interests

## Scoring System

| Category | Weight |
|----------|--------|
| Experience Level | 25% |
| Skills Relevance | 25% |
| CV Structure & Completeness | 20% |
| Career Field Alignment | 15% |
| Readability & Clarity | 15% |

## API Endpoints

- `POST /api/submit-user` - Submit user information
- `POST /api/upload-cv` - Upload and analyze CV
- `GET /api/analysis/<id>` - Get analysis results
- `GET /api/stats` - Get overall statistics

## License

This project is for educational purposes (school project).

## Author

AI CV Analyzer Team
