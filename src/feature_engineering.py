import pandas as pd

class FeatureEngineer:

    def __init__(self, data):

        self.data = data.copy()

    def encode_binary(self):

        binary_cols = [
            "mainroad",
            "guestroom",
            "basement",
            "hotwaterheating",
            "airconditioning",
            "prefarea"
        ]

        for col in binary_cols:

            self.data[col] = self.data[col].map({
                "yes":1,
                "no":0
            })

        print("✅ Binary encoding complete")

        return self.data


    def encode_furnishing(self):

        self.data = pd.get_dummies(
            self.data,
            columns=["furnishingstatus"],
            drop_first=True
        )

        print("✅ Furnishing encoded")

        return self.data


    def split_features_target(self, target):

        X = self.data.drop(target, axis=1)

        y = self.data[target]

        return X, y