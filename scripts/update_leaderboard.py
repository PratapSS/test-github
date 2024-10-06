import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate with Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("scripts/gitbasics.json", scope)
client = gspread.authorize(creds)

# Open the leaderboard sheet
sheet = client.open("Git Leaderboard").sheet1

# Example of updating the leaderboard for a user
def update_leaderboard(username, points):
    users = sheet.col_values(1)  # Assuming usernames are in column 1
    if username in users:
        row = users.index(username) + 1
        current_points = int(sheet.cell(row, 2).value)
        sheet.update_cell(row, 2, current_points + points)
    else:
        sheet.append_row([username, points])

# Add points based on activity
update_leaderboard("student_username", 10)
