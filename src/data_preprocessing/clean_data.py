import pandas as pd
import numpy as np
from load_data import load_dataset


def clean_dataset(file_name):
    """
    Clean CICIDS dataset:
    - Fix column names
    - Handle missing values
    - Handle infinite values
    - Remove duplicates
    """

    # =========================
    # 1. LOAD DATA
    # =========================
    df = load_dataset(file_name)

    print("\nDataset Loaded:", df.shape)

    # =========================
    # 2. FIX COLUMN NAMES
    # =========================
    df.columns = df.columns.str.strip()

    # =========================
    # 3. CHECK MISSING VALUES
    # =========================
    print("\nMissing Values BEFORE cleaning:")
    print(df.isnull().sum().sort_values(ascending=False).head())

    # =========================
    # 4. HANDLE INFINITE VALUES
    # =========================
    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    # =========================
    # 5. HANDLE MISSING VALUES
    # =========================
    df.dropna(inplace=True)

    print("\nDataset shape after removing NaN:", df.shape)

    # =========================
    # 6. REMOVE DUPLICATES
    # =========================
    before = df.shape[0]
    df.drop_duplicates(inplace=True)
    after = df.shape[0]

    print(f"\nDuplicates removed: {before - after}")

    # =========================
    # 7. FINAL CHECK
    # =========================
    print("\nMissing Values AFTER cleaning:")
    print(df.isnull().sum().sum())

    print("\nFinal Dataset Shape:", df.shape)

    return df


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    df = clean_dataset("Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

    print("\nSample after cleaning:")
    print(df.head())