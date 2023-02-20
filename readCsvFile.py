import os
import csv

folder_path = "Benchmark2Separate" # Replace with the path to your folder

# Create a list to store all rows that meet the given conditions
all_rows_to_write = []

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a CSV file and includes the keyword '_TicketPolicy' in its filename
    if filename.endswith('.csv') and '_TicketPolicy' in filename:
        # Open the CSV file for reading
        with open(os.path.join(folder_path, filename), 'r') as csv_file:
            # Create a CSV reader object to read the CSV file
            reader = csv.reader(csv_file)
            # Create a list to store the rows that meet the given conditions
            rows_to_write = []
            # Create variables to store the maximum fourth column value and its corresponding row
            max_fourth_col_value = float('-inf')
            row_with_max_fourth_col_value = None
            # Loop through each row in the CSV file
            for row in reader:
                print(row)
                #row = row[0].split('\t')

                # Check if the third column value is less than 800
                if float(row[2]) < 1800:
                    # If so, add the row to the list of rows to write
                    rows_to_write.append(row)
                # Check if the third column value is greater than or equal to 1800
                #elif float(row[2]) >= 1800:
                    # If so, check if the fourth column value is larger than the current maximum fourth column value
                    #if float(row[3]) > max_fourth_col_value:
                        # If so, update the maximum fourth column value and its corresponding row
                        #max_fourth_col_value = float(row[3])
                        #row_with_max_fourth_col_value = row

            # Add the rows that meet the conditions to the list of all rows to write
            all_rows_to_write += rows_to_write
            #if row_with_max_fourth_col_value:
                # Add the row with the maximum fourth column value to the list of all rows to write
                #all_rows_to_write.append(row_with_max_fourth_col_value)

# Create the output file name
output_filename = 'all_sucussful_output_TicketPolicy_1800.csv'
output_path = os.path.join(folder_path, output_filename)

# Open the output file for writing
with open(output_path, 'w') as output_file:
    # Create a CSV writer object to write to the output file
    writer = csv.writer(output_file)
    # Write all rows that meet the conditions to the output file
    writer.writerows(all_rows_to_write)
