"""
os.path learned from GeeksforGeeks.com
URL: https://www.geeksforgeeks.org/os-path-module-python/
Date: May 11, 2020
Author: GeeksforGeeks.com

MD5 Checksum learned from Stackoverflow.com
URL: https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
Date: May 11, 2020
Author: Stackoverflow.com
"""

import os
import hashlib

ans = []
files = {}
res = []

def searchMP3(dirname, res):
    for name in os.listdir(dirname):
        pa = os.path.join(dirname, name)
        if os.path.isfile(pa):
            if name[-4:] == ".mp3":
                res.append(str(pa))
        else:
            searchMP3(pa, res)

def check_duplicates(ans):
	for i in ans:
		checksum = hashlib.md5(open(i, "br").read()).hexdigest()   # use hashlib.md5 compute checksum for each file
		if files.get(checksum) is None:    # use dictionary to record, key = checksum, value = path
			files[checksum] = [i]
		else:
			files[checksum].append(i)
	for k,v in files.items():
		if len(v) > 1:
			res.append(v)
	return res



searchMP3("your_absolute_path", ans)

#for i in ans:
#    print(i)

result = check_duplicates(ans)
for i in result:
	for j in i:
		print(j)
	print()



