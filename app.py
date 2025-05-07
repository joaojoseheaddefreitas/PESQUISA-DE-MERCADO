import pandas as pd
import numpy as np

def load_data():
    data = pd.read_csv("dados_mercado.csv")
    return data

def analyze_market(data):
    print("Analisando dados de mercado...")
    print(data.head())

if __name__ == "__main__":
    data = load_data()
    analyze_market(data)
