import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], alpha=0.6, label="Data")

    # Line of best fit for all data (through 2050)
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_all = pd.Series(range(1880, 2051))
    sea_level_all = res_all.slope * years_all + res_all.intercept
    plt.plot(years_all, sea_level_all, "r", label="Best fit: 1880–2050")

    # Line of best fit for data from year 2000 onward (through 2050)
    df_2000 = df[df["Year"] >= 2000]
    res_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    years_2000 = pd.Series(range(2000, 2051))
    sea_level_2000 = res_2000.slope * years_2000 + res_2000.intercept
    plt.plot(years_2000, sea_level_2000, "g", label="Best fit: 2000–2050")

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Set x-limits and ticks to match test expectations
    plt.xlim(1850, 2075)
    xticks = [1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075]
    plt.xticks(xticks)

    # Set y-limits with a small margin based on the data and projections
    ymin = min(df["CSIRO Adjusted Sea Level"].min(), sea_level_all.min(), sea_level_2000.min())
    ymax = max(df["CSIRO Adjusted Sea Level"].max(), sea_level_all.max(), sea_level_2000.max())
    margin = (ymax - ymin) * 0.05 if ymax > ymin else 1
    plt.ylim(ymin - margin, ymax + margin)

    plt.legend(loc="best")

    # Save plot and return the Axes object
    plt.savefig("sea_level_plot.png")
    return plt.gca()


if __name__ == "__main__":
    draw_plot()