#import the pandas for accessing the datafile
import pandas as pd
#import sweetviz for analyzing the data
import sweetviz as sv


def getFile(fileName):
    """
    function to access the data file using pandas
    Args:
        fileName: file path
    Use this only when you don't need to view the data before analyzing   
    """
    f1=pd.read_csv(fileName)

    return analyzeData(f1)

def showData(fileName):
    """
    function to access the data file using pandas and show the data on the shell
    Args:
        fileName: file path
    Use this to be able to view data before analyzing 
    """
    f1=pd.read_csv(fileName)

    return analyzeData(f1)


def analyzeData(data):
    """
    function to analyze the data accessed and display using sweetviz
    Args:
        data: data that has been retrieved/accessed by the pandas
    """
    #analyze
    f1_report=sv.analyze(data)
    #display
    f1_report.show_html("Report.html")



