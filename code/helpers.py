import pandas as pd

def import_data(destination):
    """
    Import the csv files of the courses and rooms as dataframes.

        Return courses, rooms
    """
    df = pd.read_csv(f'data/{destination}.csv', sep=',')
    # Sort rooms on capacity and start with lowest capacity
    if destination == "zalen":
        df = df.sort_values(by='Max. capaciteit')

    return df


