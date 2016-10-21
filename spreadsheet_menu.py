import httplib2
import day_menu
import string
from config import user_char
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials

scopes = ['https://www.googleapis.com/auth/spreadsheets']
sheet_menu_range = "'{0}'!C4:C43"

row_index_start = 3
row_index_end = 43
user_column_index = string.ascii_uppercase.index(user_char)

def make_order(spreadsheet_id):
    gapi = get_api()

    result = gapi.get(spreadsheetId=spreadsheet_id, fields="sheets/properties").execute()

    for sheet in result['sheets']:
        if 'hidden' not in sheet['properties']:
            make_day_order(gapi, spreadsheet_id, sheet['properties'])


def make_day_order(gapi, spreadsheet_id, sheet_properties):
    sheet_title=sheet_properties['title']
    print("Заказ на " + sheet_properties['title'])

    # get available menu
    result = gapi.values().get(spreadsheetId=spreadsheet_id, range=sheet_menu_range.format(sheet_title)).execute()

    rows = [(index, row[0]) for index, row in enumerate(result['values']) if len(row) > 0]
    available_menu = [row[1] for row in rows]

    plan = day_menu.plan(available_menu, 50)
    print(plan)

    rows_nums = [next(row[0] for row in rows if row[1] is food_name) + row_index_start for food_name in plan[1]]

    requests = []
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": sheet_properties['sheetId'],
                "startRowIndex": row_index_start,
                "endRowIndex": row_index_end,
                "startColumnIndex": user_column_index,
                "endColumnIndex": user_column_index + 1
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {
                        "red": 1,
                        "green": 1,
                        "blue": 1,
                        "alpha": 1
                    }
                }
            },
            "fields": "userEnteredFormat.backgroundColor"
        }
    })
    for row_num in rows_nums:
        requests.append({
            "updateCells": {
                "rows": [
                    {
                        "values": [
                            {
                                "userEnteredFormat": {
                                    "backgroundColor": {
                                        "red": 0,
                                        "green": 0,
                                        "blue": 0,
                                        "alpha": 1
                                    }
                                }
                            }
                        ]
                    }
                ],
                "fields": "userEnteredFormat.backgroundColor",
                "start": {
                    "sheetId": sheet_properties['sheetId'],
                    "rowIndex": row_num,
                    "columnIndex": user_column_index,
                }
            }
        })

    body = {
        'requests': requests
    }
    gapi.batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()


def get_api():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discovery_url = 'https://sheets.googleapis.com/$discovery/rest?version=v4'
    return discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discovery_url).spreadsheets()


def get_credentials():
    return ServiceAccountCredentials.from_json_keyfile_name('credentials/client_secret.json', scopes)


make_order('1eDqS5ilQfPwnCmGE0HCIFdwufNwoT3ez0dxO-0zF5s8')