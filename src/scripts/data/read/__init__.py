import pandas as pd
import numpy as np
from streamlit import cache


@cache()
def read_data(path):
    df = pd.read_parquet(path, engine="pyarrow")

    return df
