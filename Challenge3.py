import math

studentsData = [
    {
        "name": "John Doe",
        "grades": [
            {"subject": "Math", "grade": 90},
            {"subject": "English", "grade": 85},
            {"subject": "Science", "grade": 92},
            {"subject": "History", "grade": 88},
            {"subject": "Art", "grade": 95},
        ],
    },
    {
        "name": "Jane Smith",
        "grades": [
            {"subject": "Math", "grade": 88},
            {"subject": "English", "grade": 92},
            {"subject": "Science", "grade": 87},
            {"subject": "History", "grade": 90},
            {"subject": "Art", "grade": 93},
        ],
    },
    {
        "name": "Bob Johnson",
        "grades": [
            {"subject": "Math", "grade": 78},
            {"subject": "English", "grade": 85},
            {"subject": "Science", "grade": 80},
            {"subject": "History", "grade": 88},
            {"subject": "Art", "grade": 82},
        ],
    },
]

def calculate_grades(data):
    average_grades_per_student = {}
    average_grades_per_subject = {subject: [] for subject in set(subject_grade["subject"] for student in data for subject_grade in student["grades"])}
    overall_average_grade = 0
    all_grades = []

    for student in data:
        student_name = student["name"]
        grades = [grade["grade"] for grade in student["grades"]]

        # Calculate average grade per student
        average_grades_per_student[student_name] = sum(grades) / len(grades)

        # Update the list of all grades for overall calculations
        all_grades.extend(grades)

        # Calculate average grade per subject
        for subject_grade in student["grades"]:
            subject = subject_grade["subject"]
            grade = subject_grade["grade"]

            average_grades_per_subject[subject].append(grade)

    # Calculate overall average grade
    overall_average_grade = sum(all_grades) / len(all_grades)

    # Calculate standard deviation of grades using math module
    grades_mean = sum(all_grades) / len(all_grades)
    squared_diff = sum((grade - grades_mean) ** 2 for grade in all_grades)
    grades_std_deviation = math.sqrt(squared_diff / len(all_grades))

    return {
        "average_grades": list(average_grades_per_student.values()),
        "average_subjects": { sum(grades) / len(grades) for subject, grades in average_grades_per_subject.items()},
        "overall_average": overall_average_grade,
        "std_deviation": grades_std_deviation,
    }

# Calculate metrics and print the results
results = calculate_grades(studentsData)
print("Output:", results)
