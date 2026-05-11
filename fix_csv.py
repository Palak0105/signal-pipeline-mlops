input_file = "data.csv"
output_file = "clean_data.csv"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        # Remove surrounding quotes
        cleaned_line = line.strip().strip('"')

        # Write cleaned line
        outfile.write(cleaned_line + "\n")

print("CSV cleaned successfully!")