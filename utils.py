import csv


def csv_to_train_data(csv_file_path, bot_col, resp_col):
    """
    Converts csv to training data
    """
    with open(csv_file_path) as f:
        csv_reader = csv.reader(f, delimiter=',')

        data = []
        for row in csv_reader:
            data.extend([row[resp_col], row[bot_col]])

    return data
