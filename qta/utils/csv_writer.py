import csv

class CSVWriter:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CSVWriter, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def write_csv(self, file_name, headers, rows):
        with open(file_name, "w", newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(headers)
            writer.writerows(rows)