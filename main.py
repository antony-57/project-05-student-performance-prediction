#           Project 5 — Student Exam Score Prediction
# 
# Build a machine learning model to predict a student's exam score.
# Use study hours and other available student factors as input features.
# Train a regression model using the student dataset.
# Make predictions on unseen/test data.
# Compare the predicted scores with the actual scores.
# Provide a simple evaluation report using an appropriate metric such as accuracy/error rate.


import joblib
import pandas as pd
# from sklearn.pipeline import Pipeline
# from sklearn.linear_model import LinearRegression

# df = pd.read_csv("StudentsPerformance.csv")

# X = df.drop("math score", axis=1)
# y = df["math score"]

pipeline = joblib.load("student_score_pipeline.pkl")

gender = input()
race_ethnicity = input()
parental_level_of_education = input()
lunch = input()
test_preparation_course = input()
reading_score = int(input())
writing_score = int(input())

student = pd.DataFrame([
    {
        "gender": gender,
        "race/ethnicity": race_ethnicity,
        "parental level of education": parental_level_of_education,
        "lunch": lunch,
        "test preparation course": test_preparation_course,
        "reading score": reading_score,
        "writing score": writing_score
    }
])

prediction = pipeline.predict(student)[0]

print("Predicted Math Score: ",prediction)

