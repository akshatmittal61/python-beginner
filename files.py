from dotenv import load_dotenv
import os

load_dotenv()
version = os.getenv('MONGO_URL')
print(version)
