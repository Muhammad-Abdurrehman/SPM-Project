import requests

# Replace with your PythonAnywhere username and API token
username = 'abdurrehmanayub01'
token = '2653c6ee615d1153fb7087520ae9965fd27037ac'
console_id=31689036
domain_name="AbdurrehmanAyub01.pythonanywhere.com"

# Step 1: Fetch the list of consoles
input_url = f'https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{console_id}/send_input/'

change_directory_command = f'cd /home/{username}/SPM-Project'
change_directory_payload = {'input': change_directory_command + '\n'}

git_pull = f'git pull'
git_pull_payload = {'input': git_pull + '\n'}

headers = {'Authorization': f'Token {token}'}

response_cd = requests.post(input_url, headers=headers, json=git_pull_payload)

if response_cd.status_code == 200:
    print('Code Updated')

web_app_url = f'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/'
response = requests.post(web_app_url, headers=headers)
if response.status_code == 200:
    print("Website reloaded successfully")