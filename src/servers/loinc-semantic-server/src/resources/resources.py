import os
import csv

class Resources:
    def __init__(self):
        # Path to the data file inside resources/data
        self.loinc_file = os.path.join(os.path.dirname(__file__), 'data', 'loinc_ontology.csv')
        self.loinc_data = []
        self.loinc_columns = []
        self._load_loinc_data()

    def _load_loinc_data(self):
        if os.path.exists(self.loinc_file):
            with open(self.loinc_file, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                self.loinc_columns = reader.fieldnames
                for row in reader:
                    self.loinc_data.append(row)
        else:
            print(f"LOINC ontology file not found at {self.loinc_file}")
