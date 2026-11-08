# AGENTS.md

Flask app that analyzes CVs with spaCy and transformers. See `README.md`.

- Python 3.11+. `pip install -r requirements.txt`, copy `.env.example` to `.env`, `python create_db.py`, then `python run.py`.
- Code: `app/routes` (Flask), `app/services` (PDF extraction, NLP, scoring), `app/models.py` (SQLAlchemy, MySQL).
- Never commit `.env` or real resumes.
