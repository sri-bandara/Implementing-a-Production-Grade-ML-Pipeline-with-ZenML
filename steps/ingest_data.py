import logging #used to print structured messages in production

import pandas as pd 
from zenml import step 

class IngestData:
    def __init__(self, data_path: str):
        self.data_path = data_path #storing file path when object is created

    def get_data(self):
        logging.info(f"Ingesting data from {self.data_path}")
        return pd.read_csv(self.data_path)

@step #pipeline step
def ingest_df(data_path: str) -> pd.DataFrame: #input is the data path and output is a dataframe
    try:
        ingest_data = IngestData(data_path) #creates ingest data object
        df = ingest_data.get_data() 
        return df
    except Exception as e:
        logging.error(f"Error while ingesting data: {e}")
        raise e