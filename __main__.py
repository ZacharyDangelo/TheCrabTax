from flask import Flask
from flask import render_template, redirect, make_response
import csv
import time

app = Flask('hello')
dataFilePath = "Z:\Dev\RS_GE\data\data.txt"


#For any route that is not defined, redirect the user to the home page.
@app.errorhandler(404)
def not_found(e):
    return home()

@app.route("/")
def home():
    dataDict = getData()
    return render_template('Home.html',data=dataDict)

@app.route("/about")
def about():
    return render_template('About.html')



def getData():
    dataDict = dict()
    fileData = list()
    targetAmount = 0

    #Read data file.
    with open(dataFilePath, 'r') as f:
        for line in f.readlines()[1:]: #Skip first line of the data file as it contains headers.
            fileData.append(line)
            targetAmount += int(line.split(":")[0])

    todays_data = fileData[-1]
    yesterdays_data = fileData[-2]
    startingAmount = targetAmount - int(todays_data.split(":")[0])
    dataDict["targetAmount"] = targetAmount
    dataDict["secondsUntilUpdate"] = int(todays_data.split(":")[1]) - round(time.time() - 86400) #There are 86400 seconds in a day.
    accumulatedChange = int(todays_data.split(":")[0]) * (1 - dataDict["secondsUntilUpdate"]/86400)
    startingAmount = startingAmount + accumulatedChange
    changePerSecond = (targetAmount - startingAmount - accumulatedChange)/dataDict["secondsUntilUpdate"]

    dataDict["startingAmount"] = startingAmount
    dataDict["accumulatedChange"] = accumulatedChange
    dataDict["changePerSecond"] = changePerSecond
    return dataDict

if __name__ == "__main__":
    app.debug = True
    app.run()

