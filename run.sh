###############################################################################
# Script to run the double_space_tracker utility.
# Includes installation.
#
# Author: adrianwan2@gmail.com
###############################################################################

## Change to correct directory
cd $(dirname $0)

################
## Virtualenv ##
################

## If in a virtualenv, deactivate.
## (from http://stackoverflow.com/a/15454916/2452770)
INVENV=$(python -c 'import sys; print ("1" if hasattr(sys, "real_prefix") else "0")')
if [ ${INVENV} -eq 1 ]; then
  echo "Detected a virtualenv. Deactivating"
  deactivate
fi

# Start the virtualenv
VENV_DIR="double_space_venv"
if [ ! -d ${VENV_DIR} ] ; then
  echo "Creating virtualenv in ${VENV_DIR}"
  virtualenv ${VENV_DIR}
fi
echo "Activating virtualenv in ${VENV_DIR}"
source ${VENV_DIR}/bin/activate

# Install requirements
echo "Installing requirements"
pip install pynput

# Run
echo
echo "Starting double-space tracker. You might need to enter your password"
echo "This is to grant superuser privileges, needed to capture global keyboard entry"
sudo ${VENV_DIR}/bin/python double_space_tracker.py

# Deactivate the venv
echo
echo "Deactivating virtualenv"
deactivate
echo "Exiting"
