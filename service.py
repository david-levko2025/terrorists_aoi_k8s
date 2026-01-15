from models import Terorists
import pandas as pd

class ValidationOnData:

    @staticmethod
    def validating_terrorists(top_5_dangers):
        terrorists_list = []
        for terrorists in top_5_dangers:
            terrorists_list.append(Terorists(terrorists["name"] ,
                                             terrorists["location"] ,
                                             terrorists["danger_rate"]).__dict__())
        
        return terrorists_list
    
    def insert_to_mongo(df):
        pass

