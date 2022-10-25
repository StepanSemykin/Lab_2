import csv

class Iterator:
    def __init__(self, directory: str, name: str):
        self.directory = directory
        self.name = name
        self.count = 0
        self.path = []
        with open(directory, "r", encoding = "utf-8") as f:
            r = csv.DictReader(f, fieldnames=["Absolut_path", "Relative_patch", "Class"], delimiter="|")
            
   
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < len(self.list):
            self.counter += 1
            return self.list[self.counter][0]

        elif self.counter == len(self.list):
            raise StopIteration