import gspread
import os
import time



def authorisation_to_google_sheets():
    """
    configure google api
    https://console.cloud.google.com/welcome?pli=1&inv=1&invt=Ab3_KA&project=crypto-iris-438820-j4
    - put api-key in  right folder
    - Tries to find  aip key, if it is not there it throws error
    - authorizes
    - Gets  specified google table and specified sheet
    :return: worksheet of google sheet
    """
    module_dir = os.path.dirname(__file__)


    api_key_path = os.path.join(module_dir, '..', 'Google-API-key', 'api-key.json') # take api key
    if not os.path.exists(api_key_path):
        raise FileNotFoundError(f"Api-key is not found: {api_key_path}")

    gc = gspread.service_account(filename=api_key_path) # login to the google

    # open doc and sheet
    sh = gc.open("TestSheet")
    work_sheet = sh.sheet1

    return work_sheet



def find_write_data_to_google_sheets(sheet_data, data_name):

    # read sheet
    data = sheet_data.row_values(1)

    # looking for empty column or column with necessary names
    for idx, name in enumerate(data, start=1):
        if name.strip().lower() == data_name.strip().lower():
            return idx

    try:
        # need use try because list.index(value) return ValueError
        idx = data.index('') + 1  # gspread uses index since 1
    except ValueError:
        idx = len(data) + 1  # if it doesn't have empty colom - add to the end

    # write name of the cell
    sheet_data.update_cell(1, idx, data_name)

    # return number of colomn for next function
    return idx




def add_data_to_google_sheets(data_img_check_algorithms:dict, sheet_data):

    # Check keys from dick and find columns, after writing data of the file and the result of the algorithms

    for data_key, data_value in data_img_check_algorithms.items():
        col_index = find_write_data_to_google_sheets(sheet_data, data_key)
        col_values = sheet_data.col_values(col_index)
        row_index = len(col_values) + 1
        sheet_data.update_cell(row_index, col_index, data_value)
        time.sleep(2)
        # temporary, kostil. To reduce the number of requests.





