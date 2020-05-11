import os
def sed(f1, f2):
	try:
		file1 = open(f1, mode="r")
		file2 = open(f2, mode="w")
		for line in file1:
			file2.write(line)
		file2.close()
		file1.close()
	except Exception:
		print(Exception)
		return
sed("file1.txt", "file2.txt")