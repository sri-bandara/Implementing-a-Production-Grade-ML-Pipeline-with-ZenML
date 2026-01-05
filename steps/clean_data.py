import logging

import pandas as pd 
from zenml import step

from src.data_cleaning import DataCleaning, DataPreprocessStrategy, DataDivideStrategy
from typing_extensions import Annotated 
from typing import Tuple

@step #zenml step
def clean_df(df: pd.DataFrame) -> Tuple[ #input is dataframe output is split sets
    Annotated[pd.DataFrame, "X_train"],
    Annotated[pd.DataFrame, "X_test"],
    Annotated[pd.Series, "y_train"],
    Annotated[pd.Series, "y_test"],
]:
    try:
        process_strategy = DataPreprocessStrategy() #creating preprocess strategy object
        data_cleaning = DataCleaning(df, process_strategy)
        processed_data = data_cleaning.handle_data()

        divide_strategy = DataDivideStrategy() #creating divide strategy object
        data_cleaning = DataCleaning(processed_data, divide_strategy)
        X_train, X_test, y_train, y_test = data_cleaning.handle_data()
        logging.info("Data cleaning completed")
        return X_train, X_test, y_train, y_test
    except Exception as e:
        logging.error("Error in cleaning data: {}".format(e))
        raise e