from load_csv import load
import matplotlib.pyplot as plt


def main():
    data = load("../ex00/life_expectancy_years.csv")
    # Find the row where the column 'Country' contains 'Switzerland'
    switzerland_data = data.loc[data['country'] == 'Switzerland']
    # Drop the 'country' column, leaving only the years (columns) and
    # life expectancy values
    years = switzerland_data.columns[1:].astype(int)  # Exclude 'country',
    # convert the remaining columns to int (years)
    life_expectancy = switzerland_data.values[0][1:]  # Extract life
    # expectancy values as an array, exclude the 'country'

    # Plotting the data
    plt.plot(years, life_expectancy, color='b',
             label="Life Expectancy in Switzerland")

    # Add titles and labels
    plt.title("Switzerland Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.show()

    return 0


if __name__ == "__main__":
    main()
