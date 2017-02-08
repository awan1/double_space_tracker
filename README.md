# Double Space Tracker
This is a Python utility that monitors keyboard inputs on OSX, generating an
alert when two spaces are typed after a period.

It requires superuser privileges to run; permission will be given after
running the shell script (which can be run with regular permissions).

It is a useful example for:

* Monitoring keystrokes on OSX
* Producing alerts in OSX

Tested on macOS Sierra v10.12.3

## Usage
Ensure pip is up to date:

    $ pip install --upgrade pip

Then, to start the utility:

    $ ./run.sh

This will:

* Deactivate any currently running virtualenvs
* Start a virtualenv for this utility, creating it if it does not exist
* Start the tracker, prompting the user for superuser authorization
* Run in the background
* Exit on a keystroke

## Trustworthiness
Anything that logs keystrokes deserves scrutiny. Users are encouraged to
inspect the source code, which is as minimal as possible.

