from os import rename, listdir
badprefix = "CUsersLLL-DEVSPAREDocumentsAndroidStudioProjectsandroidmobile-uisrcmainassetssvg"
fnames = listdir('.')
for fname in fnames:
    if fname.startswith(badprefix*2):
        rename(fname, fname.replace(badprefix, '', 1))