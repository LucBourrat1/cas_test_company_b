import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    da_prices = pd.read_csv("/home/luc/Documents/dev/python/projects/Cas_Data_Scientist/DA_Prices_Case.csv")
    imbalance_prices = pd.read_csv("/home/luc/Documents/dev/python/projects/Cas_Data_Scientist/Imbalances_Prices_Case.csv")
    power_case = pd.read_csv("/home/luc/Documents/dev/python/projects/Cas_Data_Scientist/Power_Case.csv")
    power_forecasts = pd.read_csv("/home/luc/Documents/dev/python/projects/Cas_Data_Scientist/Power_Forecasts_Case.csv")
    
    print("debug")
    return

if __name__ == '__main__':
    main()
    