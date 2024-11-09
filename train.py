# Import libraries
import pickle
import datetime as dt

import pandas as pd
import numpy as np

from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Variables
data_file = './data/data.csv'
model_file = 'model.bin'

# Load data
print(f'Loading data from file {data_file}...')

df = pd.read_csv(data_file)

# Prepare data
print('Preparing data...')

# Convert object columns to numeric
df['land_size_sqm'] = pd.to_numeric(df['land_size_sqm'].str.replace(' sqm', ''))
df['house_size_sqm'] = pd.to_numeric(df['house_size_sqm'].str.replace(' sqm', ''))
df['distance_to_school'] = pd.to_numeric(df['distance_to_school'].str.replace('km', ''))
df['distance_to_supermarket'] = pd.to_numeric(df['distance_to_supermarket'].str.replace(' km', ''))
df['house_age'] = pd.to_numeric(df['house_age'].str.replace(' Years', ''))

# Convert Yes/No columns to 1/0
df['large_living_room'] = pd.to_numeric(df['large_living_room'].replace({'No': '0', 'Yes': '1'}))
df['parking_space'] = pd.to_numeric(df['parking_space'].replace({'No': '0', 'Yes': '1'}))
df['front_garden'] = pd.to_numeric(df['front_garden'].replace({'No': '0', 'Yes': '1'}))
df['swimming_pool'] = pd.to_numeric(df['swimming_pool'].replace({'No': '0', 'Yes': '1'}))
df['wall_fence'] = pd.to_numeric(df['wall_fence'].replace({'No': '0', 'Yes': '1'}))
df['water_front'] = pd.to_numeric(df['water_front'].replace({'No': '0', 'Yes': '1'}))
df['room_size'] = pd.to_numeric(df['room_size'].replace({'small': '0', 'medium': '1', 'large': '2', 'extra_large': '3'}))

# We split our dataset into train (80%) and test (20%)
df_train, df_test = train_test_split(df, test_size=0.2, random_state=1)

# Reindex dataframe index
df_train = df_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

# Get target variable from the train, val, test datasets
y_train = np.log1p(df_train['property_value'].values)
y_test = np.log1p(df_test['property_value'].values)

# Save test data to a csv file
df_test.to_csv('./data/test.csv')

# Delete the target variable from the datasets
del df_train['property_value']
del df_test['property_value']

# Create dictionaries
dict_train = df_train.to_dict(orient='records')
dict_test = df_test.to_dict(orient='records')

# Create vectorizer
dv = DictVectorizer(sparse=True)

# Create feature matrices
X_train = dv.fit_transform(dict_train)
X_test = dv.transform(dict_test)

# Train model
print('Training model...')

rf = RandomForestRegressor(n_estimators=200, max_depth=15, random_state=1, n_jobs=-1)
rf.fit(X_train, y_train)

# Save directory vectorizer and model into a file
print('Saving model to a file...')

with open(model_file, 'wb') as f_out:
    pickle.dump((dv, rf), f_out)

print(f'Model saved to {model_file}')