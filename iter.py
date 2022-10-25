import csv

class Iterator:
    def __init__(self, directory: str, name: str):
        """Сonstructor of the class object, return NONE.
        Args:
            directory (str): full path to the folder.
            name (str): object classs.
        """
        self.directory = directory
        self.name = name
        self.count = -1
        self.read_list = []
        
        with open(directory, "r", encoding = "utf-8") as f:
            r = csv.DictReader(f, fieldnames=["Absolut_path", "Relative_patch", "Class"], delimiter="|")
            
            for i in r:
                if i["Class"] == name:
                    self.read_list.append(i["Absolut_path"])   

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < len(self.read_list):
            self.count += 1
            return self.read_list[self.count]

        elif self.count == len(self.read_list):
            raise StopIteration
       
def main():
    s = Iterator("D:\Lab Python\Lab_2\copy_patch.csv", "rose")     

    print(next(s))
    print(next(s))
    print(next(s))        
    
    t = Iterator("D:\Lab Python\Lab_2\copy_patch.csv", "tulip") 
    
    print(next(t))
    print(next(t))
    print(next(t))  
    

if __name__ == "__main__":
	main()
