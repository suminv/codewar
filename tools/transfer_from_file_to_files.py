import re


def extract_functions(file_content):
    """
    Extracts functions from the file content using regular expressions.
    Writes each function to a separate file with the same format as in the original file.
    """
    function_pattern = r"(def\s+\w+\(.*?\):(?:\s+\"{3}[\s\S]*?\"{3})?[\s\S]*?)(?=def|\Z)"
    matches = re.findall(function_pattern, file_content, re.MULTILINE | re.DOTALL)

    for match in matches:
        function_code = match.strip()
        function_name = re.search(r"def\s+(\w+)\(", function_code).group(1)
        function_filename = f"{function_name}_func.py"
        with open(function_filename, 'w') as function_file:
            function_file.write(function_code)

    print(f"Separate files for {len(matches)} functions have been created.")


# Usage example
original_file = "codewar_1.py"
with open(original_file, 'r') as file:
    file_content = file.read()

extract_functions(file_content)
