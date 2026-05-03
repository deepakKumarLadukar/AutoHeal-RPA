import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES=['https://www.googleapis.com/auth/gmail.readonly']

def get_emails():
    creds=None

    base_dir=os.path.dirname(__file__)
    token_path=os.path.join(base_dir, 'token.json')
    cred_path=os.path.join(base_dir, 'credentials.json')

    # Load token if exist
    if os.path.exists('backend/token.json'):
        creds=Credentials.from_authorized_user_file(token_path, SCOPES)

    # If not logged in → trigger login
    if not creds or not creds.valid:
        flow=InstalledAppFlow.from_client_secrets_file(cred_path, SCOPES)
        creds=flow.run_local_server(port=0)

        # Save token
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    # Connect Gmail API
    service = build('gmail','V1', credentials=creds)

    results = service.users().messages().list(userId='me', maxResults=5).execute()
    messages = results.get('messages', [])

    email_list=[]

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_data['payload']['headers']

        subject=""

        for h in headers:
            if h['name'] == 'Subject':
                subject = h['value']

        email_list.append({"subject": subject})

    return email_list