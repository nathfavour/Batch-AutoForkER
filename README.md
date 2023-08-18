	DESCRIPTION

Batch-AutoForkER is a code library for forking repositories. It forks repos from a list of repositories, depending on the name of the file.
There is a default "list" folder in this code, but it is also capable of forking lists from files within any folder in the same directory as the "local.py" main script.


	REQUIREMENTS

1. Have git cli installed
NB: You can run "brew install git" in MacOs or "sudo apt get git" in Linux
	You will also have to set git up by initialising it, connecting a remote repo, etc

2. Have github cli (gh) installed
NB: You can run "brew install gh" in MacOs or "sudo apt get gh" in Linux
	You will also have to set gh up by running "gh auth login" and following the command-line instructions as suitable.


		USAGE


1. Add your files containing the list of repos to fork in the "list" directory.
	Note that you can name these files anything you like.
	However, if you want to fork the repo into an organization of which you are a member and have fork(ing) rights, the file names must start with the string you specified in the "pre.txt". The default string specified in the "pre.txt" is "org--". So your file containing the list of repos you want to fork must have such prefix, e.g "org--myorganizationname.txt", "org--bAInaryglobe.txt", etc


	The files must contain the complete urls to the repos, and not just their name. For example, the repo list could look something like this:

	https://github.com/xxxx/yyyy
	https://github.com/aaaaa/bbbbb
	https://github.com/eeeee/fffff

2. First run:

(Windows)

		pip install -r requirements.txt

(MacOs/Linux)

		python3 -m pip install -r requirements.txt


3. Next run:

(Windows)

		python local.py

(MacOs/Linux)

		python3 local.py

4. Report any errors to nathfavour@bainaryglobe.com



