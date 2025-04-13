import ast
import os
import re

def read_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def parse_ast(file_content: str) -> ast.AST:
    return ast.parse(file_content)

def analyze_file_structure(tree: ast.AST, file_content: str) -> list[str]:
    lines = file_content.splitlines()
    num_lines = len(lines)

    imports = [node.names[0].name for node in ast.walk(tree) if isinstance(node, ast.Import)]
    classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and not isinstance(getattr(node, 'parent', None), ast.ClassDef)]

    return [
        f"Total Lines: {num_lines}",
        f"Imports: {', '.join(imports) if imports else 'None'}",
        f"Classes: {', '.join(classes) if classes else 'None'}",
        f"Functions: {', '.join(functions) if functions else 'None'}"
    ]

def extract_docstrings(tree: ast.AST) -> list[str]:
    doc_lines = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.ClassDef, ast.FunctionDef)):
            docstring = ast.get_docstring(node) or "DocString not found"
            doc_lines.append(f"{node.name}: {docstring}")
    return doc_lines

def check_type_annotations(tree: ast.AST) -> list[str]:
    missing = [
        node.name for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
        and (not node.returns or not all(arg.annotation for arg in node.args.args))
    ]
    return [
        "Functions without type annotations: " + ", ".join(missing)
        if missing else "All functions and methods have type annotations."
    ]

def check_naming_conventions(tree: ast.AST) -> list[str]:
    improper_classes = []
    improper_functions = []

    camel_case = re.compile(r'^[A-Z][a-zA-Z0-9]*$')
    snake_case = re.compile(r'^[a-z_][a-z0-9_]*$')

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and not camel_case.match(node.name):
            improper_classes.append(node.name)
        elif isinstance(node, ast.FunctionDef) and not snake_case.match(node.name):
            improper_functions.append(node.name)

    return [
        ("Classes not following CamelCase: " + ", ".join(improper_classes)) if improper_classes else "All classes follow CamelCase naming.",
        ("Functions not following snake_case: " + ", ".join(improper_functions)) if improper_functions else "All functions follow snake_case naming."
    ]

def write_report(report: list[str], file_name: str) -> None:
    output_name = f"style_report_{os.path.basename(file_name)}.txt"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    report_path = os.path.join(script_dir, output_name)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report))
    print(f"Report generated: {report_path}")

def add_parent_info(tree: ast.AST) -> ast.AST:
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            child.parent = node
    return tree

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    py_files = [f for f in os.listdir(script_dir) if f.endswith('.py') and f != os.path.basename(__file__)]

    print("Available Python files in this script's directory:")
    for i, fname in enumerate(py_files, 1):
        print(f"{i}. {fname}")

    choice = input("Select the file number to analyze: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(py_files)):
        print("Invalid selection.")
        return

    file_path = os.path.join(script_dir, py_files[int(choice) - 1])
    file_content = read_file(file_path)
    tree = parse_ast(file_content)
    tree = add_parent_info(tree)

    report = []
    report += analyze_file_structure(tree, file_content)
    report += extract_docstrings(tree)
    report += check_type_annotations(tree)
    report += check_naming_conventions(tree)

    write_report(report, file_path)

if __name__ == "__main__":
    main()