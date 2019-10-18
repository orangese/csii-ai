# Installing EasyAI

This is a three step process-- first, you must install Python. Next, `git`, which makes installing `easyai` a lot easier.
Finally, installing `easyai` using Python's package manager.

__Important__: if you have Python 2.7 installed, use this guide to install Python 3! If you don't know if you have Python 2.7,
disregard this message.

## 1. Installing Python

### Mac:

1. Go to https://www.python.org/ftp/python/3.7.5/python-3.7.5-macosx10.9.pkg
2. Double-click on the installed package and follow installation instructions. Select all default options and enter your 
password if prompted.
3. Go to Terminal and type `python --version` (then the Enter key) to verify installation. Python's current version
should show up. If that doesn't wok, try `python3 --version`.
4. Go to Applications in Finder and select Python. Double click on `Install Certificate.command` and then on `Update Shell Profile.command`.

### Linux:

1. Go to Terminal and type `sudo apt-get update` (then the Enter key). Enter password if prompted.
2. Type `sudo apt-get upgrade` (then the Enter key).
3. Type `sudo apt-get install python3` (then the Enter key).
4. Type and enter `sudo apt-get install python3-pip`.
4. Go to Terminal and type `python --version` to verify installation. Python's current version should show up. If that doesn't wok, try `python3 --version`.

### Windows:

1. Go to https://www.python.org/ftp/python/3.7.5/python-3.7.5-amd64.exe
2. Double-click on the installed package and follow installation instructions. 
__Important__: on the FIRST installation screen, select `Add Python 3.7 to PATH`. Otherwise, select all default options and 
enter your password if prompted. 
3. Go to Command Prompt and type `python --version` (then the Enter key) to verify installation. Python's current version
should show up. If that doesn't wok, try `python3 --version`.


## 2. Installing `git`

### Mac:

1. Go to https://sourceforge.net/projects/git-osx-installer/files/git-2.23.0-intel-universal-mavericks.dmg/download
2. Double click on downloaded package and follow installation instructions. If you're not allowed to install the package because of Mac security reasons, go to System Preferences > Security & Privacy > General and open the `git` package anyway. 
3. Verify using `git --version` in Terminal.

### Windows:

1. Go to https://git-scm.com/download/win
2. Double click on the downloaded package and follow instructions. 
__Important__: on the `Adjusting your PATH environment` installation screen, select Option 2 (`Use Git from the Windows Command Prompt`). Otherwise, select all default options and enter your password if prompted. 
3. Verify using `git --version` in Command Prompt.

### Linux:

1. Enter `sudo apt-get install git` in Terminal and press Enter.
2. Verify using `git --version` in Terminal.


## 3. Installing `easyai`

### Mac/Windows/Linux:

1. Go to Terminal (or Command Prompt for Windows) and paste
`pip3 install tensorflow`. If that doesn't work, replace `pip3` with `pip`.
2. Paste 
`pip3 install "git+https://github.com/orangese/easyai.git"`. If that doesn't work, replace `pip3` with `pip`.
