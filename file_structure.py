
import os

# Define the directory structure
directory_structure = {
    'data': ['raw', 'processed', 'analytics'],
    'streaming': ['kafka'],
}

# Define the file names
file_names = {
    'data/raw': ['dataset1.csv', 'dataset2.csv'],
}

# Define the function to create directories and files
def create_directory_structure():
    for directory in directory_structure:
        os.makedirs(directory, exist_ok=True)
        for subdirectory in directory_structure[directory]:
            os.makedirs(os.path.join(directory, subdirectory), exist_ok=True)
            for file_name in file_names.get(os.path.join(directory, subdirectory), []):
                with open(os.path.join(directory, subdirectory, file_name), 'w') as f:
                    pass
                
# Call the function to create the directories and files
create_directory_structure()
