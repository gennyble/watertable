from datetime import datetime
from typing import Iterator, List, Tuple

def clean_and_process(stamp: str, value: str, code: str):
    try:
        if int(code) < 0:
            return False
    except ValueError:
        return False
    if stamp[5:10] == "02-29": # janky hack, mate!
        return False # 😭
    depth = float(value)
    if depth > 11:
        return False
    date = datetime.fromisoformat(stamp + '-07:00')
    return (
        date,
        -depth
    )

def year_splitter(days: Iterator[Tuple[datetime, float]]) -> List[List[Tuple[datetime, float]]]:
    current_year = datetime.today().year
    years = [[] for _ in range(current_year-2003 + 1)]
    for day in days:
        years[day[0].year-2003].append(day)
    return years
    
def unify_year(dates: List[Tuple[datetime, float]], year:int=2021):
    unified_dates = []
    for date in dates:
        unified_dates.append((date[0].replace(year=year), date[1]))
        # print(date[0].year)
    return unified_dates