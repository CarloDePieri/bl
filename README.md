# bl

An utility to manage my bluetooth headsets and quickly fix them when they do not connect.
It's mainly a wrapper around the most used bluetoothctl commands.

## Installation

### With pip

Create a virtual environment if desired:

```bash
python3 -m venv .venv
. .venv/bin/activate
```

Install the application in the venv (or directly in the user space, with the `--user` flag):

```bash
pip install https://github.com/CarloDePieri/bl/archive/master.zip
```

### With git and Pipenv

Clone the repository:

```bash
git clone https://github.com/CarloDePieri/bl.git
cd bl
```

Prepare the virtual environment. Pipenv can do this like so:

```bash
pipenv --three
```

Prepend `PIPENV_VENV_IN_PROJECT=1`, if a local venv is preferred.

Install the dependencies with:

```bash
pipenv install
```

### With git and pip

Download the repo files as described above, prepare a venv if desired, then run:

```bash
pip install .
```

## Configuration

The tool will, when first run, prepare a stub config file at `~/.config/bl/config.ini`.
It's then necessary to populate this file with the desired device data. Here's an example:

```ini
[Default]
key = mydevice

[Name]
mydevice = My complete device name

[Address]
mydevice = 00:00:00:00:00:00
```

More than one device can be added, but remember to add them to both the `[Name]` and the `[Address]` sections.

## Run

Documentation about all flags and commands of the tool can be inspected by using `--help`:

```bash
bl --help  # For the main help
bl connect --help  # For the connect command help, as an example
```
