import numpy as np

def normalize_data(raw_data, center_value, k = float):

    normalized_data = 1 / (1 + np.exp(-k * (raw_data - center_value)))*100
    # print(normalized_data)
    return normalized_data

def normalize_data_linear(raw_data, min_raw_data, max_raw_data):

    normalized_data_linear = (raw_data - min_raw_data) / (max_raw_data - min_raw_data) * 100
    # print(normalized_data_linear)
    return normalized_data_linear


