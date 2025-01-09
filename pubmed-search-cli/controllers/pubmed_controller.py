import requests
import re
from requests.exceptions import Timeout, ConnectionError

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
DETAILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_pubmed_ids(query, debug=False):
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 100,
    }

    if debug:
        print("Fetching PubMed IDs with query:", query)

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()  
    except Timeout:
        print("Request timed out while fetching PubMed IDs.")
        return []
    except ConnectionError:
        print("Connection error while fetching PubMed IDs.")
        return []
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

    ids = response.json().get("esearchresult", {}).get("idlist", [])
    if debug:
        print(f"Found {len(ids)} papers.")
    return ids


def fetch_paper_details(paper_id):
    details_params = {
        "db": "pubmed",
        "id": paper_id,
        "retmode": "json",
    }

    try:
        details_response = requests.get(DETAILS_URL, params=details_params, timeout=10)
        details_response.raise_for_status()
    except Timeout:
        print(f"Request timed out while fetching details for paper ID {paper_id}.")
        return {}
    except ConnectionError:
        print(f"Connection error while fetching details for paper ID {paper_id}.")
        return {}
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return {}

    return details_response.json().get("result", {}).get(paper_id, {})


def extract_non_academic_authors(authors):
    non_academic_authors = []
    company_affiliations = []
    for author in authors:
        affiliation = author.get("affiliation", "")
        if re.search(r"\b(pharma|biotech|company|corp|inc|ltd)\b", affiliation, re.IGNORECASE):
            non_academic_authors.append(author.get("name", ""))
            company_affiliations.append(affiliation)
    return non_academic_authors, company_affiliations


def extract_corresponding_email(authors):
    for author in authors:
        if "@" in author.get("affiliation", ""):
            return author.get("affiliation").split()[-1]
    return ""


def process_paper_data(ids, debug=False):
    paper_data = []
    for paper_id in ids:
        summary = fetch_paper_details(paper_id)
        if not summary:
            continue

        title = summary.get("title", "")
        pub_date = summary.get("pubdate", "")
        authors = summary.get("authors", [])

        # gets non_academic authors
        non_academic_authors, company_affiliations = extract_non_academic_authors(authors)
        # gets corresponding authors email
        corresponding_email = extract_corresponding_email(authors)
        # map the data 
        paper_data.append({
            "PubmedID": paper_id,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": ", ".join(non_academic_authors),
            "Company Affiliation(s)": ", ".join(company_affiliations),
            "Corresponding Author Email": corresponding_email,
        })

    return paper_data


