import os
import sys
import pytest
import pandas as pd

# Ensure src is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from data.load_data import load_data
from data.preprocess import preprocess

def test_load_data():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    data.to_csv('test.csv', index=False)
    loaded_data = load_data('test.csv')
    assert isinstance(loaded_data, pd.DataFrame)
    assert not loaded_data.empty

def test_preprocess():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [None, 5, 6]
    })
    processed_data = preprocess(data)
    assert isinstance(processed_data, pd.DataFrame)
    assert processed_data.isna().sum().sum() == 0
    assert (processed_data.mean().round(2) == 0).all()

