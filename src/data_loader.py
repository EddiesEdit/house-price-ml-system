import pandas as pd

class DataLoader:

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def load_data(self):

        self.data = pd.read_csv(self.filepath)

        print("✅ Data loaded successfully")

        return self.data

    def preview_data(self, rows=5):

        return self.data.head(rows)

    def data_info(self):

        return self.data.info()

    def describe_data(self):

        return self.data.describe()

    def check_missing(self):

        return self.data.isnull().sum()

    def check_unique_counts(self):

        return self.data.nunique()