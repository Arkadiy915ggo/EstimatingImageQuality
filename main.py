import cv2
import importlib
import pkgutil
import Modules_EstimateImgQuality
from Modules_DataExport.DataExport_GoogleSheets import authorisation_to_google_sheets, add_data_to_google_sheets
from pathlib import Path


# common variables. path to the folder should be moved to separate module with the input date
folder = Path("F:/photo/Exorts/forStock/") #
completed_data = {}
authorisation_data = authorisation_to_google_sheets()

# run all modules located in the Modules_DataExport folder, to add a new algorithm - need to add this algorithm to the folder. It should accept an image, return a variable string
def run_estimate_modules(image):

    results = {}
    for _, module_name, _ in pkgutil.iter_modules(Modules_EstimateImgQuality.__path__):
        # print(module_name)
        module = importlib.import_module(f'Modules_EstimateImgQuality.{module_name}')

        if hasattr(module, 'estimate'):
            result = module.estimate(image)
            short_name = '_'.join(module_name.split('_')[2:])
            results[short_name] = result

    return results


# main cycle, read whole images from folder, run estimating, form algorithm data, give for writing to Google Sheets
for file in folder.iterdir():
    if file.suffix.lower() in [".jpg", ".jpeg"]:
        raw_image = cv2.imread(str(file))
        estimated_data = run_estimate_modules(raw_image)
        file_data = {"Name": file.name}
        completed_data = file_data|estimated_data
        add_data_to_google_sheets(completed_data, authorisation_data)
