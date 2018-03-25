import argparse
from os import path
from matplotlib import pyplot as plt

def line_chart(src):
    x = []
    y_set = []

    with open(src, "r") as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            y_values = [float(v) for v in line.split(",")]
            x.append(len(x))
            y_set.append(y_values)

    # Transverse
    y_set = list(map(list, zip(*y_set)))            

    for y in y_set:
        plt.plot(x, y)

    plt.title(path.basename(src))
    plt.show()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="Source csv file path")
    args = parser.parse_args()

    line_chart(args.src)
