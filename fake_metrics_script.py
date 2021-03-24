#!/usr/bin/env python

import sys, os


def main(metric_names):
    output = ""
    for metric in metric_names:
        filename = f"{metric}.json"
        if os.path.exists(filename):
            with open(filename) as f:
                output += f.read()
    return output or "No metrics found."


if __name__ == "__main__":
    print(main(sys.argv[1:]))