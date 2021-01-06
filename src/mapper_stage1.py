#!/usr/bin/python3
""" mapper.py """
import sys


def read_input(filename: str) -> None:
    for line in filename:
        row_data = line.split(',')
        yield (row_data[1], row_data[2])


def mapper() -> None:
    samples = read_input(sys.stdin)
    for sample in samples:
        try:
            if int(sample[0]):
                print('{}, {}'.format(sample[0], sample[1]))
        except ValueError:
            pass


if __name__ == '__main__':
    mapper()
