import logging

import geopy.distance
import maidenhead
from numpy import math

from repeaters.config import QTHR
from repeaters.outputs import get_repeaters_csv_output_path
from repeaters.uk_repeaters import get_uk_repeaters_dataframe

log = logging.getLogger(__name__)




def main():
    my_location = maidenhead.to_location(QTHR)
    repeaters = get_uk_repeaters_dataframe()

    def distance_function(row):
        d = geopy.distance.distance(my_location, (row.lat, row.lon))
        return d.kilometers

    repeaters["distance"] = repeaters.apply(distance_function, axis=1)
    repeaters = repeaters.sort_values(by=["distance"])


    with get_repeaters_csv_output_path().open("w") as repeaters_file:
        repeaters.to_csv(repeaters_file, index=False, line_terminator="\n")


if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger("").setLevel(logging.INFO)
    main()
