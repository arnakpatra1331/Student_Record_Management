# Command-line interface and program execution (single access point)
import argparse
from manager import StudentManager
from student import Student

def main():
    parser = argparse.ArgumentParser(description="Student Record Management & Search System")
    parser.add_argument("--file", required=True, help="Path to input data file")
    parser.add_argument("--format", required=True, choices=["txt", "csv", "json", "TXT", "CSV", "JSON"], help="File format")
    
    # Optional search
    parser.add_argument("--search-id", help="Search student by ID")
    parser.add_argument("--search-name", help="Search student by Name")
    parser.add_argument("--search-dept", help="Search student by Department")
    parser.add_argument("--min-avg", type=float, help="Search students with average marks >= min-avg")
    
    parser.add_argument("--add", nargs=7, metavar=('ID', 'NAME', 'DEPT', 'SEM', 'M1', 'M2', 'M3'),
                        help="Add new student: ID Name Dept Sem Mark1 Mark2 Mark3 (e.g. 406 Arnak CSE 1 80 85 90)")
    parser.add_argument("--out", help="Output file path to save updated records")

    args = parser.parse_args()

    manager = StudentManager()
    manager.load_from_file(args.file, args.format)

    print("\n--- Loaded Records ---")
    manager.display_all_students()

    # Add new student
    if args.add:
        s_id, name, dept, sem = args.add[0], args.add[1], args.add[2], args.add[3]
        marks = [int(args.add[4]), int(args.add[5]), int(args.add[6])] if len(args.add) >= 7 else [int(args.add[4]), int(args.add[5]), 0]
        new_student = Student(s_id, name, dept, sem, marks)
        manager.add_student(new_student)
        print(f"\nAdded Student: {name}")

    # Search student by ID
    if args.search_id:
        print(f"\n--- Search Result (ID: {args.search_id}) ---")
        results = manager.search_by_id(args.search_id)
        for s in results:
            s.display_student()

    # Search student by Name
    if args.search_name:
        print(f"\n--- Search Result (Name: {args.search_name}) ---")
        results = manager.search_by_name(args.search_name)
        for s in results:
            s.display_student()

    # Search student by Result
    if args.search_dept:
        print(f"\n--- Search Result (Dept: {args.search_dept}) ---")
        results = manager.search_by_department(args.search_dept)
        for s in results:
            s.display_student()

    if args.min_avg is not None:
        print(f"\n--- Search Result (Average >= {args.min_avg}) ---")
        results = manager.search_by_average(args.min_avg)
        for s in results:
            s.display_student()

    if args.out:
        manager.save_to_file(args.out, args.format)
        print(f"\nUpdated records saved to {args.out}")

if __name__ == "__main__":
    main()