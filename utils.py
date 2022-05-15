import time
from datetime import datetime
import numpy as np
import pandas as pd

def timestampToDate(ts):
    return datetime(np.array(ts,dtype=np.uint64))

def dateToTimestamp(dt):
    dt_obj = datetime.strptime(dt, '%d.%m.%Y')
    return str(int(dt_obj.timestamp() * 1000))[:10]
