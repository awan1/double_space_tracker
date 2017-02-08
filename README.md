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

## Debugging / manual runs
If the script fails because it's missing libraries, you can try to manually
fix it by installing the right libraries. Either add the missing libraries to
`pip_requirements.txt` and re-run `run.sh`, or start the virtualenv and run
the tracker manually:

    # Activate the virtualenv
    $ source double_space_venv/bin/activate

    # Install whatever packages are missing
    $ pip install ...

    # Run the tracker with superuser privileges, using the virtualenv python
    # (just using python will get the superuser version rather than the
    # virtualenv one)
    $ sudo double_space_venv/bin/python double_space_tracker.py

