import json
import argparse
import sys

def check_json_validity(file_path):
    errors = []
    keys_seen = set()
    iata_seen = set()

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        print(f"Found {len(data)} airport entries")

        for key, value in data.items():
            if key in keys_seen:
                errors.append(f'Duplicate key found: "{key}".')
            else:
                keys_seen.add(key)

            if "icao" not in value:
                errors.append(f'Missing "icao" field in entry "{key}".')
            else:
                if not isinstance(value["icao"], str):
                    errors.append(f'Invalid type for "icao" in entry "{key}". Expected str, got {type(value["icao"]).__name__}.')
                else:
                    if value["icao"] != key:
                        errors.append(f'Key "{key}" does not match its "icao" field value "{value["icao"]}".')
                    if len(value["icao"]) != 4:
                        errors.append(f'Invalid "icao" length in entry "{key}". Expected 4, got {len(value["icao"])}.')

            if "iata" not in value:
                errors.append(f'Missing "iata" field in entry "{key}".')
            else:
                if not isinstance(value["iata"], str):
                    errors.append(f'Invalid type for "iata" in entry "{key}". Expected str, got {type(value["iata"]).__name__}.')
                else:
                    if len(value["iata"]) != 0 and len(value["iata"]) != 3:
                        errors.append(f'Invalid "iata" length in entry "{key}". Expected 0 or 3, got {len(value["iata"])}.')
                    if value["iata"] in iata_seen:
                        errors.append(f'Duplicate "iata" value found: "{value["iata"]}" in entry "{key}".')
                    elif len(value["iata"]) > 0:
                        iata_seen.add(value["iata"])

            if "name" not in value:
                errors.append(f'Missing "name" field in entry "{key}".')
            else:
                if not isinstance(value["name"], str):
                    errors.append(f'Invalid type for "name" in entry "{key}". Expected str, got {type(value["name"]).__name__}.')

            if "city" not in value:
                errors.append(f'Missing "city" field in entry "{key}".')
            else:
                if not isinstance(value["city"], str):
                    errors.append(f'Invalid type for "city" in entry "{key}". Expected str, got {type(value["city"]).__name__}.')

            if "state" not in value:
                errors.append(f'Missing "state" field in entry "{key}".')
            else:
                if not isinstance(value["state"], str):
                    errors.append(f'Invalid type for "state" in entry "{key}". Expected str, got {type(value["state"]).__name__}.')

            if "country" not in value:
                errors.append(f'Missing "country" field in entry "{key}".')
            else:
                if not isinstance(value["country"], str):
                    errors.append(f'Invalid type for "country" in entry "{key}". Expected str, got {type(value["country"]).__name__}.')
                else:
                    if len(value["country"]) != 2:
                        errors.append(f'Invalid "country" length in entry "{key}". Expected 2, got {len(value["country"])}.')

            if "elevation" not in value:
                errors.append(f'Missing "elevation" field in entry "{key}".')
            else:
                if not isinstance(value["elevation"], int):
                    errors.append(f'Invalid type for "elevation" in entry "{key}". Expected int, got {type(value["elevation"]).__name__}.')

            if "lat" not in value:
                errors.append(f'Missing "lat" field in entry "{key}".')
            else:
                if not isinstance(value["lat"], (float, int)):
                    errors.append(f'Invalid type for "lat" in entry "{key}". Expected float or int, got {type(value["lat"]).__name__}.')
                else:
                    if not -90 <= value["lat"] <= 90:
                        errors.append(f'Invalid value for "lat" in entry "{key}". Expected between -90 and 90, got {value["lat"]}.')

            if "lon" not in value:
                errors.append(f'Missing "lon" field in entry "{key}".')
            else:
                if not isinstance(value["lon"], (float, int)):
                    errors.append(f'Invalid type for "lon" in entry "{key}". Expected float or int, got {type(value["lon"]).__name__}.')
                else:
                    if not -180 <= value["lon"] <= 180:
                        errors.append(f'Invalid value for "lon" in entry "{key}". Expected between -180 and 180, got {value["lon"]}.')

            if "tz" not in value:
                errors.append(f'Missing "tz" field in entry "{key}".')
            else:
                if not isinstance(value["tz"], str):
                    errors.append(f'Invalid type for "tz" in entry "{key}". Expected str, got {type(value["tz"]).__name__}.')

        return errors

    except json.JSONDecodeError as e:
        errors.append(f"Invalid JSON: {e}")
    except Exception as e:
        errors.append(f"An unexpected error occurred: {e}")

    return errors

def main():
    parser = argparse.ArgumentParser(description="Check if a JSON file is valid and meets specific criteria.")
    parser.add_argument("file", help="The path to the JSON file to validate.")
    args = parser.parse_args()

    errors = check_json_validity(args.file)

    if errors:
        print(f'{len(errors)} validation errors found:')
        for error in errors:
            print(error)
        sys.exit(1)
    else:
        print("The JSON file is valid.")

if __name__ == "__main__":
    main()