#!/usr/bin/python3
""" mapper_stage2.py """
import sys


def read_input(filename: str) -> None:
    for line in filename:
        yield line.rstrip().split(',', 1)


def mapper() -> None:
    samples = read_input(sys.stdin)
    for sample in samples:
        # Reverse the ratings and movieID order
        print('{}, {}'.format(sample[1], sample[0]))


if __name__ == '__main__':
    mapper()
