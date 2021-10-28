from Data import Data

data = Data()
averageECN = 0
averageECSUM = [0,0,0]

def __averageADD__(value, sensorVal):
    global averageECN
    global averageECSUM
    averageECN += 1
    return averageECSUM[sensorVal] += value

def __averageGET__(sensorVal):
    return averageECSUM[sensorVal] /  value


while(True):




