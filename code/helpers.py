import pandas as pd

def import_data():
    """
    Import the csv files of the courses and rooms as dataframes.

        Return courses, rooms
    """
    courses_df = pd.read_csv('data/vakken.csv', sep=';')
    # Sort rooms on capacity and start with lowest capacity
    rooms_df = pd.read_csv('data/zalen.csv', sep=';').sort_values('Capaciteit')

    return courses_df, rooms_df