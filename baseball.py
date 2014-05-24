# baseball

import chart

def getdata(filename):
    """return header and data frrom the file"""
    everything = [
        line.strip().split(',')
        for line in file(filename)]
    return (everything[0], everything[1:])
        
def getstat(data, name):
    """return a list of the stat from the data"""
    header, stats = data
    position = header.index(name)
    return [line[position] for line in stats]

def getchart(data, name):
    """return a piechart url laveled with years"""
    amounts = getstart(data, name)
    labels = getstat(data, "Year")

    return chart.chart_activities(amounts, labels)


def getlinechart(data, name, low, high):
    """return a linechart of the statistic"""
    amounts = getstat(data, name)
    # labels = getstat(data, "Year")

    return chart.linechart(','.join(amounts), low, high)
