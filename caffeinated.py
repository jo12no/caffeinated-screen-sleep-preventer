"""Simulate keypress to prevent screen from locking.
"""
import random
import time

import pyautogui


def caffeinated(time_between_presses, button_to_press):
    """
    Entrypoint: simulate keypress to prevent screen from locking.

    :param time_between_presses: Base time in seconds between key presses.
    :param button_to_press: Button press to simulate.
    """
    print("Caffeinated! CTRL+C to exit...")

    try:
        while True:
            random_time = random.randint(
                (time_between_presses - 10), (time_between_presses + 10)
            )
            pyautogui.press(button_to_press)  # Simulate button press
            print(f"Pressed {button_to_press}.")
            print(f"Sleeping for: {random_time} seconds.")
            time.sleep(random_time) 
    except KeyboardInterrupt:
        print("Program exited.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    caffeinated(time_between_presses=120, button_to_press="f15")
