import os
from glob import glob
import re
import sys
 
def get_valid_filename(s):
    # https://github.com/django/django/blob/master/django/utils/text.py#L218
    s = str(s).strip().replace('/', '_')
    s = str(s).strip().replace(' ', '_')
    s = re.sub(r'(?u)[^-\w.]', '', s)
    return s
 
 
if len(sys.argv) < 2:
    print("Please supply a root path.")
    quit()
 
path = sys.argv[1]
 
if not os.path.isdir(path):
    print("Supplier root path does not seem to exist.")
    quit()
 
print("Make sure you have backed your data up before running this. Do you want to proceed? y/n")
if input().lower() == "y":
    print("Moving all the things.")
else:
    print("Exiting.")
    quit()
 
results = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.*'))]
 
for result in results:
    newpath = get_valid_filename(result)
    os.rename(result, newpath)