# Caffeinated ☕

Caffeinated [_caffeinated-screen-sleep-preventer_] is a simple Python script designed to prevent your computer screen from locking by simulating periodic keypresses. It uses the `pyautogui` library to automate the keypresses (F15 by default).

Useful for when you need to temporaily prevent a screen from turning off, when eg. cooking, playing guitar etc! 

## Features

- Prevents screen locking by simulating keypresses.
- Randomised intervals between keypresses to mimic natural usage.
- Easy to configure with adjustable time intervals and specific keys.

## Dependencies

- Python 3.x
- `pyautogui`

## Usage

To use the script, simply run it from your command line:

`python caffeinated.py`

Recommended usage is to add an alias in your terminal settings (eg. `.bash_profile`) as a shortcut: `alias caffeinated="python path/caffeinated.py"`

You can customize the time between presses and the specific key to press by modifying the parameters inline. 

## Installation

Before running the script, you need to ensure you have Python installed on your system and the necessary Python package:

```
pip install -r requirements.txt
```
