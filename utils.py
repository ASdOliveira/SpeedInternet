def toMegaBytes(valueInBytes):
    temp = valueInBytes / 1000000
    valueInMegaByte = formatIntoTwoDigits(temp)
    return valueInMegaByte


def formatIntoTwoDigits(value):
    return float("{:.2f}".format(value))
