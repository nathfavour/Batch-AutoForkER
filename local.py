import subprocess
import pyautogui
import time
import os
import signal

with open("clone.txt", "r") as cloner:
    clone = cloner.read().strip()

with open("clone.txt", "r") as debugger:
    debug = debugger.read().strip()

with open("pre.txt", "r") as pree:
    pre = pree.read().strip()

def fork_repository_with_org(repo_url, file_path, name_file):
    if clone == "0":
        fork_command = f"gh repo fork {repo_url} --org {name_file}"
        
        # Run the command in a subprocess
        process = subprocess.Popen(fork_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        
        start_time = time.time()
        elapsed_time = 0
        cloned_fork = False

        # Continuously monitor the output
        while True:
            output = process.stdout.readline().strip()
            if output:
                if debug == "0":
                    print(output)

            ask = "you like to clone the fork"
            bytes_ask = ask.encode("utf-8")

            bsk = "Cloned fork"
            cytes_ask = bsk.encode("utf-8")

            csk = "Cloning into"
            dytes_ask = bsk.encode("utf-8")

            if bytes_ask in output:
                process.stdin.write("Y\n".encode("utf-8"))
                process.stdin.flush()
            elif cytes_ask in output:
                cloned_fork = True
            if cloned_fork and dytes_ask in output:
                process.send_signal(signal.SIGINT)  # Terminate the process
                break

            elapsed_time = time.time() - start_time
            if elapsed_time >= 5:
                process.send_signal(signal.SIGINT)  # Terminate the process
                print("Timeout: No string detected in the output within 5 seconds.")
                break

        # Wait for the process to finish
        stdout, stderr = process.communicate()
        
        # Print the captured output
        print("Standard Output:")
        print(stdout.decode())
        print("Standard Error:")
        print(stderr.decode())
    else:
        fork_command = f"gh repo fork {repo_url} --org {name_file}"
    
        # Run the command in a subprocess
        process = subprocess.Popen(fork_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        
        start_time = time.time()
        elapsed_time = 0

        # Continuously monitor the output
        while True:
            output = process.stdout.readline().strip()
            if output:
                if debug == "0":
                    print(output)

            ask = "you like to clone the fork"
            bytes_ask = ask.encode("utf-8")
            if bytes_ask in output:
                process.send_signal(signal.SIGINT)  # Terminate the process
                break

            elapsed_time = time.time() - start_time
            if elapsed_time >= 5:
                process.send_signal(signal.SIGINT)  # Terminate the process
                print("Timeout: No string detected in the output within 5 seconds.")
                break

        # Wait for the process to finish
        stdout, stderr = process.communicate()
        
        # Print the captured output
        print("Standard Output:")
        print(stdout.decode())
        print("Standard Error:")
        print(stderr.decode())
        print(f"You just forked {repo_url} from {file_path} into organization {name_file}! :)")

def fork_repository_without_org(repo_url, file_path):
    fork_command = f"gh repo fork {repo_url}"
    
    # Run the command in a subprocess
    process = subprocess.Popen(fork_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    if clone == "0":
        fork_command = f"gh repo fork {repo_url} --org"
            
        # Run the command in a subprocess
        process = subprocess.Popen(fork_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        
        start_time = time.time()
        elapsed_time = 0
        cloned_fork = False

        # Continuously monitor the output
        while True:
            output = process.stdout.readline().strip()
            if output:
                if debug == "0":
                    print(output)

            ask = "you like to clone the fork"
            bytes_ask = ask.encode("utf-8")

            bsk = "Cloned fork"
            cytes_ask = bsk.encode("utf-8")

            csk = "Cloning into"
            dytes_ask = bsk.encode("utf-8")

            if bytes_ask in output:
                process.stdin.write("Y\n".encode("utf-8"))
                process.stdin.flush()
            elif cytes_ask in output:
                cloned_fork = True
            if cloned_fork and dytes_ask in output:
                process.send_signal(signal.SIGINT)  # Terminate the process
                break

            elapsed_time = time.time() - start_time
            if elapsed_time >= 5:
                process.send_signal(signal.SIGINT)  # Terminate the process
                print("Timeout: No string detected in the output within 5 seconds.")
                break

        # Wait for the process to finish
        stdout, stderr = process.communicate()
        
        # Print the captured output
        print("Standard Output:")
        print(stdout.decode())
        print("Standard Error:")
        print(stderr.decode())
    else:
        fork_command = f"gh repo fork {repo_url}"
    
        # Run the command in a subprocess
        process = subprocess.Popen(fork_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        
        start_time = time.time()
        elapsed_time = 0

        # Continuously monitor the output
        while True:
            output = process.stdout.readline().strip()
            if output:
                if debug == "0":
                    print(output)

            ask = "you like to clone the fork"
            bytes_ask = ask.encode("utf-8")
            if bytes_ask in output:
                process.send_signal(signal.SIGINT)  # Terminate the process
                break

            elapsed_time = time.time() - start_time
            if elapsed_time >= 5:
                process.send_signal(signal.SIGINT)  # Terminate the process
                print("Timeout: No string detected in the output within 5 seconds.")
                break

        # Wait for the process to finish
        stdout, stderr = process.communicate()
        
        # Print the captured output
        print("Standard Output:")
        print(stdout.decode())
        print("Standard Error:")
        print(stderr.decode())
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

    for folder_name in os.listdir(current_directory):
        folder_path = os.path.join(current_directory, folder_name)

        # Check if the current item is a folder and not ignored
        if os.path.isdir(folder_path) and not check_if_folder_ignored(folder_name) and folder_name == "list":
            print(f"Now working in {folder_name}")

            # Iterate over all files in the current folder
            for file_name in os.listdir(folder_path):
                base_name = os.path.basename(file_name)  # Get the base name (including extension)
                name_file, _ = os.path.splitext(base_name)  # Split the base name into name and extension

                file_path = os.path.join(current_directory, folder_path, file_name)

                if os.path.isfile(file_path):
                    if name_file.startswith(pre):
                        name_file = name_file[len(pre):]
                        print(f"We confirmed that {base_name} is an organizational repo fork file")

                        # Check if the current item is a file and not ignored
                        if not check_if_file_ignored(file_name):
                            with open(file_path, "r") as org_file:
                                org_lines = org_file.readlines()
                                for line in org_lines:
                                    repo_url = line.strip()
                                    fork_repository_with_org(repo_url, file_path, name_file)

                        else:
                            print(f"either {file_path} is not a file, or it is in 'file-ignore.txt'")

                    else:
                        print(f"We confirmed that {base_name} is a personal repo fork file")
                         # Check if the current item is a file and not ignored
                        if not check_if_file_ignored(file_name):
                            with open(file_path, "r") as org_file:
                                org_lines = org_file.readlines()
                                for line in org_lines:
                                    repo_url = line.strip()
                                    fork_repository_without_org(repo_url, file_path)
                        else:
                            print(f"either {file_path} is not a file, or it is in 'file-ignore.txt'")

        else:
            pass


if __name__ == "__main__":
    main()
