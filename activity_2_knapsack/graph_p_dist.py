import numpy as np
import matplotlib.pyplot as plt
from random import randint
from scipy.optimize import curve_fit


def generate_index_opposite(length):
    _index = randint(0, length - 1)
    index = _index - randint(0, _index)
    return index


def exponential(x, a, b):
    return a * np.exp(-b * x)


n_trials = 100000
length = 100
indices = [generate_index_opposite(length) for _ in range(n_trials)]

scatter_color = "#96B5B4"
line_color = "#000000"

# Scatter Plot with Exponential Best-fit Line
counts, _ = np.histogram(indices, bins=np.arange(-0.5, length, 1))
probabilities = counts / n_trials
x = np.arange(length)
y = probabilities

params, _ = curve_fit(exponential, x, y, p0=[1, 0.1])
rounded_params = np.round(params, 2)
best_fit_line = exponential(x, *rounded_params)

plt.scatter(x, y, alpha=0.75, color=scatter_color)
plt.plot(x, best_fit_line, color=line_color, linestyle="--")
plt.title(
    f"Scatter Plot of Index Selection Probability\n(List Length {length:,}\n{n_trials:,} Trials)",
    fontname="Georgia",
    fontsize=14,
)
plt.xlabel("Index", fontname="Georgia", fontsize=14)
plt.ylabel("Probability", fontname="Georgia", fontsize=14)
plt.xticks(fontname="Georgia", fontsize=14)
plt.yticks(fontname="Georgia", fontsize=14)
plt.text(
    0.5 * length,
    max(y) * 0.6,
    f"Best-fit Exponential:\n y = {rounded_params[0]:.2f} * e^(-{rounded_params[1]:.2f} * x)",
    fontname="Georgia",
    fontsize=14,
    ha="left",
)
plt.subplots_adjust(top=0.8)
plt.savefig("probability_distribution_scatter_opposite.png", dpi=300)
plt.show()
