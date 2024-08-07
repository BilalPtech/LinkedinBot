import gspread
from oauth2client.service_account import ServiceAccountCredentials

def write_to_google_sheet(profile):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("app/utils/linkedinbot-431807-87638b129bf0.json", scope)

    client = gspread.authorize(creds)

    try:
        spreadsheet = client.open("linkedinprofile data")
    except gspread.exceptions.SpreadsheetNotFound:
        spreadsheet = client.create("linkedinprofile data")
        spreadsheet.share('testnetptech123@linkedinbot-431807.iam.gserviceaccount.com', perm_type='user', role='writer')
        spreadsheet.share('testnetptech123@gmail.com', perm_type='user', role='writer')

    sheet = spreadsheet.sheet1

    header = ["Name", "URL", "Job Title", "Current Company", "Headline", "Location", "Connections Count", "About", "Connection Sent Time"]
    if sheet.row_count == 0 or sheet.row_values(1) != header:
        sheet.append_row(header)

    row = [
        profile.get("Name", ""),
        profile.get("URL", ""),
        profile.get("Job Title", ""),
        profile.get("Current Company", ""),
        profile.get("Headline", ""),
        profile.get("Location", ""),
        profile.get("Connections Count", ""),
        profile.get("About", ""),
        profile.get("Connection Sent Time", "")
    ]
    sheet.append_row(row)
    print('data written')