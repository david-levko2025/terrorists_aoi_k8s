from models import Terorists
import pandas as pd


class Validation():
    def __init__(self, file) -> None:
        self.file = pd.read_csv(file)

    def top_terorist(self):
        self.file.sort_values(by="danger_rate", ascending=False)
        top_terorist = self.file.head()
        return top_terorist   

    def drop_column_age(self):
        self.file.drop('age',axis=1)
        drop_column = self.file.head()
        return drop_column

    def drop_column_group(self):    
        self.file.drop('group',axis=1)
        drop_column = self.file.head()
        return drop_column

    def drop_column_last_seen(self):
        self.file.drop('last_seen',axis=1)
        drop_column = self.file.head()
        return drop_column

    def drop_column_notes(self):    
        self.file.drop('notes',axis=1)
        drop_column = self.file.head()
        return drop_column



