import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''Load takes a path as an arg, load the csv file and
    fill it in a pd.DataFrame'''
    try:
        data = pd.read_csv(path)
        print(f"Loading dataset of dimension {data.shape}")
        return data
    except Exception as e:
        print(f"error with path or file type: {e}")
        return None
