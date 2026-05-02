import pandas as pd
from clean_data import clean_dataset


def select_features(file_name):
    """
    Remove irrelevant columns and keep useful features
    """

    # =========================
    # 1. LOAD CLEAN DATA
    # =========================
    df = clean_dataset(file_name)

    print("\nInitial Shape:", df.shape)

    # =========================
    # 2. DROP IRRELEVANT COLUMNS (IF EXISTS)
    # =========================
    drop_cols = [
        "Flow ID",
        "Source IP",
        "Destination IP",
        "Timestamp"
    ]

    df.drop(columns=[col for col in drop_cols if col in df.columns], inplace=True)

    print("\nDropped unnecessary columns (if present)")

    # =========================
    # 3. SEPARATE FEATURES & LABEL
    # =========================
    X = df.drop("Label", axis=1)
    y = df["Label"]

    print("\nFeature Shape:", X.shape)
    print("Label Shape:", y.shape)

    # =========================
    # 4. FINAL CHECK
    # =========================
    print("\nRemaining Columns:", len(X.columns))
    print("\nSample Features:")
    print(X.head())

    return X, y


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    X, y = select_features("Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

    print("\nFeature Selection Completed ✅")