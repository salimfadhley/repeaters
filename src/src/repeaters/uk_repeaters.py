import csv
import dataclasses
from typing import Iterator

import pandas
import requests

UK_VOICE_REPEATERS = "https://ukrepeater.net/csvcreate1.php"


@dataclasses.dataclass(frozen=True)
class Repeater:
    repeater: str
    band: str
    channel: str
    tx: float
    rx: float
    mode: str
    qthr: str
    where: str
    region: str
    code: float
    keeper: str
    lat: float
    lon: float

    @classmethod
    def from_row(cls, row):
        field_names = {f.name for f in dataclasses.fields(cls)}
        reformatted_row = {k.lower(): v for (k, v) in row.iteritems() if k}
        return cls(**{k: v for k, v in reformatted_row.items() if k in field_names})


def get_uk_repeaters() -> Iterator[Repeater]:
    r = get_uk_repeaters_dataframe()
    for _, row in r.iterrows():
        yield Repeater.from_row(row)


def get_uk_repeaters_dataframe():
    r: pandas.DataFrame = pandas.read_csv(UK_VOICE_REPEATERS)

    return r.drop(columns=["Unnamed: 13"], axis=1)


if __name__ == "__main__":
    for r in get_uk_repeaters():
        print(r)
