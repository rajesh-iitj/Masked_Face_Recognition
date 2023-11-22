import os
import pandas as pd
import pdb

def remove_missing_files(csv_path, folder_path):
    # Read the CSV file
    df = pd.read_csv(csv_path)

    # Extract the 'path' column
    file_paths = df['path'].tolist()
    code_folder = 'Code'
    current_folder = os.getcwd()

    # Check if each file exists in the folder
    missing_files = []
    for file_path in file_paths:
        full_path = os.path.join(current_folder, code_folder, file_path)
        full_path = os.path.normpath(full_path)
        if not os.path.exists(full_path):
            print(full_path)
            missing_files.append(full_path)
            # Remove the entry from the DataFrame
            df = df[df['path'] != file_path]

    # Save the modified DataFrame back to the CSV file
    df.to_csv(csv_path, index=False)

    return missing_files

# Example usage
csv_path = './Data/train.csv'  # Replace with the actual path to your train.csv
folder_path = './Code/train'  # Replace with the actual path to your folder

missing_files = remove_missing_files(csv_path, folder_path)

if not missing_files:
    print("All files are present.")
else:
    print("Missing files:")
    for file in missing_files:
        print(file)
