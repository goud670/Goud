# Goud
# Import necessary libraries
import pandas as pd
import zipfile
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Extract ZIP file
zip_file_path = "/mnt/data/IoTProcessed_Data.csv.zip"
extract_folder = "/mnt/data/iot_data"

with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
    zip_ref.extractall(extract_folder)

# Find extracted CSV file
extracted_files = os.listdir(extract_folder)
csv_file_path = None

for file in extracted_files:
    if file.endswith(".csv"):
        csv_file_path = os.path.join(extract_folder, file)
        break

# Load dataset
df = pd.read_csv(csv_file_path)

# Convert 'date' column to datetime and sort
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

# Define features and target variable
features = ["tempreature", "humidity", "water_level", "N", "P", "K"]
target = "Watering_plant_pump_ON"

# Split data into train (80%) and test (20%) sets
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

# Train Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
rf_model.fit(X_train, y_train)

# Model evaluation
y_pred = rf_model.predict(X_test)

# Classification metrics
class_report = classification_report(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Print results
print("Classification Report:\n", class_report)
print("\nConfusion Matrix:\n", conf_matrix)
