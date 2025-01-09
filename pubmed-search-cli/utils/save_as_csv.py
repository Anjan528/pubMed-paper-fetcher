import pandas as pd

def save_to_csv(data, filename):
    if filename is None:
        print("Missing filename e.g. example.csv") 
        return 
    df = pd.DataFrame(data)
    # sort by PubmedID
    df = df.sort_values(by='PubmedID')
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
