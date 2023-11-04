from functions import random_breaks
from utils.common_functions import find_object_precise_new


def start_course():
    find_object_precise_new('agility')
    random_breaks(5.02, 6.25)


def first_jump():
    find_object_precise_new('agility', 'canifis-first-jump')
    random_breaks(5.12, 6.65)


def second_jump():
    find_object_precise_new('agility', 'canifis-second-jump')
    random_breaks(5.01, 6.5)


def third_jump():
    find_object_precise_new('agility', 'canifis-third-jump')
    random_breaks(5.8, 6.5)


def fourth_jump():
    find_object_precise_new('agility', 'canifis-fourth-jump')
    random_breaks(5.19, 6.45)


def fifth_jump():
    find_object_precise_new('agility', 'canifis-fifth-jump')
    random_breaks(5.21, 7.15)


def sixth_jump():
    find_object_precise_new('amber','canifis-sixth-jump')
    random_breaks(5.19, 6.45)


# click on the tree
if __name__ == "__main__":
    # start_course()
    # first_jump()
    # second_jump()
    # third_jump()
    # fourth_jump()
    # fifth_jump()
    sixth_jump()
