# Statement for enabling the development environment
DEBUG = False

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database : SQLite 
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
#DATABASE_CONNECT_OPTIONS = {}

# Application threads : 2 per available processor cores to handle incoming requests using one and performing background operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for signing the data.
CSRF_SESSION_KEY = "7cbbbfb46e4300823a400ec799c32b828b391d47fd403360"

# Secret key for signing cookies
SECRET_KEY = "7cbbbfb46e4300823a400ec799c32b828b391d47fd403360"
