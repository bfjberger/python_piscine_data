from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def format_func(value, tick_number):
    """ Custom function to format the ticks as 'k' for thousands. """
    if value >= 1000:
        return f'{int(value / 1000)}k'  # Convert to 'k' format
    return int(value)


def main():
    # Load the data
    data_income = load("/Users/bb/42lausanne/machine_learnia/piscine_python/2/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    data_life = load("/Users/bb/42lausanne/machine_learnia/piscine_python/2/life_expectancy_years.csv")

    # Specify the year for analysis
    year = "1900"

    # Select the 'country' and the chosen year from both datasets
    income_year = data_income[['country', year]]
    life_year = data_life[['country', year]]

    # Merge the two datasets on 'country'
    combined_data_year = pd.merge(income_year, life_year, on='country', suffixes=('_income', '_life_expectancy'))

    # Rename the columns for clarity
    combined_data_year.columns = ['country', 'income', 'life_expectancy']

    # Convert the income and life expectancy values to numeric (handling errors like non-numeric values)
    combined_data_year['income'] = pd.to_numeric(combined_data_year['income'], errors='coerce')
    combined_data_year['life_expectancy'] = pd.to_numeric(combined_data_year['life_expectancy'], errors='coerce')

    # Drop any rows with missing or NaN values
    combined_data_year = combined_data_year.dropna()

    # Plotting income vs life expectancy with a log scale for the x-axis
    plt.scatter(combined_data_year['income'], combined_data_year['life_expectancy'], color='b')

    # Add titles and labels
    plt.title(f"{year}")
    plt.xlabel("Gross Domestic Product (Income)")
    plt.ylabel("Life Expectancy (Years)")

    # Set the x-axis to a logarithmic scale
    plt.xscale('log')
    # Use FuncFormatter to apply the custom tick formatting
    plt.gca().xaxis.set_major_formatter(FuncFormatter(format_func))

    # Show the plot
    plt.show()

    return 0


if __name__ == "__main__":
    main()
