#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    options = ['rock', 'paper', 'scissors']
    outcomes = []

    def find_outcome(remaining, result=[]):
        if remaining == 0:
            outcomes.append(result)
            return
        for option in options:
            find_outcome(remaining - 1, result + [option])

    find_outcome(n, [])
    return outcomes


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
