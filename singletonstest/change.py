# changge.py

from singletonstest import source
source.FILENAME = "ThisIsChange.py"


def get_num():
    print("I am in change.py")
    print(__name__)

source.get_num = get_num