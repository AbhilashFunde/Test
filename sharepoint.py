import requests
import time

# Skytap API credentials
SKYTAP_USERNAME = "your_username"
SKYTAP_API_TOKEN = "your_api_token"

# Environment IDs
DOMAIN_CONTROLLER_ENV_ID = "dc_environment_id"
SQL_SERVER_ENV_ID = "sql_server_environment_id"
SHAREPOINT_SERVER_ENV_ID = "sharepoint_server_environment_id"

# Start Domain Controller
print("Starting Domain Controller...")
headers = {"Content-Type": "application/json"}
data = {"runstate": "running"}
url = f"https://cloud.skytap.com/configurations/{DOMAIN_CONTROLLER_ENV_ID}"
requests.post(url, auth=(SKYTAP_USERNAME, SKYTAP_API_TOKEN), headers=headers, json=data)

# Wait for Domain Controller to start
time.sleep(60)

# Start SQL Server
print("Starting SQL Server...")
url = f"https://cloud.skytap.com/configurations/{SQL_SERVER_ENV_ID}"
requests.post(url, auth=(SKYTAP_USERNAME, SKYTAP_API_TOKEN), headers=headers, json=data)

# Wait for SQL Server to start
time.sleep(60)

# Start SharePoint Server
print("Starting SharePoint Server...")
url = f"https://cloud.skytap.com/configurations/{SHAREPOINT_SERVER_ENV_ID}"
requests.post(url, auth=(SKYTAP_USERNAME, SKYTAP_API_TOKEN), headers=headers, json=data)

# Wait for SharePoint Server to start
time.sleep(60)

print("All servers started successfully!")
