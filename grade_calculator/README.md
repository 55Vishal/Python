# Student Grade Calculator

A comprehensive Python program for calculating and managing student grades with a user-friendly menu interface.

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Grading System](#grading-system)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Interactive Menu System**: Easy navigation with 4 main options
- **Grade Calculation**: Automatic calculation of grades based on average marks
- **Multi-Subject Support**: Handles marks for Math, Science, and English
- **Input Validation**: Ensures valid marks (0-100) and positive student count
- **Color-Coded Results**: Visual grade representation using ANSI colors
- **Class Statistics**: Comprehensive statistics including class average, highest/lowest scores
- **Student Search**: Search functionality to find specific students
- **File Export**: Save results to text files for record-keeping
- **Error Handling**: Robust error handling for all user inputs

## 🔧 Requirements

- Python 3.x
- No external dependencies required (uses only standard library)

## 🚀 Installation 

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student-grade-calculator.git
   ```

2. Navigate to the project directory:
   ```bash
   cd student-grade-calculator
   ```

## 📖 Usage

Run the program using Python:

```bash
python grade_calculator.py
```

### Menu Options:

1. **Calculate Grades**: Input student information and calculate grades
2. **Search Student**: Search for a specific student by name
3. **Save Results to File**: Export results to a text file
4. **Exit**: Close the application

### Input Format:

- Enter number of students (must be positive integer)
- For each student:
  - Student name (cannot be empty)
  - Marks for Math (0-100)
  - Marks for Science (0-100)
  - Marks for English (0-100)

## 📊 Sample Output

```
==================================================
      STUDENT GRADE CALCULATOR MENU
==================================================
1. Calculate Grades
2. Search Student
3. Save Results to File
4. Exit
==================================================

Enter your choice (1-4): 1
==================================================
      STUDENT GRADE CALCULATOR
==================================================

Enter number of students: 2

=== STUDENT 1 ===
Student name: John Smith
Enter marks (0-100):
Math: 85
Science: 92
English: 88

=== STUDENT 2 ===
Student name: Sarah Johnson
Enter marks (0-100):
Math: 78
Science: 81
English: 85

==================================================
            RESULTS SUMMARY
==================================================
Name                 |   Avg | Grade | Comment
------------------------------------------------------------
John Smith           |  88.3 |   B   | Very Good! You're doing well.
Sarah Johnson        |  81.3 |   B   | Very Good! You're doing well.

==================================================
          CLASS STATISTICS
==================================================
Total Students: 2
Class Average: 84.8
Highest Average: 88.3 (John Smith)
Lowest Average: 81.3 (Sarah Johnson)
```

## 📈 Grading System

| Average Range | Grade | Comment |
|---------------|-------|---------|
| 90-100 | A | Excellent! Keep up the great work! |
| 80-89 | B | Very Good! You're doing well. |
| 70-79 | C | Good. Room for improvement. |
| 60-69 | D | Needs Improvement. Please study more. |
| 0-59 | F | Failed. Please seek help from teacher. |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
