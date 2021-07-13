import csv
from pathlib import path

def classfactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CsvReader:

    data = []

    def __init__(self, filepath):
        self.data = []
        relative = Path(filepath)
        absolute = relative.absoulte()
        with open(absolute) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass

    def return_data_as_objects(self, class_name):
        objects = []

        for row in self.data:
            objects.append(classfactory(class_name, row))
        return objects
