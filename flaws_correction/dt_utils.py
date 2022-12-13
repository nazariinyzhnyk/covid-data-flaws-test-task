import datetime
from typing import List


def parse_date(date: str) -> List[int]:
    return [int(x) for x in date.split("-")]


def get_date_sequence(start_date: str, end_date: str, out_template: str = "%m-%d-%Y") -> List[str]:
    # TODO:: develop unit tests for functions

    dt = datetime.datetime(*parse_date(start_date))
    end = datetime.datetime(*parse_date(end_date))
    step = datetime.timedelta(days=1)

    result = []
    while dt < end:
        result.append(dt.strftime(out_template))
        dt += step

    return result
