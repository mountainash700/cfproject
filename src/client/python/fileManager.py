import dataManager
import shutil

class fileManager():
    def __init__(self, dataManager):
        return

    #fetches file over ftp
    def fetch(fileName):
        return

    #reads in file with dataManager.fileName
    #stores file in dataManager.fileData
    def read():
        with open(dataManager.fileName, 'r') as file:
            dataManager.fileData = file.read()
        return

    #writes data from dataManager.fileData to correct file location
    #which file location?
    def write(path):
        with open(path, 'w') as file:
            file.write(dataManager.fileData)
        return

    #for file management
    def move(currentFilePath, destinationFilePath):
        shutil.move(currentFilePath, destinationFilePath)
        return

    #logs file corrections and faults
    #need to add log file location
    def log(message, string):
        with open(wherelogfile, 'a') as file:
            file.write(message)
        return