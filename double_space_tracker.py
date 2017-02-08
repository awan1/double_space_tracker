"""
This is a background application that will alert a user when they input two
spaces (instead of one) after a period.

It exhibits interesting functionality:
- Monitoring keyboard inputs on OSX
- Displaying OSX alerts

Algorithm: if a space is seen after a period and a space, output an alert.
That's it. Could do more subtle checking of context (e.g. don't want to alert
when writing code) but I can't think of any contexts where a double space is
actually desired.

Author: adrianwan2@gmail.com
"""
import os

from pynput.keyboard import Key, KeyCode, Listener


# The universal key to stop the tracking with.
# Must be one of the values of keyboard.Key
STOP_KEY = 'f8'


def notify_double_space():
    """
    Utility function to notify if a double space was pressed after a period.
    """
    os.system(
        """
        osascript -e 'display notification "Double space!" with title "KeyTracker"'
        """
    )


class LengthTwoQueue(object):
    """
    A queue that holds two objects.
    - first is the most recently inserted item
    - second is the second-most-recently inserted item
    """
    def __init__(self):
        self.first = None
        self.second = None

    def add(self, item):
        self.second = self.first
        self.first = item


class ListenerWithCache(Listener):
    """
    An extension of the Listener class that comes with a cache.
    """
    def __init__(self):
        self.cache = LengthTwoQueue()
        # Run the superclass __init__, passing in *instance methods*.
        # This gives the methods appropriate access to the cache.
        super(ListenerWithCache, self).__init__(
            on_press=self.on_press,
            on_release=self.on_release)

    def on_press(self, key):
        if (key == Key.space and
                self.cache.first == Key.space and
                self.cache.second == KeyCode.from_char('.')):
            notify_double_space()
        self.cache.add(key)

    def on_release(self, key):
        if key == getattr(Key, STOP_KEY):
            return False


if __name__ == '__main__':
    print("Starting to watch for double-spacing. Press {} outside "
          "of terminal windows to exit."
          "".format(STOP_KEY))
    with ListenerWithCache() as listener:
        try:
            listener.join()
        finally:
            print("Double-space tracker stopped.")

