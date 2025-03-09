# Housing Data Model

A machine learning project for housing price prediction using TensorFlow, MongoDB, scikit-learn, and containerized with Docker.

## Project Overview

This project builds a predictive model for housing prices based on features like location, size, number of bedrooms/bathrooms, etc. The system uses:

- TensorFlow for the neural network model
- MongoDB for data storage
- Python data science libraries (pandas, numpy, scikit-learn) for data processing
- Docker for containerization

## Dataset Features

The housing dataset includes the following features:

- `BROKERTITLE`: Title of the broker
- `TYPE`: Type of the house
- `PRICE`: Price of the house (target variable)
- `BEDS`: Number of bedrooms
- `BATH`: Number of bathrooms
- `PROPERTYSQFT`: Square footage of the property
- `ADDRESS`: Full address of the house
- `STATE`: State of the house
- Various location fields (LATITUDE, LONGITUDE, etc.)

## Project Structure

```
HousingDataModel/
│
├── data/                  # Data directory
├── models/                # Saved model files
├── src/                   # Source code
│   ├── __init__.py
│   ├── config.py          # Configuration settings
│   ├── data_utils.py      # Data loading and preprocessing
│   ├── model.py           # Machine learning model definition
│   └── train.py           # Model training script
├── notebooks/             # Jupyter notebooks for exploration
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
├── .env                   # Environment variables
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Setup and Installation

### Using Docker (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/HousingDataModel.git
   cd HousingDataModel
   ```

2. Build and start the Docker containers:
   ```bash
   docker-compose up -d
   ```

   This will start three containers:
   - The main app container that runs the training script
   - MongoDB for data storage
   - Jupyter notebook server for data exploration

3. Access Jupyter notebooks at http://localhost:8888

### Without Docker

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/HousingDataModel.git
   cd HousingDataModel
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the training script:
   ```bash
   python src/train.py
   ```

## Data

The model expects housing data with the features listed in the Project Overview section. If no data file is present, the system will generate sample data for testing purposes.

To use your own data:
1. Place your CSV file at `data/housing_data.csv`
2. Ensure it contains the necessary columns (PRICE, BEDS, BATH, etc.)

## MongoDB Integration

The project is configured to work with MongoDB:

- Data can be loaded from and saved to MongoDB
- The database connection settings are in the `.env` file
- Default database name: `housing_data`
- Default collection name: `properties`
