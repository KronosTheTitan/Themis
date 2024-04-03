# Debug.py
# This class will be used to write messages to the console and to a more permanent file.
# By this approach it will be possible to ensure that no Error is lost in the case of a critical failure.

def Log(message):
    print(message)


def LogWarning(message):
    print("\033[93m {}\033[00m" .format(message))


def LogError(message):
    print("\033[91m {}\033[00m".format(message))
