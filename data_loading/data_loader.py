import pandas as pd
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder


def load_dataset(file_path):
    df, x_data, y_data = load_data(file_path)
    # 90 % train, 5 % test, 5 % val
    x_train, x_temp, y_train, y_temp = train_test_split(x_data, y_data, test_size=0.1, random_state=42)
    x_val, x_test, y_val, y_test = train_test_split(x_temp, y_temp, test_size=0.5, random_state=42)

    return x_train, y_train, x_val, y_val, x_test, y_test


def load_data(file_path):
    df = pd.read_csv(file_path)
    drop_cols = ["Attack_label", "Attack_type"]
    df_feats = df.drop(columns=[c for c in drop_cols if c in df.columns])

    x = df_feats.to_numpy().astype('float32')  # Features: all columns except 'Attack_type'
    y = to_categorical(LabelEncoder().fit_transform(df['Attack_type']))
    return df, x, y
