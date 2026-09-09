## A. Title
**Student Record Management & Search System**  
*AI/ML Laboratory | B.Tech. 5th Semester* | Arnak Patra | Roll 31

---

## B. Objective
The objective of this assignment is to design and implement a modular, command-line-driven **Student Record Management & Search System** in Python using Object-Oriented Programming (OOP) principles. 

The project demonstrates core Python programming concepts including:
* Custom class architecture and object interactions without relying on external frameworks.
* Standard file input/output operations across multiple data formats (**TXT**, **CSV**, and **JSON**) using built-in modules.
* Custom algorithmic searching and filtering logic using basic loops and conditional statements.
* Command-line argument parsing and program configuration using `argparse`.

---

## C. Features
* **Multi-Format File Support**: Load and save student records seamlessly across `.txt`, `.csv`, and `.json` formats.
* **Student Record Management**: Create student entities, compute academic statistics (total marks, average marks, pass/fail result), and dynamically add new records.
* **Command-Line Interface (CLI)**: Flexibly run operations (loading, searching, adding, saving) using standard execution flags.
* **ID-Based Exact Search**: Retrieve specific student records matching a unique Student ID.
* **Name Substring Search**: Perform case-insensitive search matching student names.
* **Department Search**: Filter students based on their department or field of study.
* **Condition-Based Search (Threshold Filtering)**: Filter and identify students achieving an average mark at or above a user-specified threshold.
* **Dynamic Record Updates & Export**: Add new records via CLI and persist updated datasets into a target file format.

---

## D. Project Structure
The project is organized into four distinct Python modules alongside sample data files as recommended by the project guidelines:

```text
student-record-system/
│
├── main.py             # Command-line interface and program execution entry point
├── student.py          # Student class definition, attribute setup, and academic calculations
├── manager.py          # StudentManager class managing collections of Student objects
├── file_handler.py     # Lower-level file I/O operations for TXT, CSV, and JSON formats
│
├── data/
│   ├── students.txt    # Sample input/output text dataset
│   ├── students.csv    # Sample input/output CSV dataset
│   └── students.json   # Sample input/output JSON dataset
│
└── README.md           # Complete project documentation and submission report
```

### Module Responsibilities
* **`main.py`**: Acts as the single entry point. Parses command-line arguments using `argparse`, initializes `StudentManager`, invokes file loading, triggers search/add operations, and outputs results.
* **`student.py`**: Defines the `Student` model class. Stores core student attributes (`student_id`, `name`, `department`, `semester`, `marks`) and handles calculations (`calculate_total`, `calculate_average`, `get_result`, `update_marks`, `display_student`).
* **`manager.py`**: Implements the `StudentManager` class. Manages an in-memory list of `Student` objects, offering methods for adding, removing, searching (by ID, name, department, average), and delegating file I/O operations.
* **`file_handler.py`**: Contains helper functions (`read_txt`, `write_txt`, `read_csv`, `write_csv`, `read_json`, `write_json`) to handle file parsing and serializing using Python's standard libraries.

---

## E. Requirements
* **Environment**: Python 3.7 or higher.
* **External Dependencies**: None. Standard Python modules (`csv`, `json`, `argparse`) are used exclusively in compliance with assignment guidelines.

---

## F. How to Run

Execute `main.py` from the terminal by providing the required `--file` and `--format` flags.

### 1. Basic Execution (Load and Display Records)
```bash
python main.py --file data/students.csv --format csv
```

### 2. Searching by Student ID
```bash
python main.py --file data/students.json --format json --search-id 101
```

### 3. Substring Search by Name
```bash
python main.py --file data/students.txt --format txt --search-name Priya
```

### 4. Search by Department
```bash
python main.py --file data/students.csv --format csv --search-dept "Computer Science"
```

### 5. Condition-Based Search (Minimum Average Marks)
```bash
python main.py --file data/students.json --format json --min-avg 75.0
```

### 6. Adding a New Student and Saving Output
```bash
python main.py --file data/students.csv --format csv --add 106 "Rohan Verma" "Electronics" 2 85 90 88 --out data/updated_students.csv
```

---

## G. Input and Output

### Input Formats
* **CSV (`students.csv`)**: Header line followed by comma-separated student attributes:
  ```csv
  Student ID, Name, Department, Semester, Subject1, Subject2, Subject3
  101, Rahul, Computer Science, 1, 78, 82, 69
  ```
