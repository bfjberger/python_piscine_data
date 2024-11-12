from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker

def main():
    # Load the CSV data
    data = load("../population_total.csv")

    # Debug: print first few rows of the data to inspect
    print(data.head())  # Print the first few rows to check the data format

    # Filter rows for Switzerland and France
    switzerland_data = data.loc[data['country'] == 'Switzerland']
    france_data = data.loc[data['country'] == 'France']

    # Debug: print the filtered data for Switzerland and France to check
    print("Switzerland Data:", switzerland_data)
    print("France Data:", france_data)

    # Extract years (excluding 'country' column)
    years = switzerland_data.columns[1:].astype(int)  # Convert the year columns to int
    print("Years:", years)  # Debugging: print years to make sure they are correct

    # Function to clean and convert population data from '78M' to numeric values
    def clean_population(pop_data):
        # Remove the 'M' and convert to numeric, multiplying by 1e6 for millions
        return pd.to_numeric(pop_data.str.replace('M', '').astype(float) * 1e6, errors='coerce')

    # Extract and clean population data for Switzerland and France
    switzerland_pop = clean_population(switzerland_data.iloc[0, 1:])
    france_pop = clean_population(france_data.iloc[0, 1:])

    # Debug: print the cleaned population data
    print("Switzerland Population Data:", switzerland_pop)
    print("France Population Data:", france_pop)

    # Check if there are any NaN values in population data (should not be)
    if switzerland_pop.isna().any() or france_pop.isna().any():
        print("Warning: NaN values found in population data!")

    # Plotting the data
    plt.plot(years, switzerland_pop / 1e6, color='b', label="Switzerland Population")  # Dividing by 1e6 to keep M units
    plt.plot(years, france_pop / 1e6, color='g', label="France Population")  # Dividing by 1e6 to keep M units

    # Add titles and labels
    plt.title("Population Comparison: Switzerland vs France")
    plt.xlabel("Year")
    plt.ylabel("Population (in millions)")

    # Format the y-axis ticks to show population in millions with "M"
    def millions(x, pos):
        'The two args are the value and tick position'
        return f'{x:.1f}M'  # Format as millions with 'M' at the end

    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(millions))

    # Show the legend
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()