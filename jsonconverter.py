import json

def convert_to_json(input_file, output_file):
    data = []

    with open(input_file, 'r') as f:
        # Skip the first 4 lines
        for _ in range(4):
            next(f)

        for line in f:
            line = line[4:].strip()  # Ignore first 4 characters
            columns = line.split()  # Split line into columns

            # Handle cases where there might not be enough columns
            if len(columns) >= 7:
                # Replace "#" with whitespace in Player name
                player_name = columns[0].replace("#", " ")

                # Assign values to JSON object
                entry = {
                    "Player": player_name,
                    "Kills": columns[1],
                    "Deaths": columns[2],
                    "K/D": columns[3],
                    "Credits": columns[4],
                    "Score": columns[5],
                    "Team": columns[6] if columns[6] in ["Nod", "GDI"] else ""
                }
                data.append(entry)

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

# Prompt user for filename
input_file = input("Enter the results file name: ")

# Use a default output file name or prompt for it if needed
output_file = "results.json"

# Convert to JSON
convert_to_json(input_file, output_file)

print(f"Conversion completed. JSON data saved to {output_file}.")
