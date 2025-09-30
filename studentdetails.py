def get_student_details():
    print("=== Student Details Collection ===")
    
    name = input("Enter student name: ")
    usn = input("Enter student SRN: ")
    
    return name, usn

def display_student_details(name, usn):
    print("\n=== Student Information ===")
    print(f"Student Name: {name}")
    print(f"Student USN: {usn}")

def main():
    student_name, student_usn = get_student_details()
    
    display_student_details(student_name, student_usn)

if __name__ == "__main__":
    main()