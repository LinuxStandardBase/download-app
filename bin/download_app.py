#!python

from flask_script import Manager
import downloadapp

manager = Manager(downloadapp.app)
if __name__ == "__main__":
    manager.run()
