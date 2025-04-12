# Open the input file for reading and the output file for writing
with open("File1.txt", "r") as file1, open("File2.txt", "w") as file2:
    for line in file1:
        parts = line.strip().split("\t")  # Split line using tab
        if len(parts) >= 2:  # Ensure there are at least two parts
            file2.write(parts[0] + "\n")  # Write first part with newline
            file2.write(parts[1] + "\n")  # Write second part with newline
