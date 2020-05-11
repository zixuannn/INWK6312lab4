import os

ans = []


def searchMP3(dirname, res):
    for name in os.listdir(dirname):
        pa = os.path.join(dirname, name)
        if os.path.isfile(pa):
            if name[-4:] == ".mp3":
                res.append(str(pa))
        else:
            searchMP3(pa, res)


searchMP3("Your_Absolute_Path", ans)

for i in ans:
    print(i)

