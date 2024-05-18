import requests
import pandas as pd
from datetime import datetime

# Set the URL of the Web UI and login information
qb_url = 'http://your_qbittorrent_web_ui_url'  # Replace with your qBittorrent Web UI URL
username = 'your_username'                      # Replace with your username
password = 'your_password'                      # Replace with your password

# Log in to get the cookie
login_payload = {'username': username, 'password': password}
session = requests.Session()
response = session.post(f'{qb_url}/api/v2/auth/login', data=login_payload)

# Check if login is successful
if response.status_code == 200 and response.text == "Ok.":
    print("Login successful")
else:
    print("Login failed")
    exit()

# Get torrent information
response = session.get(f'{qb_url}/api/v2/torrents/info')
if response.status_code == 200:
    torrents = response.json()
else:
    print("Failed to get torrent information")
    exit()

# Function: Convert bytes to a suitable unit
def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Y{suffix}"

# Extract the required torrent information
data = []
for torrent in torrents:
    torrent_info = {
        'Name': torrent['name'],
        'Size': sizeof_fmt(torrent['total_size']),
        'Uploaded': sizeof_fmt(torrent['uploaded']),
        'Ratio': torrent['ratio'],
        'Added Time': pd.to_datetime(torrent['added_on'], unit='s'),  # Convert timestamp to datetime
        'Completion Time': pd.to_datetime(torrent['completion_on'], unit='s') if torrent['completion_on'] != -1 else None,  # Convert timestamp to datetime
        'Update Time': datetime.now()  # Add last update time
    }
    data.append(torrent_info)

# Create DataFrame
df_new = pd.DataFrame(data)

# Read the previous Excel data
try:
    df_old = pd.read_excel('path_to_your_previous_excel_file')  # Replace with the path to your previous Excel file
except FileNotFoundError:
    df_old = pd.DataFrame()

# Merge data and remove duplicates
df_merged = pd.concat([df_old, df_new]).drop_duplicates(subset=['Name', 'Added Time'], keep='last')

# Export to Excel
excel_file = 'path_to_your_output_excel_file'  # Replace with the path to your output Excel file
df_merged.to_excel(excel_file, index=False)

print(f"Torrent information exported to {excel_file}")
