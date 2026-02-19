# Photo Quality Estimator → Google Sheets

A modular Python tool that evaluates the technical quality of photos in a specified directory, calculates quality scores based on multiple image metrics, and exports the results to Google Sheets with automatic formatting.

This tool was built to speed up manual photo review workflows and automate repetitive quality checks.

---

## Overview

The script:

1. Loads images from a local directory
2. Runs multiple quality checks (noise, sharpness, exposure, etc.)
3. Normalizes metric values
4. Calculates a final score per image
5. Exports results to Google Sheets
6. Applies formatting for better readability

The project is structured as a modular pipeline, allowing new quality checks to be added easily.

---

## Quality Metrics

The following checks are currently implemented:

- Noise estimation
- Clipping detection (highlights & shadows)
- Sharpness estimation
- Artifact detection
- Exposure evaluation
- Contrast evaluation

Each metric produces a score that contributes to the final image quality rating.

Scores are normalized before aggregation to ensure balanced evaluation.

---

## Tech Stack

- Python
- OpenCV (`cv2`) – image analysis
- NumPy – numerical computation
- gspread – Google Sheets integration
- gspread-formatting – spreadsheet formatting
- Google API authentication (service account / OAuth)
- Dynamic module discovery using `importlib` and `pkgutil`

---

## Project Structure
to directory Google-API-key add api-key.json from Google https://console.cloud.google.com/welcome?pli=1&inv=1&invt=Ab3_KA&project=crypto-iris-438820-j4
