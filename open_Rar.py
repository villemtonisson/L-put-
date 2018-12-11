##Vaja installida rarfile
##repos on unrar.exe kaasas, seda on samuti vaja
import rarfile
rarfile.UNRAR_TOOL = "unrar.exe"

with rarfile.RarFile('pakk.rar') as rf:
    print(rf.namelist())
    rf.extract('2016-10-02_13-31-39_0.txt')