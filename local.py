import subprocess
import pyautogui
import time
import os
import signal

with open("clone.txt", "r") as cloner:
    clone = cloner.read().strip()

with open("clone.txt", "r") as debugger:
    debug = debugger.read().strip()

def against_clone():

    # Continuously monitor the output
    while True:
        output = process.stdout.readline().strip()
        if output:
            if debug == "0":
                print(output)

        if "you like to clone the fork" in output:
                process.send_signal(signal.SIGINT)  # Terminsate the process
                break
    
    # Wait for the process to finish
    stdout, stderr = process.communicate()
    
    # Print the captured output
    print("Standard Output:")
    print(stdout.decode())
    print("Standard Error:")
    print(stderr.decode())

def for_clone():
    # Continuously monitor the output
    while True:
        output = process.stdout.readline().strip()
        if output:
            if debug == "0":
                print(output)

        if "you like to clone the fork" in output:
            process.stdin.write("Y\n")
            process.stdin.flush()
        elif "Cloned fork" in output:
            cloned_fork = True
        if cloned_fork and "Cloning into" in output:
            process.send_signal(signal.SIGINT)  # Terminate the process
            break

    # Wait for the process to finish
    stdout, stderr = process.communicate()
    
    # Print the captured output
    print("Standard Output:")
    print(stdout.decode())
    print("Standard Error:")
    print(stderr.decode())


def fork_repository_with_org(repo_url, name_file, file_path):
    fork_command = f"gh repo fork {repo_url} --org {name_file}"
    
    # Run the command in a subprocess
    process = subprocess.Popen(fork_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    
    if clone == "0":
        for_clone()
    else:
        against_clone()


    print(f"You just forked {repo_url} from {file_path} into organization {name_file}! :)")

def fork_repository_without_org(repo_url, file_path):
    fork_command = f"gh repo fork {repo_url}"
    
    # Run the command in a subprocess
    process = subprocess.Popen(fork_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    if clone == "0":
        for_clone()
    else:
        against_clone()

    print(f"You just forked {repo_url} from {file_path}! :)")

def check_if_folder_ignored(folder_name):
    # Function to check if folder should be ignored
    with open("folder-ignore.txt", "r") as folder_ignore_file:
        ignored_folders = folder_ignore_file.read().splitlines()
        return folder_name in ignored_folders

def check_if_file_ignored(file_name):
    # Function to check if file should be ignored
    with open("file-ignore.txt", "r") as file_ignore_file:
        ignored_files = file_ignore_file.read().splitlines()
        return file_name in ignored_files

def main():
    # Get the current directory
    current_directory = os.getcwd()

    # Iterate over all folders in the current directory
    for folder_name in os.listdir(current_directory):
        folder_path = os.path.join(current_directory, folder_name)

        # Check if the current item is a folder and not ignored
        if os.path.isdir(folder_path) and not check_if_folder_ignored(folder_name):
            # Iterate over all files in the current folder
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, name_file, file_name)

                base_name = os.path.basename(file_name)  # Get the base name (including extension)
                name_file, _ = os.path.splitext(base_name)  # Split the base name into name and extension

                if name_file.startswith("org--"):
                    name_file = name_file[len("org--"):]

                    # Check if the current item is a file and not ignored
                    if os.path.isfile(file_path) and not check_if_file_ignored(file_name):
                        with open(file_path, "r") as org_file:
                            org_lines = org_file.readlines()
                            for line in org_lines:
                                repo_url = line.strip()
                                fork_repository_with_org(repo_url, name_file, file_path)

                else:
                     # Check if the current item is a file and not ignored
                    if os.path.isfile(file_path) and not check_if_file_ignored(file_name):
                        with open(file_path, "r") as org_file:
                            org_lines = org_file.readlines()
                            for line in org_lines:
                                repo_url = line.strip()
                                fork_repository_without_org(repo_url, file_path)

if __name__ == "__main__":
    main()


