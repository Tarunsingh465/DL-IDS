import pandas as pd
import os

def load_dataset(file_name):
    """
    Load dataset from data folder
    """
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    file_path = os.path.join(base_path, "data", file_name)

    print(f"Loading file from: {file_path}")

    df = pd.read_csv(file_path)

    return df


if __name__ == "__main__":
    df = load_dataset("Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

    print("Shape:", df.shape)
    print("\nColumns:\n", df.columns)
    print("\nSample:\n", df.head())