import numpy as np 
import matplotlib.pyplot as plt

def trigonometric():
    x = np.linspace(0, 2*np.pi, 1000)
    y1 = np.sin(x)
    plt.plot(x, y1, label="$sin(x)$")
    y2 = np.cos(x)
    plt.plot(x, y2, label="$cos(x)$")
    y3 = np.tan(x)
    plt.plot(x, y3, label="$tan(x)$")

    plt.xticks(np.linspace(0, 2*np.pi, 5), labels=("0", r"$\frac{1}{2}\pi$", r"$\pi$", r"$\frac{3}{2}\pi$", r"${2}\pi$"))
    plt.hlines(0, 0, 2*np.pi, linestyles="dashed", linewidth=0.5)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    trigonometric()
