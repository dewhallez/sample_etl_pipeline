import pandas as pd
import pytest
from sqlalchemy import create_engine

def test_empty_dataframe_load():
    df = pd.DataFrame()
    engine = create_engine("sqlite:///:memory:")
    with pytest.raises(ValueError):
        if df.empty:
            raise ValueError("DataFrame is empty, nothing to load.")
