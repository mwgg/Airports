import json
import argparse

def sort_json_by_keyword(input_file, output_file, keyword):
    with open(input_file, 'r') as file:
        data = json.load(file)

    print(f"Found {len(data)} airport entries")

    sorted_keys = sorted(data.keys(), key=lambda k: data[k][keyword])
    sorted_data = {k: data[k] for k in sorted_keys}

    with open(output_file, 'w') as file:
        json.dump(sorted_data, file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sort JSON objects by a specified keyword.')
    parser.add_argument('input_file', help='Path to the input JSON file.')
    parser.add_argument('output_file', help='Path to the output JSON file.')
    parser.add_argument('keyword', help='Keyword to sort the JSON objects by.')

    args = parser.parse_args()

    sort_json_by_keyword(args.input_file, args.output_file, args.keyword)
