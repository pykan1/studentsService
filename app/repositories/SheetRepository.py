from google.oauth2 import service_account
from googleapiclient.discovery import build

from app.containers import Container


class SheetRepository:
    @staticmethod
    def sheet_service():
        SCOPES = Container().sheet["scope"]
        SERVICE_ACCOUNT_FILE = Container().sheet["keys"]
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        # If modifying these scopes, delete the file token.json.
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        return service.spreadsheets()
