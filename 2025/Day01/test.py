import unittest

from day01 import parse

def test_parse():
    x: list[str] = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']
    for item in x:
        direction,  rotation = parse(item)
        if direction == 'L':
            print("left|")
        elif direction == 'R':
            print("right|")
        else:
            print("oops|")
