import os
import shutil
import subprocess

def organize_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    for filename in os.listdir(source_folder):
        if filename.endswith('.txt'):
            shutil.move(os.path.join(source_folder, filename), os.path.join(destination_folder, filename))

def run_command(command):
    subprocess.run(command, shell=True)

def main():
    # Example usage of the automation functions
    source_folder = 'C:\\Users\\Saksham\\Documents\\Downloads'
    destination_folder = 'C:\\Users\\Saksham\\Documents\\Organized'
    
    organize_files(source_folder, destination_folder)
    
    # Run a system command as an example
    run_command('echo Automation tasks completed!')

if __name__ == '__main__':
    main()