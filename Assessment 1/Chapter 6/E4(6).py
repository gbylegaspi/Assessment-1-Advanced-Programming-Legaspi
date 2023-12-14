import json

# Function to write student details to a JSON file
def write_to_json(file_path, details):
    """Write student details to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(details, file)

# Function to read and print student details from a JSON file
def read_from_json(file_path):
    """Read and print student details from a JSON file."""
    with open(file_path, 'r') as file:
        details = json.load(file)
        print("\nDetails of the Student are")
        print(f"\tName: {details['Name']}")
        print(f"\tID: {details['ID']}")
        print(f"\tCourse: {details['Course']}")
        course_details = details.get("CourseDetails", {})
        print(f"\tGroup: {course_details.get('Group', 'N/A')}")
        print(f"\tYear: {course_details.get('Year', 'N/A')}")

# JSON file name
json_file_name = 'StudentJson.json'

# Prompt user for input and store in a dictionary
name = input("Enter the student name: ")
student_id = input("Enter the student ID: ")
course_name = input("Enter the course: ")

# Dictionary to hold student details
student_info = {
    "Name": name,
    "ID": int(student_id),
    "Course": course_name
}

# Write initial details to JSON file
write_to_json(json_file_name, student_info)

# Additional course details dictionary
additional_course_info = {
    "Group": "A",
    "Year": 2
}

# Update student details dictionary with additional course details
student_info["CourseDetails"] = additional_course_info

# Update JSON file with the additional details
write_to_json(json_file_name, student_info)

# Read and print details from JSON file
read_from_json(json_file_name)
