# Student Performance Prediction

My first machine learning project — a simple regression model that predicts a student's math score based on demographic and academic information.

## About

This project was built to learn and validate the basic end-to-end machine learning workflow.

The trained preprocessing and model are saved together as a pipeline and later loaded by `main.py` to make predictions from new user input.

## Features

The model uses:

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch
* Test Preparation Course
* Reading Score
* Writing Score

## Dataset

This project uses the **Students Performance in Exams** dataset from Kaggle.

Dataset Source:
https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

## Workflow

```text
Dataset
   ↓
Preprocessing
   ↓
Model Training
   ↓
Evaluation
   ↓
Pipeline
   ↓
Save Pipeline
   ↓
Load Pipeline
   ↓
User Input
   ↓
Prediction
```

## Example

Example input:

```text
female
group B
bachelor's degree
standard
none
72
74
```

Example prediction:

```text
66.11
```

## How to Run

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python main.py
```

Enter the requested student information when prompted.

## Project Structure

```text
student-performance-prediction/
│
├── StudentsPerformance.csv
├── student_pipeline.pkl
├── train.py
├── main.py
├── model_training.ipynb
├── requirements.txt
└── README.md
```

## Project Status

Completed — **25 August 2026**

This project serves as my first ML project and focuses on understanding and implementing a basic regression workflow.
