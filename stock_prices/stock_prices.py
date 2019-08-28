#!/usr/bin/python

import argparse


def find_max_profit(prices):
    minPrice = prices[0]
    maxProfit = prices[1] - minPrice

    for currentPrice in prices[1:]:
        maxProfit = max(currentPrice - minPrice, maxProfit)
        minPrice = min(currentPrice, minPrice)

    return maxProfit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
