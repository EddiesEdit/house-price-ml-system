import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:

    def __init__(self, data):

        self.data = data

    def plot_distribution(self, column):

        plt.figure(figsize=(6,4))

        sns.histplot(self.data[column], kde=True)

        plt.title(f"Distribution of {column}")

        plt.show()

    def correlation_matrix(self):

        numeric_data = self.data.select_dtypes(include=["number"])

        plt.figure(figsize=(10,6))

        sns.heatmap(
            numeric_data.corr(),
            annot=True,
            cmap="coolwarm"
        )

        plt.title("Correlation Matrix")

        plt.show()