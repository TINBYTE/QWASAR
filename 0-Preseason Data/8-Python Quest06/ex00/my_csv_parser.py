def my_csv_parser(param1, param2):
    param1 = param1.strip()
    return [row.split(param2) for row in param1.split("\n")]
