file_path = "B2_Timeout180SResults.txt"
benchmark = "2"
timeout = "180"
output_file = "{}_timout{}.txt.format(benchmark, timeout)"

with open(file_path, "r") as file:
    lines = file.readlines()[1:]

with open(output_file, "w") as output:
    for line in lines:
        if "Error: Failed to execute query" in line:
            split_line= line.split("/")
            content = split_line[1]

            output.write(content + "\n")