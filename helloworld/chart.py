# make charts

import webbrowser

chart_url = "http://chart.apis.google.com/chart?"

def piechart(data, labels):
    url = (chart_url +
            "cht=p3&chd=t:" +
            data +
            "&chs=250x100&chl=" + labels)
    return url

# print piechart("60,40", "charles|Martin")

# percent = ["40", "30", "20", "10"]
# activities = ["Python", "Food", "Sleep", "Singing"]

def linechart(data, low = 0, high = 100):
    url = (chart_url +
           "cht=lc&chd=t:" +
           data +
           "&chds=" + str(low) + "," + str(high) +
           "&chs=250x100")
    webbrowser.open(url)
    return url
           

def chart_activities(percents, activities):
    data = ",".join(percents)
    labels = "|".join(activities)
    return piechart(data, labels)

#time = [
 #   ("40", "Python"),
  #  ("30", "Food"),
   # ("20", "Sleep"),
    #("10", "Singing")
    #]

# chart_activities(percent, activities)

def joinString(time):
    percents = []
    activies = []
    
    for a,b in time:
        percents.append(a)
        activities.append(b)

    data = ",".join(percents)
    labels = "|".join(activities)
    piechart(data, labels)


# print joinString(time)

def chart_time(time):
    percents = [x[0] for x in time]
    activities = [x[1] for x in time]
    return chart_activities(percent, activities)

# print chart_time(time)

def dictionary_chart(diction):
    data = [str(x) for x in diction.values()]
    labels = diction.keys()
    return chart_activities(data, labels)
    
    
        
    
