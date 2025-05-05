import os 
import glob 

pattern = "*_lines.txt"
#glob.glob("*_lines.txt") find all the files with a specified name in current dir
files = glob.glob(pattern)

if not files:
    print("There is no files to delete")
else:
    for file in files:
        try:
            os.remove(file)
            print(f"Removed {file}")
        except Exception as e:
            print(f"Error occured while removing {file}: {e}")

