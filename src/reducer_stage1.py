#!/usr/bin/python3
""" reducer.py """
import sys
import csv
from collections import defaultdict


def read_input(filename: str) -> None:
    for line in filename:
        yield line.rstrip().split(',', 1)


def reducer() -> None:
    sample_aggr = defaultdict(list)
    samples = read_input(sys.stdin)
    for sample in samples:
        if sample_aggr.get(sample[0], None) is not None:
            running_avg = round(
                float(float(sample_aggr[str(sample[0])]) + float(sample[1])),
                2) / 2.00
            sample_aggr[str(sample[0])] = round(running_avg, 2)
        else:
            sample_aggr[str(sample[0])] = sample[1]

    for movie, rating in sample_aggr.items():
        print('{}, {}'.format(movie, rating))


if __name__ == '__main__':
    reducer()
