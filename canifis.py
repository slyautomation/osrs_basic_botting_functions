from functions import random_breaks
from utils.common_functions import find_object_precise_new


def start_course():
    find_object_precise_new('green')
    random_breaks(5.01, 6.5)


def second_jump():
    find_object_precise_new('green')
    random_breaks(5.01, 6.5)


# click on the tree
if __name__ == "__main__":
    # start_course()
    second_jump()
