import os

# set the path to the folder containing the files
folder_path = 'Benchmark2Separate'

# iterate over each file in the folder
for file_name in os.listdir(folder_path):
    # check if the file is a text file
    if file_name.endswith('.rq'):
        # create the full file path
        file_path = os.path.join(folder_path, file_name)
        # open the file and read its contents
        with open(file_path, 'r') as f:
            lines = f.readlines()
        # remove the first line
        lines = lines[1:]
        # write the modified contents back to the file
        with open(file_path, 'w') as f:
            f.writelines(lines)