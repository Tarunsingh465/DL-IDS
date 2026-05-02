import pandas as pd
import matplotlib.pyplot as plt
from load_data import load_dataset


def run_eda(file_name):
    """
    Perform Exploratory Data Analysis on CICIDS2017 dataset
    """

    # =========================
    # 1. LOAD DATA
    # =========================
    df = load_dataset(file_name)

    print("=" * 60)
    print("DATASET LOADED SUCCESSFULLY")
    print("=" * 60)

    # =========================
    # 2. FIX COLUMN NAMES (VERY IMPORTANT)
    # =========================
    df.columns = df.columns.str.strip()

    print("\nColumn names cleaned (spaces removed) ✅")

    # =========================
    # 3. BASIC INFO
    # =========================
    print("\nShape of Dataset:", df.shape)

    print("\nFirst 10 Columns:")
    print(df.columns[:10].tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nDataset Info:")
    df.info()

    # =========================
    # 4. LABEL DISTRIBUTION
    # =========================
    print("\n" + "=" * 60)
    print("LABEL DISTRIBUTION")
    print("=" * 60)

    if "Label" not in df.columns:
        print("❌ ERROR: 'Label' column not found even after cleaning!")
        print("Available columns:", df.columns.tolist())
        return

    label_counts = df["Label"].value_counts()
    print(label_counts)

    # =========================
    # 5. PERCENTAGE DISTRIBUTION
    # =========================
    print("\nLabel Percentage Distribution:")

    total = len(df)

    for label, count in label_counts.items():
        percentage = (count / total) * 100
        print(f"{label}: {percentage:.2f}%")

    # =========================
    # 6. VISUALIZATION
    # =========================
    plt.figure(figsize=(10, 6))
    label_counts.plot(kind='bar')

    plt.title("Attack Type Distribution")
    plt.xlabel("Attack Type")
    plt.ylabel("Number of Samples")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

    # =========================
    # 7. FEATURE TYPE ANALYSIS
    # =========================
    print("\n" + "=" * 60)
    print("FEATURE TYPE ANALYSIS")
    print("=" * 60)

    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    print(f"Total Numerical Features: {len(numerical_cols)}")
    print(f"Categorical Features: {list(categorical_cols)}")

    # =========================
    # 8. UNIQUE LABELS
    # =========================
    print("\nUnique Labels:")
    print(df["Label"].unique())

    print("\nEDA COMPLETED SUCCESSFULLY ✅")


# =========================
# MAIN EXECUTION
# =========================
if __name__ == "__main__":
    run_eda("Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")