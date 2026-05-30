import pandas as pd
import pathlib as pth
import argparse


from scripts.process_data_initial import process_data




def init_run() -> None:
    df: pd.DataFrame = process_data(pth.Path(f"data_raw/SG.csv"))
    
    df.to_csv(f"data_processed/SG_nona.csv")



if __name__ == "__main__":
    init_run()