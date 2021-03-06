from typing import List

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


def doubles_counter(input: List) -> int:
    """
    Count all double timeslots in students activities.
    Return number of doubles.
    """
    doubles = {i: input.count(i) for i in input}
    N_doubles = 0
    for i in doubles.values():
        N_doubles += i - 1

    return N_doubles
