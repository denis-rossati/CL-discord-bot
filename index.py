import os
from src.client import client
from dotenv import load_dotenv

load_dotenv()

client.run(os.environ.get('TOKSON'))