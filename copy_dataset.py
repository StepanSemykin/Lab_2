import csv
import os
import shutil
import tqdm

def directory(c_directory: str):
    if not os.path.isdir(c_directory):
        os.makedirs(c_directory)

def copy_dataset(directory_obj: str, c_directory_obj: str, name: str):
    data = os.listdir(directory_obj)
    for i in tqdm.tqdm(data):
        shutil.copy(directory_obj + "\\" + i, c_directory_obj + "\\"+ name + "_" + i)
   
def write_csv_copy(directory_obj: str, start: str, name: str):
    file = "copy_patch.csv"
    f = open(file, "a", encoding = "utf-8", newline = "")
    f_writer = csv.DictWriter(f, fieldnames = ["Absolut_path", "Relative_patch", "Class"], delimiter = "|")
    
    data = os.listdir(directory_obj)
    r_directory_obj = os.path.relpath(directory_obj, start)
    
    for i in data:
        f_writer.writerow({"Absolut_path": directory_obj + "\\" + i, "Relative_patch":  r_directory_obj + "\\" + i, "Class": name})   

def main():
  c_directory =  "D:\Lab Python\Lab_2\dataset2"   
  directory_rose = "D:\VS Code project\Images.py\dataset\ rose"
  directory_tulip = "D:\VS Code project\Images.py\dataset\ tulip"  
  start = "D:\Lab Python\Lab_2\\"
  
  directory(c_directory)
  copy_dataset(directory_rose, c_directory, "rose")
  write_csv_copy(c_directory, start, "rose")
  
  copy_dataset(directory_tulip, c_directory, "tulip")
  write_csv_copy(c_directory, start, "tulip")
   
if __name__ == "__main__":
	main()  