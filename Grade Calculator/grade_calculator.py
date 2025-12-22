# Student Grade Calculator
# Week 2 Project - Control Flow & Data Structures

def calculate_grade(average):
    """Calculate grade based on average marks"""
    if average >= 90:
        return 'A', 'Excellent! Keep up the great work!'
    elif average >= 80:
        return 'B', 'Very Good! You\'re doing well.'
    elif average >= 70:
        return 'C', 'Good. Room for improvement.'
    elif average >= 60:
        return 'D', 'Needs Improvement. Please study more.'
    else:
        return 'F', 'Failed. Please seek help from teacher.'

def get_valid_number(prompt, min_val=0, max_val=100):
    """Get a valid number within specified range"""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_color_code(grade):
    """Return ANSI color code based on grade"""
    colors = {
        'A': '\033[92m',
        'B': '\033[93m',
        'C': '\033[94m',
        'D': '\033[91m', 
        'F': '\033[91m'   
    }
    return colors.get(grade, '\033[0m')  

def reset_color():
    """Reset color to default"""
    return '\033[0m'

def search_student(student_names, student_results):
    """Search for a specific student"""
    search_name = input("Enter student name to search: ").strip().lower()
    found = False
    for i, name in enumerate(student_names):
        if name.lower() == search_name:
            result = student_results[i]
            print(f"\nStudent Found: {name}")
            print(f"Average: {result['average']:.1f}")
            print(f"Grade: {result['grade']}")
            print(f"Comment: {result['comment']}")
            found = True
            break
    if not found:
        print("Student not found.")

def save_results_to_file(student_names, student_results, class_stats):
    """Save results to a file"""
    filename = input("Enter filename to save (e.g., results.txt): ").strip()
    if not filename:
        filename = "grade_results.txt"
    try:
        with open(filename, 'w') as f:
            f.write("STUDENT GRADE CALCULATOR RESULTS\n")
            f.write("=" * 50 + "\n")
            f.write(f"{'Name':<20} | {'Avg':>5} | {'Grade':^5} | Comment\n")
            f.write("-" * 60 + "\n")
            for i in range(len(student_names)):
                name = student_names[i]
                avg = student_results[i]['average']
                grade = student_results[i]['grade']
                comment = student_results[i]['comment']
                f.write(f"{name:<20} | {avg:>5.1f} | {grade:^5} | {comment}\n")
            f.write("\nCLASS STATISTICS\n")
            f.write("=" * 50 + "\n")
            for key, value in class_stats.items():
                f.write(f"{key}: {value}\n")
        print(f"Results saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

def display_menu():
    """Display main menu"""
    print("\n" + "=" * 50)
    print("      STUDENT GRADE CALCULATOR MENU")
    print("=" * 50)
    print("1. Calculate Grades")
    print("2. Search Student")
    print("3. Save Results to File")
    print("4. Exit")
    print("=" * 50)

def main():
    student_names = []
    student_results = []
    class_stats = {}

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '1':
            calculate_grades(student_names, student_results, class_stats)
        elif choice == '2':
            if student_names:
                search_student(student_names, student_results)
            else:
                print("No student data available. Please calculate grades first.")
        elif choice == '3':
            if student_names:
                save_results_to_file(student_names, student_results, class_stats)
            else:
                print("No student data available. Please calculate grades first.")
        elif choice == '4':
            print("Thank you for using the Grade Calculator!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

def calculate_grades(student_names, student_results, class_stats):
    print("=" * 50)
    print("      STUDENT GRADE CALCULATOR")
    print("=" * 50)
    print()
    
    while True:
        try:
            num_students = int(input("Enter number of students: "))
            if num_students > 0:
                break
            else:
                print("Please enter a positive number!")
        except ValueError:
            print("Invalid input! Please enter a whole number.")
    
    student_names.clear()
    student_results.clear()
    
# Collect data for each student
    for i in range(num_students):
        print(f"\n=== STUDENT {i+1} ===")
        
        # Get student name
        name = input("Student name: ")
        while name.strip() == "":
            print("Name cannot be empty!")
            name = input("Student name: ")
        student_names.append(name)
        
        print("Enter marks (0-100):")
        math = get_valid_number("Math: ")
        science = get_valid_number("Science: ")
        english = get_valid_number("English: ")
        
        average = (math + science + english) / 3
        grade, comment = calculate_grade(average)

        student_results.append({
            'average': average,
            'grade': grade,
            'comment': comment
        })
    
    print("\n" + "=" * 50)
    print("  RESULTS SUMMARY")
    print("=" * 50)
    print(f"{'Name':<20} | {'Avg':>5} | {'Grade':^5} | Comment")
    print("-" * 60)
    
    for i in range(num_students):
        name = student_names[i]
        avg = student_results[i]['average']
        grade = student_results[i]['grade']
        comment = student_results[i]['comment']
        
        color = get_color_code(grade)
        reset = reset_color()
        print(f"{name:<20} | {avg:>5.1f} | {color}{grade:^5}{reset} | {comment}")
    
    # Calculate and display statistics
    if num_students > 0:
        averages = [result['average'] for result in student_results]
        class_avg = sum(averages) / len(averages)
        max_avg = max(averages)
        min_avg = min(averages)
        max_index = averages.index(max_avg)
        min_index = averages.index(min_avg)
        
        class_stats.update({
            'Total Students': num_students,
            'Class Average': f"{class_avg:.1f}",
            'Highest Average': f"{max_avg:.1f} ({student_names[max_index]})",
            'Lowest Average': f"{min_avg:.1f} ({student_names[min_index]})"
        })
        
        print("\n" + "=" * 50)
        print("          CLASS STATISTICS")
        print("=" * 50)
        for key, value in class_stats.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
