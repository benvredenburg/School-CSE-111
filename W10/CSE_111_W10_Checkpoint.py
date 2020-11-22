import matplotlib.pyplot as plt
import pandas as pd

def main():
    try:
        print()
        df = pd.read_csv('W09water.csv', 
                dtype={"meterNumber":"str", "meterSize":"float32",
                    "readDate":"str", "numberOfDays":"int_", "usage":"int_",
                    "accountType":"str", "numberOfDwellings":"int_"
                }, 
                parse_dates=['readDate'])

        df['readDate'] = df['readDate'].dt.date
        
        meter = input('Please enter a meter number: ').capitalize()
        df = filter_for_meter(df, meter)

        # Define a vertical bar plot from the DataFrame.
        barplot = df.plot.bar(x='readDate', y='usage', legend=False)
        barplot.set_title(f"Water Usage for Meter #{meter}")
        barplot.set_xlabel("")
        barplot.set_ylabel("x1000 gallons")
        plt.tight_layout()

        # Draw and show all defined plots.
        plt.show()

    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")


def filter_for_meter(df, meter):
    """Return a new DataFrame that contains only the rows
    where the meterNumber equals the parameter meter.
    """
    meter_filter = (df['meterNumber'] == meter)
    meter_filtered = df[meter_filter]
    df = meter_filtered
    return df





main()