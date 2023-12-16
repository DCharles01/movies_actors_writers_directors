import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME=os.getenv('DATABASE')
DB_USER=os.getenv('USER')
DB_PASSWORD=os.getenv('PASSWORD')
DB_HOST=os.getenv('HOST')

