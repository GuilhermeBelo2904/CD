from Utils import show_symbols_info, write_sequence_to_file, delete_file
import random
import os 

class fontAssociatedWithRange:
    def __init__(self, simbolList, showInfo = False):
        total = len(simbolList)
        self.total = total
        if showInfo:
            currDir = os.getcwd()
            makeSequence = ''
            for simbol in simbolList:
                makeSequence += simbol
            fileName = "temp"+ str(random.randint(0, 1000)) + ".txt"

            write_sequence_to_file(fileName, makeSequence)
            show_symbols_info(fileName, currDir)
            delete_file(fileName)
        self.simbolList = {}
        listToCount = []
        for simbol in simbolList:
            if (simbol not in listToCount):
                listToCount.append(simbol)
        prop = 100
        for simbol in listToCount:
            number = 0
            for simbol2 in simbolList:
                if simbol == simbol2:
                    number += 1
            itemProb = (number/total)*100
            initRange = prop - itemProb
            self.simbolList[simbol] = Pair(initRange, prop-0.01)
            prop = initRange
        prop = initRange

    def getSimbolByRange(self, range):
        range = round(range * 100, 2)
        for simbol in self.simbolList:
            pair = self.simbolList[simbol]
            if range >= pair.begin and range <= pair.end:
                return simbol
        return None
    
    def getRangeBySimbol(self, simbol):
        return self.simbolList[simbol]
    
    def getSimbolList(self):
        return self.simbolList
    
    def __str__(self):
        return str(self.simbolList)



class Pair:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def __str__(self):
        return f"({self.begin}, {self.end})"