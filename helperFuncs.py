import pickle
import sys


def printObj(object):
    for item in object:
        print(item)

def printDict(dict):
    for key, value in dict:
        print(f"{key}, {value}")

def printMultObj(object, object2):
    i = 0
    for item in object:
        print(item + ": " + object2[i])


def unpickle_object(filename):
    try:
        object = pickle.load(filename)
    except:
        e = sys.exc_info()[0]
        print(e)
    else:
        return object


def save_object(object):  # saves a static object of any kind as a .obj
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


def generic_freq(obj_to_count, what_is_counted): #what_is_counted is a string
    obj_freq = dict()

    for item in obj_to_count:
        if item in obj_freq:
            obj_freq[item] += 1
        else:
            obj_freq[item] = 1

    for key, value in obj_freq.items():
        print(f"{what_is_counted} {key} shows up {value} times.")

    return obj_freq