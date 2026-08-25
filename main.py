#           Project 5 — Student Exam Score Prediction


import joblib
import pandas as pd

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

