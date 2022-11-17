def mean(sortedList):
    total = 0
    for val in sortedList:
        total = total + val
    total = total / (len(sortedList))
    return total

def median(sortedList):
    index = (len(sortedList) - 1) / 2
    if index % 1 != 0.5:
        return sortedList[int(index)]
    else:
        return (sortedList[int(index-0.5)] + sortedList[int(index+0.5)]) / 2

def medianIndex(sortedList):
    index = (len(sortedList) - 1) / 2
    if index % 1 != 0.5:
        return [index]
    else:
        return [index-0.5, index+0.5]

def lowerQ(sortedList):
    upperBound = medianIndex(sortedList)
    #what if the bound is between indexes?
    return median(sortedList[0:int(upperBound[0])])

def upperQ(sortedList):
    lowerBound = medianIndex(sortedList)
    #what if the bound is between indexes?
    return median(sortedList[int(lowerBound[-1]):])

def Percentiles(sortedList):

    total = sum(sortedList)
    percentileDict = {}

    cumulativePercent = 0

    for key in sortedList:
        cumulativePercent = cumulativePercent + (key/total) * 100
        percentileDict[key] = cumulativePercent

    return percentileDict

print("Prototype A Mean TTC: " + str(mean([18, 19, 20.5, 23, 24.35, 30])))
print("Prototype A Mean ERR: " + str(mean([0, 0, 0, 0, 0, 2])))
print("Prototype A Mean SUS: " + str(mean([70, 75, 75, 77.5, 82.5, 82.5])))

print("Prototype A Median TTC: " + str(median([18, 19, 20.5, 23, 24.35, 30])))
print("Prototype A Median ERR: " + str(median([0, 0, 0, 0, 0, 2])))
print("Prototype A Median SUS: " + str(median([70, 75, 75, 77.5, 82.5, 82.5])))

print("Prototype A Lower Quartile TTC: " + str(lowerQ([18, 19, 20.5, 23, 24.35, 30])))
print("Prototype A Lower Quartile ERR: " + str(lowerQ([0, 0, 0, 0, 0, 2])))
print("Prototype A Lower Quartile SUS: " + str(lowerQ([70, 75, 75, 77.5, 82.5, 82.5])))

print("Prototype A Upper Quartile TTC: " + str(upperQ([18, 19, 20.5, 23, 24.35, 30])))
print("Prototype A Upper Quartile ERR: " + str(upperQ([0, 0, 0, 0, 0, 2])))
print("Prototype A Upper Quartile SUS: " + str(upperQ([70, 75, 75, 77.5, 82.5, 82.5])))

print("Prototype B Mean TTC: " + str(mean([15, 18, 19, 22, 32, 48.14])))
print("Prototype B Mean ERR: " + str(mean([0, 0, 1, 1, 1, 2])))
print("Prototype B Mean SUS: " + str(mean([62.5, 62.5, 67.5, 70, 75, 77.5])))

print("Prototype B Median TTC: " + str(median([15, 18, 19, 22, 32, 48.14])))
print("Prototype B Median ERR: " + str(median([0, 0, 1, 1, 1, 2])))
print("Prototype B Median SUS: " + str(median([62.5, 62.5, 67.5, 70, 75, 77.5])))

print("Prototype B Lower Quartile TTC: " + str(lowerQ([15, 18, 19, 22, 32, 48.14])))
print("Prototype B Lower Quartile ERR: " + str(lowerQ([0, 0, 1, 1, 1, 2])))
print("Prototype B Lower Quartile SUS: " + str(lowerQ([62.5, 62.5, 67.5, 70, 75, 77.5])))

print("Prototype B Upper Quartile TTC: " + str(upperQ([15, 18, 19, 22, 32, 48.14])))
print("Prototype B Upper Quartile ERR: " + str(upperQ([0, 0, 1, 1, 1, 2])))
print("Prototype B Upper Quartile SUS: " + str(upperQ([62.5, 62.5, 67.5, 70, 75, 77.5])))

print("Prototype A Percentile SUS: " + str(Percentiles([70, 75, 75, 77.5, 82.5, 82.5])))
print("Prototype B Percentile SUS: " + str(Percentiles([62.5, 62.5, 67.5, 70, 75, 77.5])))
print("All Prototype Percentile SUS: " + str(Percentiles([62.5, 62.5, 67.5, 70, 70, 75, 75, 75, 77.5, 77.5, 82.5, 82.5])))
print("All Prototype Mean Percentile SUS: " + str(Percentiles([69.1666666666666, 77.0833333333333])))
