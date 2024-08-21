import json
import argparse
import sys

def check_json_validity(file_path):
    try:
        with open(file_path, 'r') as file:
            json.load(file)
        return True, ""
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {e}"
    except Exception as e:
        return False, f"An unexpected error occurred: {e}"

def main():
    parser = argparse.ArgumentParser(description="Check if a JSON file is valid.")
    parser.add_argument("file", help="The path to the JSON file to check.")
    
    args = parser.parse_args()
    file_path = args.file
    
    is_valid, message = check_json_validity(file_path)
    
    if is_valid:
        print(f"The JSON file '{file_path}' is valid.")
        sys.exit(0)
    else:
        print(f"The JSON file '{file_path}' is invalid. Error: {message}")
        sys.exit(1)

if __name__ == "__main__":
    main()
