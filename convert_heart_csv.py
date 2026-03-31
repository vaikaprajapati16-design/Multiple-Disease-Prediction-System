import pandas as pd

# Read the original Heart Disease CSV
df = pd.read_csv('Datasets/Heart Disease Data.csv')

print(f"Original shape: {df.shape}")
print(f"Original columns: {df.columns.tolist()}")

# Rename columns to match the app requirements
column_mapping = {
    'cp': 'chest_pain',
    'trestbps': 'resting_bp',
    'chol': 'serum_cholestoral',
    'fbs': 'fasting_blood_sugar',
    'restecg': 'resting_ecg',
    'thalach': 'max_heart_achieved',
    'exang': 'exercise_induced_angina',
    'slope': 'slope_of_peak_exercise',
    'ca': 'number_of_major_vessels'
}

df_converted = df.rename(columns=column_mapping)

# Remove target column if present (not needed for prediction input)
if 'target' in df_converted.columns:
    df_converted = df_converted.drop('target', axis=1)

# Select only the required columns in the right order
required_columns = [
    'age', 'sex', 'chest_pain', 'resting_bp', 'serum_cholestoral',
    'fasting_blood_sugar', 'resting_ecg', 'max_heart_achieved',
    'exercise_induced_angina', 'oldpeak', 'slope_of_peak_exercise',
    'number_of_major_vessels', 'thal'
]

df_final = df_converted[required_columns]

# Save the converted CSV
output_file = 'Heart_Disease_Converted.csv'
df_final.to_csv(output_file, index=False)

print(f"\n✅ Converted! New shape: {df_final.shape}")
print(f"✅ New columns: {df_final.columns.tolist()}")
print(f"\n✅ File saved as: {output_file}")
print(f"✅ Ready to upload in CSV Bulk Upload section!")
