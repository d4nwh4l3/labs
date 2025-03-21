import ast
import os
import re
import sys

class StyleChecker:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(self.file_path, "r", encoding="utf-8") as f:
            self.content = f.read()
            self.lines = self.content.splitlines()
        self.tree = ast.parse(self.content)
        self.report = []

    def _parse_file(self):
        """Parses the Python file into an AST tree."""
        return self.tree
    
    def get_file_structure(self):
        """Extracts the file structure: lines of code, imports, classes, and functions."""
        with open(self.file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        num_lines = len(lines)
        imports = [node.names[0].name for node in ast.walk(self.tree) if isinstance(node, ast.Import)]
        classes = [node.name for node in ast.walk(self.tree) if isinstance(node, ast.ClassDef)]
        
        functions = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                for parent in ast.walk(self.tree):
                    if isinstance(parent, ast.ClassDef) and node in parent.body:
                        functions.append(f"{parent.name}_{node.name}")
                        break
                else:
                    functions.append(node.name)

        self.report.append(f"Total Lines: {num_lines}")
        self.report.append(f"Imports: {', '.join(imports) if imports else 'None'}")
        self.report.append(f"Classes: {', '.join(classes) if classes else 'None'}")
        self.report.append(f"Functions: {', '.join(functions) if functions else 'None'}")


    def extract_docstrings(self):
        """Extracts docstrings from classes and functions."""
        for node in ast.walk(self.tree):
            if isinstance(node, (ast.ClassDef, ast.FunctionDef)):
                docstring = ast.get_docstring(node) or "DocString not found"
                self.report.append(f"{node.name}: {docstring}")
                self.report.append("") 

    def check_type_annotations(self):
        """Checks if functions and methods have type annotations."""
        missing_annotations = []

        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                if not node.returns or not all(arg.annotation for arg in node.args.args):
                    missing_annotations.append(node.name)

        if missing_annotations:
            self.report.append("Functions without type annotations: " + ", ".join(missing_annotations))
        else:
            self.report.append("All functions and methods have type annotations.")

    def check_naming_conventions(self):
        """Checks if class and function names follow proper conventions."""
        improper_classes = []
        improper_functions = []

        camel_case = re.compile(r'^[A-Z][a-zA-Z0-9]*$')
        snake_case = re.compile(r'^[a-z_][a-z0-9_]*$')

        for node in ast.walk(self.tree):
            if isinstance(node, ast.ClassDef):
                if not camel_case.match(node.name):
                    improper_classes.append(node.name)
            elif isinstance(node, ast.FunctionDef):
                if not snake_case.match(node.name):
                    improper_functions.append(node.name)

        if improper_classes:
            self.report.append("Classes not following CamelCase: " + ", ".join(improper_classes))
        else:
            self.report.append("All classes follow CamelCase naming.")

        if improper_functions:
            self.report.append("Functions not following snake_case: " + ", ".join(improper_functions))
        else:
            self.report.append("All functions follow snake_case naming.")

    def generate_report(self):
        """Writes the analysis to a text file in the same directory as the source file."""
        source_dir = os.path.dirname(os.path.abspath(self.file_path))
        source_filename = os.path.basename(self.file_path)
        report_filename = f"style_report_{source_filename}.txt"
        
        report_path = os.path.join(source_dir, report_filename)
        
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("\n".join(self.report))
        print(f"Report generated: {report_path}")

if __name__ == "__main__":
    directory_path = os.path.dirname(os.path.abspath(__file__))
    filename = None

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:

        current_script = os.path.basename(__file__)
        py_files = [f for f in os.listdir(directory_path) 
                   if f.endswith('.py') and f != current_script]
        
        if not py_files:
            print(f"No Python files found in the current directory (excluding {current_script})")
            sys.exit(1)
            
        if len(py_files) == 1:
            confirm = input(f"Found {py_files[0]}. Would you like to check this file? (y/n): ")
            if confirm.lower() == 'y':
                filename = py_files[0]
            else:
                print("Operation cancelled.")
                sys.exit(0)
        else:

            print("Available Python files:")
            for i, file in enumerate(py_files, 1):
                print(f"{i}. {file}")
            
            while True:
                try:
                    choice = int(input("Enter the number of the file to check (or 0 to cancel): "))
                    if choice == 0:
                        print("Operation cancelled.")
                        sys.exit(0)
                    if 1 <= choice <= len(py_files):
                        filename = py_files[choice - 1]
                        break
                    else:
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Please enter a valid number.")

    if not filename:
        print("No file selected. Operation cancelled.")
        sys.exit(0)

    file_to_check = os.path.join(directory_path, filename)

    if not os.path.isfile(file_to_check):
        print(f"Error: File '{file_to_check}' not found.")
        sys.exit(1)

    print(f"About to check file: {filename}")
    confirm = input("Proceed? (y/n): ")
    if confirm.lower() != 'y':
        print("Operation cancelled.")
        sys.exit(0)

    checker = StyleChecker(file_to_check)
    checker.get_file_structure()
    checker.extract_docstrings()
    checker.check_type_annotations()
    checker.check_naming_conventions()
    checker.generate_report()