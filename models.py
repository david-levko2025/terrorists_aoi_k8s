import pandas as pd
import numpy as np

def validation_data():
    """read the csv file"""
    df = pd.read_csv("terrorists_data.csv")
    """sort the most danger terroists"""
    sort_by_danger = df.sort_values('danger_rate', ascending=False)
    """drop age column"""
    drop_age = sort_by_danger.drop('age',axis=1)
    """drop group column"""
    drop_group = drop_age.drop('group',axis=1)
    """drop last_seen column"""
    drop_last_seen = drop_group.drop('last_seen',axis=1)
    """drop notes column"""
    drop_notes = drop_last_seen.drop('notes',axis=1)
    """the most 5 dangers terrorists"""
    the_high_five = drop_notes.head(5)

    return the_high_five

from pydantic import BaseModel


class Terorists(BaseModel):
    name : str
    danger_rate : int
    location : str
