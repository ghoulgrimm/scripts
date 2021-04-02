import os
from pathlib import Path
import shutil

dateien = {
    'Bilder' : ['jpg', 'jpeg', 'png', 'tif', 'tiff', 'gif', 'ai', 'psd', 'svg', 'bmp', 'ps', 'ico'],
    'Audio' : ['aif', 'cda', 'mid', 'midi', 'mp3', 'mpa', 'ogg', 'wav', 'wma', 'wpl'],
    'Dokumente' : ['pdf', 'odt', 'doc', 'docx', 'txt', 'wpd'],
    'Videos' : ['3g2', '3gp', 'avi', 'flv', 'h264', 'm4v', 'mkv', 'mov', 'mp4', 'mpg', 'mpeg', 'rm', 'swf', 'vob', 'wmv'],
    'Praesentationen' : ['key', 'odp', 'pps', 'ppt', 'pptx', 'xps', 'pot', 'pptm', 'ppsx', 'ppsm'],
    'Tabellen' : ['ods', 'xls', 'xlsm', 'xlsx'],
    'Emails' : ['email', 'eml', 'emlx', 'msg', 'oft', 'ost', 'pst', 'vcf']
}

drives = ['C:\\', 'D:\\']
output_folder = 'BKPR-Output'
dir_path = os.path.dirname(os.path.realpath(__file__))

# Ordner anlegen
def create_folders():
    for key in dateien.keys():
        Path(drives[0] + "\\" + output_folder + "\\" + key ).mkdir(parents = True, exist_ok = True)
        

def walking():
    # OS-Walking
    for drive in drives:
        for root, dirs, files in os.walk(drive):
            for filename in files:
                extension = filename.rpartition('.')[2]
                for key in dateien.keys():
                    for value in dateien[key]:
                        origin = root + "\\" + filename
                        destination = drives[0] + output_folder + "\\" + key 
                        if extension == value and origin != (destination + "\\" + filename):
                            try:
                                shutil.copy2(origin, destination)
                                print("copied "+ origin + "to" + destination)
                            except:
                                pass
                            


create_folders()
walking()
