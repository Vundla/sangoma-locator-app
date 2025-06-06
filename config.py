import os

# Get the absolute path to the directory where this file is located
basedir = os.path.abspath(os.path.dirname(__file__))

# Secret key for session management and security
SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

# Database URI: SQLite database file named 'sangoma.db' in the project root folder
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'sangoma.db')}"

# Disable SQLAlchemy event system to save resources
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Folder where uploaded files (IDs, bank statements) will be stored
UPLOAD_FOLDER = os.path.join(basedir, 'uploads')

