# Task 2 - Mahalakshmi -20572108

import urllib.parse


url = "https://www.abcd.com/search?q=python"
parsed_url = urllib.parse.urlparse(url)

print("Website / Domain:", parsed_url.netloc)
print("Path:", parsed_url.path)
print("Query:", parsed_url.query)
