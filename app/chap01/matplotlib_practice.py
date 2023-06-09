import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread

# set matplotlib style
plt.style.use(
    "ggplot"
)  # ref: https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html


def plot_sin_and_cos():
    # create data
    x = np.arange(0, 6, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)

    # plot
    plt.plot(x, y1, label="sin")
    plt.plot(x, y2, linestyle="--", label="cos")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("sin & cos")
    plt.legend()

    # save
    plt.savefig("output/chap01/sin_and_cos.png")

    # close (must)
    plt.close()


def plot_img():
    img = imread("data/chap01/lena.png")
    plt.imshow(img)
    plt.savefig("output/chap01/lena.png")
    plt.close()


def main():
    plot_sin_and_cos()
    plot_img()


main()