* **TXT (`students.txt`)**: Comma-delimited line records:
  ```text
  101, Rahul, Computer Science, 1, 78, 82, 69
  102, Priya, Computer Science, 1, 91, 87, 94
  ```
* **JSON (`students.json`)**: Array of JSON objects:
  ```json
  [
      {
          "student_id": 101,
          "name": "Rahul",
          "department": "Computer Science",
          "semester": 1,
          "marks": {
              "subject1": 78,
              "subject2": 82,
              "subject3": 69
          }
      }
  ]
  ```

### Output Location
Outputs are displayed directly in the terminal console. If `--out` is specified, updated records are written to the provided path.

### Sample Output Example
```text
$ python main.py --file data/students.csv --format csv --search-name Priya

--- Loaded Records ---
ID: 101 | Name: Rahul | Dept: Computer Science | Sem: 1 | Marks: [78, 82, 69] | Total: 229 | Avg: 76.33 | Status: Pass
ID: 102 | Name: Priya | Dept: Computer Science | Sem: 1 | Marks: [91, 87, 94] | Total: 272 | Avg: 90.67 | Status: Pass
ID: 103 | Name: Amit | Dept: Mathematics | Sem: 1 | Marks: [65, 71, 68] | Total: 204 | Avg: 68.00 | Status: Pass

--- Search Result (Name: Priya) ---
ID: 102 | Name: Priya | Dept: Computer Science | Sem: 1 | Marks: [91, 87, 94] | Total: 272 | Avg: 90.67 | Status: Pass
```

---

## H. OOP Concepts Used
* **Classes & Objects**:
  * `Student` in `student.py` represents individual student entities.
  * `StudentManager` in `manager.py` manages collections of `Student` objects.
* **Constructors (`__init__`)**:
  * `Student.__init__` initializes student attributes and converts data types appropriately (e.g., strings to integers for marks and semester).
  * `StudentManager.__init__` initializes an empty internal list `self.students`.
* **Attributes**:
  * Encapsulated instance attributes such as `self.student_id`, `self.name`, `self.department`, `self.semester`, and `self.marks`.
* **Instance Methods**:
  * Behavior-driven methods like `calculate_total()`, `calculate_average()`, `get_result()`, and `display_student()` operate directly on `Student` instances.

---

## I. File Handling Concepts Used
* **Text File Processing (`read_txt`, `write_txt`)**: Uses `open()` with mode `'r'` and `'w'` within `with` blocks. Standard string manipulation (`strip()`, `split(',')`) parses line entries.
* **CSV Processing (`read_csv`, `write_csv`)**: Utilizes Python's standard `csv` module. `csv.reader()` handles line extraction while `next(reader)` strips the header row. `csv.writer()` handles clean tabular output.
* **JSON Processing (`read_json`, `write_json`)**: Uses `json.load()` to parse JSON files into Python dictionaries/lists and `json.dump()` with `indent=4` to serialize objects into formatted JSON files.

---

## J. Searching Concepts Used
All search features are constructed using fundamental Python control flow (`for` loops, `if` statements, standard comparison operators) without reliance on external analytical libraries:

* **ID Search (`search_by_id`)**: Iterates through `self.students` comparing `s.student_id == str(target_id)`.
* **Name Search (`search_by_name`)**: Iterates through records using substring matching with `target_name.lower() in s.name.lower()`.
* **Department Search (`search_by_department`)**: Performs case-insensitive matching against `s.department`.
* **Condition-Based Search (`search_by_average`)**: Computes `s.calculate_average()` for each student and evaluates if `avg >= min_avg`.

---

## K. Learning Outcome & Conclusion
Through this assignment, I reinforced my practical understanding of fundamental Object-Oriented Programming (OOP) in Python and learned how to build a clean, modular application architecture. Separating responsibilities across separate files (`student.py`, `manager.py`, `file_handler.py`, `main.py`) highlighted the benefits of loose coupling and high cohesion.

Key technical takeaways include:
* Parsing and writing data across different file formats (**TXT**, **CSV**, **JSON**) using native Python libraries.
* Implementing robust argument parsing with `argparse`.
* Writing clean filtering and mathematical evaluation logic from scratch using core Python iteration constructs.

---
