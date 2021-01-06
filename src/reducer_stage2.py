#!/usr/bin/python3
""" reducer_stage2.py """
import sys


def read_input(filename: str) -> None:
    for line in filename:
        yield line.rstrip().split(',', 1)


def reducer() -> None:
    samples = read_input(sys.stdin)
    # Identity reducer => NOP
    for sample in samples:
        print('{}, {}'.format(sample[0], sample[1]))


if __name__ == '__main__':
    reducer()
