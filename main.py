"""Boot-strapping module to create the application and ask it to run"""

from application import Application

try:
    #create the application object
    app = Application()

    #ask the application to run
    app.run()
except Exception as ex:
    print(f"An unknown eror has occourred.\nMessage: {ex}")

