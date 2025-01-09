import pandas as pd
import argparse
from controllers.pubmed_controller import fetch_pubmed_ids, process_paper_data
from utils.save_as_csv import save_to_csv

def main():
    parser = argparse.ArgumentParser(description='Fetch and process PubMed data.')
    parser.add_argument('query', type=str, help='Search query for PubMed')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode')
    parser.add_argument('-f', '--file', type=str, help='Output file name (CSV)')

    args = parser.parse_args()

    ids = fetch_pubmed_ids(args.query, args.debug)
    if not ids:
        print("No data found.")
        return

    data = process_paper_data(ids, args.debug)
    if not data:
        print("No paper data found.")
        return

    if args.file:
        save_to_csv(data, args.file)
    else:
        print(pd.DataFrame(data).sort_values(by="PubmedID"))


if __name__ == "__main__":
    main()
