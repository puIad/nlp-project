"""
Configuration settings for AI CV Analyzer
"""
import os
from datetime import timedelta

# Base directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration"""
    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ai-cv-analyzer-secret-key-2024'
    
    # Database - MySQL
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'cv')
    
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 280,
        'pool_pre_ping': True,
    }
    
    # File Upload
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'pdf'}
    
    # Session
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    
    # Admin credentials (for school project)
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin123')
    
    # NLP Settings
    SPACY_MODEL = 'en_core_web_sm'
    
    # Scoring Weights
    SCORING_WEIGHTS = {
        'experience_level': 25,
        'skills_relevance': 25,
        'cv_structure': 20,
        'career_alignment': 15,
        'readability': 15
    }
    
    # CV Sections to detect
    CV_SECTIONS = [
        'professional_summary',
        'education',
        'work_experience',
        'internship_experience',
        'skills',
        'projects',
        'certifications',
        'achievements',
        'hobbies'
    ]


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
