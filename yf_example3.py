"""yf_example3.py

Example of a function to download stock prices of QAN.AX for a given year from Yahoo Finance.
"""

import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    """
    Download Qantas stock prices for a given year and save the information in a CSV file.

    Parameters:
    year (int): The year for which the stock prices will be downloaded.

    Returns:
    None

    Raises:
    None
    """
    tic = 'QAN.AX'
    start = f'{year}-01-01'
    end = f'{year+1}-01-01'
    path_file = cfg.DATADIR
    final_path = os.path.join(path_file,f'qan_prc_{year}csv')
    yf_example2.yf_prc_to_csv(tic, final_path, start=start, end=end)

if __name__ == "__main__":
    qan_prc_to_csv(year=2020)

