from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import json
import requests
from xml.etree import ElementTree as ET
 
# URL of the sitemap
sitemap_url = 'https://shop0.xyz/product-sitemap.xml'
 
JSON_KEY_FILE = "your.json"
 
SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
 
 
# Authorize credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)
http = credentials.authorize(httplib2.Http())
 
# Fetch the sitemap XML
response = requests.get(sitemap_url)
sitemap_xml = response.text
 
# Parse the sitemap XML
sitemap_root = ET.fromstring(sitemap_xml)
 
# Iterate over URLs in the sitemap
for child in sitemap_root:
    url = child[0].text  # Assuming the <loc> tag contains the URL
    
    # Build the request body
    content = {}
    content['url'] = url
    content['type'] = "URL_UPDATED"
    json_content = json.dumps(content)
    
    response, content = http.request(ENDPOINT, method="POST", body=json_content)
    result = json.loads(content.decode())
    
    # Handle the result as needed
    print(result)
