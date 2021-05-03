#17MIS0307_PARTHIBAN_S
from datetime import datetime

import pandas as pd

date_str = '04:23:15'
nunam_assignment = pd.read_csv(
    'detail.csv', low_memory=False,
    date = datetime.strptime(date_str, '%H:%M:%S'),
    index_col=['Record ID']
)
nunam_assignment