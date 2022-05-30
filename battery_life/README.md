# Battery checker
This module is intended to check the battery of the laptop and notify if the
battery percentage is out from the boundaries.

The default boundaries have been set from 20% to 80%, because is the
recommended percentage for most of the batteries.

The script has been tested under:
- python >= 3.8
- Ubuntu (Pop!OS) 22.04
- GNOME Shell 3.36.7
## Instructions

### Get the application
Clone the package (`git clone ...`).

### Run the application
Follow these steps for running the application from a virtual environment:
```shell
python3 -m venv checker-env
source checker-env/bin/activate
build-essential libdbus-glib-1-dev libgirepository1.0-dev
pip3 install -r requirements.txt
python3 battery_checker.py &
```
Store somewhere (write it, for example) the PID of the process.

### Stop the application
Stop it with the stored PID:
```shell
kill <pid>
```

## ToDos
- Once the laptop has been plugged/unplugged, accordingly to the
  instructions, the notification should disappear.
- Store the pid of the process to be able of killing it.
- Build the instructions to set up the process at start up.
- Build an interface able to stop the process and change the boundaries.
- Implement a sound notification.
