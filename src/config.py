import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB Configuration
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("DB_NAME", "housing_data")
COLLECTION_NAME = "properties"

# Model Configuration
MODEL_NAME = os.getenv("MODEL_NAME", "housing_price_model")
MODEL_SAVE_PATH = os.getenv("MODEL_SAVE_PATH", "./models/")

# Data Configuration
DATA_PATH = "./data/housing_data.csv"

# Training Configuration
RANDOM_SEED = 42
TEST_SIZE = 0.2
VALIDATION_SIZE = 0.1
BATCH_SIZE = 32
EPOCHS = 100
LEARNING_RATE = 0.001

# Feature Configuration
NUMERICAL_FEATURES = ["BEDS", "BATH", "PROPERTYSQFT", "LATITUDE", "LONGITUDE"]
CATEGORICAL_FEATURES = ["TYPE", "STATE", "BROKERTITLE"]
TARGET_FEATURE = "PRICE"

# Create directories if they don't exist
os.makedirs(MODEL_SAVE_PATH, exist_ok=True)
os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)