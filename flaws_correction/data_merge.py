import os
import shutil
from typing import List, Optional

import pandas as pd

from dt_utils import get_date_sequence


class DataParser:
    def __init__(self, path_to_data: str, start_date: str, end_date: str, cols_to_record: Optional[List[str]] = None):
        self.path_to_data = path_to_data
        self.out_dir = None
        self.__validate_path()
        self.__prepare_output_dir()

        self.cols_to_record = cols_to_record
        if self.cols_to_record is None:
            # use default ones
            self.cols_to_record = ['Confirmed', 'Deaths', 'Recovered', 'Active', 'Incident_Rate', 'Case_Fatality_Ratio']

        self.date_seq = get_date_sequence(start_date, end_date)
        self.parse_files()

    def parse_files(self) -> None:
        # TODO:: develop concurrent files processing

        for i, current_date in enumerate(self.date_seq):
            print(f"Processing: {current_date}")
            table_path = os.path.join(self.path_to_data, current_date) + ".csv"
            if not os.path.exists(table_path):
                print(f"Data for date {current_date} was not found!")
                continue

            df = pd.read_csv(table_path)
            if i == 0:
                # init all necessary objects on first iteration
                # save countries coordinates once
                df[["Lat", "Long_", "Combined_Key"]].to_csv(
                    os.path.join(self.out_dir, "countries_coordinates.csv"),
                    index=False
                )

                # init dict to save all features
                dct = {}
                for region_to_record in df["Combined_Key"].to_list():
                    dct[region_to_record] = {col_to_rec: [] for col_to_rec in self.cols_to_record}
                    dct[region_to_record]["date"] = []

            for _, row in df.iterrows():
                region_key = row["Combined_Key"]
                dct[region_key]["date"].append(current_date)
                for col_to_rec in self.cols_to_record:
                    dct[region_key][col_to_rec].append(row[col_to_rec])

        for country_name, country_dct in dct.items():
            country_csv_path = os.path.join(self.out_dir, country_name) + ".csv"
            pd.DataFrame(country_dct).to_csv(country_csv_path, index=False)

    def __validate_path(self) -> None:
        if not os.path.exists(self.path_to_data):
            raise NotADirectoryError(f"{self.path_to_data} does nopt exists!")

    def __prepare_output_dir(self) -> None:
        data_root = os.path.dirname(self.path_to_data)
        self.out_dir = os.path.join(data_root, "countries_data")
        if os.path.exists(self.out_dir):
            shutil.rmtree(self.out_dir)
        os.makedirs(self.out_dir)


if __name__ == '__main__':
    # see EDA notebook with explanations of date selection
    dp = DataParser(
        path_to_data=os.path.join("..", "data", "csse_covid_19_daily_reports"),
        start_date="2022-01-21",
        end_date="2022-06-21"
    )
