import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

# IMPORTANT - Make sure to share the sheet with the client_email address in your Google JSON Credentials file 

PATH_TO_JSON = '/home/aoblah/.google_credentials.json' 
SCOPES = ['https://spreadsheets.google.com/feeds']

class Gsheet():

    def __init__(self):

        credentials = ServiceAccountCredentials.from_json_keyfile_name(PATH_TO_JSON, scopes=SCOPES)
        self.client = gspread.authorize(credentials)
    
    def get_gsheet(self):
        """
        Gets the data in the worksheet
        """
        spreadsheet = self.client.open_by_key("Dummy key")
        sheet = spreadsheet.worksheet("Sheet1")
        data = sheet.get_all_records()
        return data



    def get_worksheet(self):
        """
        Gets the worksheet
        """
        spreadsheet = self.client.open_by_key("Dummy Key")
        sheet = spreadsheet.worksheet("Sheet1")
        return sheet


    def write_gsheet(self,doc_id,sheet_name,data,start_row,start_col):
        """
        data - list of lists, each sublist is a row of values to be filled in the Sheet
        start_row/start_col - integer. For example, if you want to start populating the sheet from D3,
                          start row = 3, start_col = 4
        """
        spreadsheet = self.client.open_by_key(doc_id)
        sheet = spreadsheet.worksheet(sheet_name)

        for row in data:
            col = start_col
            for val in row:
                sheet.update_cell(start_row,col,val)
                col+=1
            start_row+=1
        return


