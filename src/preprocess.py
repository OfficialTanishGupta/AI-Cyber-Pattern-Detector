import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler



train_path = "../data/KDDTrain+.txt"

df = pd.read_csv(train_path, header=None)

print("Dataset Loaded Successfully")
print(df.head())



columns = [
    "duration","protocol_type","service","flag","src_bytes",
    "dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins",
    "logged_in","num_compromised","root_shell","su_attempted","num_root",
    "num_file_creations","num_shells","num_access_files","num_outbound_cmds",
    "is_host_login","is_guest_login","count","srv_count","serror_rate",
    "srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
    "diff_srv_rate","srv_diff_host_rate","dst_host_count",
    "dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate","dst_host_srv_diff_host_rate",
    "dst_host_serror_rate","dst_host_srv_serror_rate",
    "dst_host_rerror_rate","dst_host_srv_rerror_rate",
    "attack","difficulty"
]

df.columns = columns

print("\nColumns Added Successfully")



df.drop("difficulty", axis=1, inplace=True)

print("\nDifficulty Column Removed")



categorical_columns = [
    "protocol_type",
    "service",
    "flag"
]

encoder = LabelEncoder()

for column in categorical_columns:
    df[column] = encoder.fit_transform(df[column])

print("\nCategorical Columns Encoded")



# normal = 0
# attack = 1

df["attack"] = df["attack"].apply(
    lambda x: 0 if x == "normal" else 1
)

print("\nAttack Labels Converted")



X = df.drop("attack", axis=1)

y = df["attack"]

print("\nFeatures Shape:", X.shape)
print("Labels Shape:", y.shape)



scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)

print("\nFeatures Normalized")



print("\nFirst Processed Row:")
print(X_scaled[0])

print("\nPreprocessing Completed Successfully")



processed_df = pd.DataFrame(X_scaled)

processed_df["attack"] = y.values

processed_df.to_csv(
    "../data/processed_data.csv",
    index=False
)

print("\nProcessed Dataset Saved")