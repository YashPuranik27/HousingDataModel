import pandas as pd
import os
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Extract constant for the default file path
DEFAULT_FILE_PATH = "../data/NY-House-Dataset.csv"


def load_housing_data(file_path=DEFAULT_FILE_PATH):
    """
    Load housing data from a specified CSV file.

    :param file_path: Path to the CSV file
    :return: Loaded Pandas DataFrame
    """
    return pd.read_csv(file_path, na_values="?")

housing_data = load_housing_data()

# identifies categories and numerical features in the data set

def preprocessdata(dataframe):
    dataframe.dropna(how="any", inplace=True)

    # Target variable
    target = "PRICE"
    y = dataframe[target].values

    # Features
    x = dataframe.drop(target, axis=1)

    # Dictionary to hold encoders
    encoders = {}

    for column in x.columns:
        if x[column].dtype == 'object':  # Check for categorical columns
            encoder = LabelEncoder()
            x[column] = encoder.fit_transform(x[column])
            encoders[column] = encoder

    xarray = x.values  # Convert to Numpy array after preprocessing

    scaler = StandardScaler()
    xarray = scaler.fit_transform(xarray)

    return xarray, y




# write a main function that loads the csv and calls preprocessed data
if __name__ == "__main__":
    housing_data = load_housing_data()
    print(housing_data)
    x, y = preprocessdata(housing_data)
    print(x)

