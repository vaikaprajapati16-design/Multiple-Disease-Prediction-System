# CSV Bulk Upload Feature - User Guide

## Overview
The CSV Bulk Upload feature allows you to upload multiple patient records at once and get predictions for all of them in a single batch operation. This is useful for healthcare providers, researchers, and administrators who need to process multiple patient data simultaneously.

## How to Use

### Step 1: Prepare Your CSV File
Create a CSV file with patient data. The columns depend on which disease(s) you want to predict.

### Step 2: Upload the CSV
1. Navigate to "CSV Bulk Upload" from the sidebar menu
2. Click "Choose a CSV file" and select your CSV file
3. The system will display a preview of your data (first 10 rows)

### Step 3: Select Diseases to Predict
Check the boxes for the diseases you want to predict:
- ✓ Diabetes
- ✓ Heart Disease
- ✓ Parkinson's Disease
- ✓ Breast Cancer

### Step 4: Process Predictions
Click the "Process Predictions" button and wait for the system to process all rows.

### Step 5: Review & Download Results
- View the results in an interactive table
- Check summary statistics for average risks
- Download the results as CSV for further analysis

---

## Required CSV Columns by Disease

### 1. Diabetes Prediction
**Required Columns (8 fields):**
- `Pregnancies` - Number of pregnancies (0-17)
- `Glucose` - Plasma glucose concentration (0-200)
- `BloodPressure` - Diastolic blood pressure (0-122)
- `SkinThickness` - Triceps skin fold thickness (0-99)
- `Insulin` - 2-Hour serum insulin (0-846)
- `BMI` - Body Mass Index (0.0-67.1)
- `DiabetesPedigreeFunction` - Diabetes pedigree function (0.078-2.420)
- `Age` - Age in years (21-81)

**Example CSV:**
```csv
Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
6,148,72,35,0,33.6,0.627,50
1,85,66,29,0,26.6,0.351,31
8,183,64,0,0,23.3,0.672,32
```

### 2. Heart Disease Prediction
**Required Columns (13 fields):**
- `age` - Age in years
- `sex` - Gender (0=Female, 1=Male)
- `chest_pain` - Chest pain type (1-4)
- `resting_bp` - Resting blood pressure
- `serum_cholestoral` - Serum cholesterol level
- `fasting_blood_sugar` - Fasting blood sugar (0 or 1)
- `resting_ecg` - Resting ECG results (0-2)
- `max_heart_achieved` - Maximum heart rate achieved
- `exercise_induced_angina` - Exercise induced angina (0 or 1)
- `oldpeak` - ST depression induced by exercise
- `slope_of_peak_exercise` - Slope of peak ST segment (1-3)
- `number_of_major_vessels` - Number of major vessels (0-3)
- `thal` - Thalassemia type (1-3)

### 3. Parkinson's Disease Prediction
**Required Columns (22 voice features):**
All standard Parkinson's vocal features including:
- MDVP:Fo(Hz), MDVP:Fhi(Hz), MDVP:Flo(Hz)
- MDVP:Jitter(%), MDVP:Jitter(Abs)
- MDVP:RAP, MDVP:PPQ, Jitter:DDP
- MDVP:Shimmer, MDVP:Shimmer(dB)
- Shimmer:APQ3, Shimmer:APQ5, MDVP:APQ
- Shimmer:DDA
- NHR, HNR
- RPDE, DFA, spread1, spread2, D2
- PPE

### 4. Breast Cancer Prediction
**Required Columns (30 features):**
Standard breast cancer features from the Wisconsin Breast Cancer Dataset including:
- radius, texture, perimeter, area, smoothness
- compactness, concavity, concave_points
- symmetry, fractal_dimension
- (Both mean and standard error versions of these)

---

## Output Results

After processing, you'll receive predictions with:

### For Each Disease:
- **Prediction Results**: Binary classification for each ML model (Positive/Negative)
- **Confidence Scores**: Probability percentage for each model
- **Average Risk**: Combined risk score from all models (%)

### Example Output Columns:
```
Diabetes_Pred_SVC: Positive/Negative
Diabetes_Prob_SVC: 0-100 (%)
Diabetes_Pred_LR: Positive/Negative
Diabetes_Prob_LR: 0-100 (%)
Diabetes_Pred_RF: Positive/Negative
Diabetes_Prob_RF: 0-100 (%)
Diabetes_Avg_Risk: 0-100 (%)
```

---

## Sample Files

Sample CSV files are provided:
- `sample_diabetes.csv` - Diabetes prediction example
- `sample_heart_disease.csv` - Heart disease prediction example

These can be used to test the feature with known data.

---

## Tips & Best Practices

1. **Data Validation**: Ensure all values are numeric and within expected ranges
2. **Missing Values**: Replace NaN or empty cells with 0 or appropriate defaults
3. **Column Names**: Must match exactly (case-sensitive)
4. **Batch Size**: Works efficiently with 100-1000+ records at once
5. **Error Handling**: The system will skip rows with missing data and report errors

---

## Limitations & Notes

- Ensure column names exactly match the requirements
- All numeric fields should be in the appropriate range for medical data
- Processing time depends on the number of rows (typically 1-2 seconds per 100 rows)
- Results should not be used as medical diagnosis; consult healthcare professionals
- Downloaded CSV preserves all original data plus prediction results

---

## Troubleshooting

**Error: "Column X not found in CSV"**
- Check that your CSV has all required columns
- Verify column names match exactly (case-sensitive)

**Error: "Invalid data type"**
- Ensure all values are numeric
- Replace any text or special characters with appropriate numeric values

**Slow Processing**
- This is normal for large datasets
- Processing speed: ~100 rows per second

---

For more information, visit the Dashboard or individual disease prediction pages.
