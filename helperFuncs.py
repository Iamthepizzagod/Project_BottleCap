import pickle
import sys

def printObj(object):
    for item in object:
        print (item)

def printMultObj(object, object2):
    i = 0
    for item in object:
        print (item + ": " + object2[i])


def unpickle_object(filename):
    try:
        object = pickle.load(filename)
    except:
        e = sys.exc_info()[0]
        print (e)
    else:
        return object

def save_object(object): #saves a static object of any kind as a .obj
    print("What would you like to name the file (extension will always be .obj)? ")
    filename = input()
    filename = str(filename) + ".obj"
    print("file name will be: " + filename)
    try:
        file_packets = open(filename, 'wb')
        pickle.dump(object, file_packets)
    except:
        print("File saving failed.")
    else:
        print(filename + " saved successfully!")


def generic_freq(object):
    objFreq = dict()

    for item in object:
        if item in objFreq:
            objFreq[item] += 1
        else:
            objFreq[item] = 1

    for key, value in objFreq.items():
        print(f"Object '{key}' shows up {value} times.")

    return objFreq