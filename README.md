PubMed Paper Fetcher
===================

This script is a tool to fetch and process data from PubMed, extracting useful details like paper titles, publication dates, author affiliations, and corresponding author email addresses. The data can be saved in a structured CSV format for further analysis.

Features
--------

*   Fetch PubMed article IDs based on a search query.
    
*   Retrieve detailed information about each article.
    
*   Extract non-academic author details and their affiliations.
    
*   Identify corresponding authors' email addresses.
    
*   Save the processed data in a CSV file.
    

Requirements
------------

### Python Version

*   Python 3.6 or higher
    

### Required Libraries

*   requests
    
*   re
    
*   pandas
    
*   argparse
    

To install the required libraries, use:

<pre>
  <code>
    pip install requests pandas
  </code>
</pre>
Usage
-----

### Command-Line Arguments

1.  **query**: _(Required)_ Search query for PubMed.
    
2.  **\-d, --debug**: _(Optional)_ Enable debug mode for additional logs.
    
3.  **\-f, --file**: _(Optional)_ Specify the output file name (CSV format).
    

### Example Command

<pre>
    <code>
     python main.py "breast cancer" -d -f output.csv 
    </code>
</pre>

How It Works
------------

1.  **Fetch PubMed IDs**:
    
    *   Queries PubMed using the provided search term.
        
    *   Retrieves up to 100 article IDs.
        
2.  **Retrieve Paper Details**:
    
    *   Fetches article metadata for each PubMed ID, including title, publication date, and authors.
        
3.  **Extract Author Information**:
    
    *   Identifies non-academic authors affiliated with companies (e.g., pharma, biotech).
        
    *   Extracts the email address of the corresponding author if available.
        
4.  **Save to CSV**:
    
    *   Stores the collected data in a CSV file for further use.
        

Functions
---------

### 1\. fetch\_pubmed\_ids(query, debug=False)

Fetches PubMed IDs for a given query.

**Parameters**:

*   query: Search term for PubMed.
    
*   debug: (Optional) Enable debugging logs.
    

**Returns**:

*   A list of PubMed IDs.
    

### 2\. fetch\_paper\_details(paper\_id)

Retrieves metadata for a specific PubMed ID.

**Parameters**:

*   paper\_id: PubMed ID of the article.
    

**Returns**:

*   A dictionary with article details.
    

### 3\. extract\_non\_academic\_authors(authors)

Extracts non-academic authors and their company affiliations.

**Parameters**:

*   authors: List of author data.
    

**Returns**:

*   A tuple containing non-academic authors and their affiliations.
    

### 4\. extract\_corresponding\_email(authors)

Finds the corresponding author's email.

**Parameters**:

*   authors: List of author data.
    

**Returns**:

*   The email address of the corresponding author or an empty string if not found.
    

### 5\. process\_paper\_data(ids, debug=False)

Processes metadata for multiple PubMed IDs.

**Parameters**:

*   ids: List of PubMed IDs.
    
*   debug: (Optional) Enable debugging logs.
    

**Returns**:

*   A list of dictionaries containing processed article data.
    

### 6\. save\_to\_csv(data, filename)

Saves the processed data to a CSV file.

**Parameters**:

*   data: List of dictionaries containing processed data.
    
*   filename: The name of the output CSV file.
    

Example Output
--------------

A CSV file with columns:

*   **PubmedID**
    
*   **Title**
    
*   **Publication Date**
    
*   **Non-academic Author(s)**
    
*   **Company Affiliation(s)**
    
*   **Corresponding Author Email**
    

Error Handling
--------------

*   Handles request timeouts, connection errors, and other request exceptions.
    
*   Logs descriptive error messages for troubleshooting.
    

Author
------

Developed by \[Anjan Maity\].
