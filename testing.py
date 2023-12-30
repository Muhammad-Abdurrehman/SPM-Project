import requests

# Replace with your PythonAnywhere username and API token
username = 'abdurrehmanayub01'
token = '2653c6ee615d1153fb7087520ae9965fd27037ac'
console_id=31689036

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

# if response_consoles.status_code == 200:
#     consoles = response_consoles.json()['result']
#     if consoles:
#         # Choose the first console (you may need to adjust this based on your setup)
#         console_id = consoles[0]['id']

#         # Step 2: Send command to change directory
#         change_directory_command = 'cd /home/{}/SPM-Project'.format(username)
#         change_directory_payload = {'input': change_directory_command + '\n'}
#         change_directory_input_url = f'https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{console_id}/send_input/'
#         response_cd = requests.post(change_directory_input_url, headers=headers, json=change_directory_payload)

#         if response_cd.status_code == 200:
#             print('Changed directory successfully.')

#             # Step 3: Send command to perform git pull
#             git_pull_command = 'git pull origin main'  # Adjust the branch name as needed
#             git_pull_payload = {'input': git_pull_command + '\n'}
#             git_pull_input_url = f'https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{console_id}/send_input/'
#             response_git_pull = requests.post(git_pull_input_url, headers=headers, json=git_pull_payload)

#             print('Git pull response:', response_git_pull.status_code, response_git_pull.content)
#         else:
#             print('Error changing directory:', response_cd.status_code, response_cd.content)
#     else:
#         print('No consoles available.')
# else:
#     print('Error fetching consoles:', response_consoles.status_code, response_consoles.content)
