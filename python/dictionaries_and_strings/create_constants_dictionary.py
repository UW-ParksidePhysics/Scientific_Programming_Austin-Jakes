import numpy as numpy



#constants.txt
#parse_constants_file
def parse_constants_file():
    infile = open('/work/Scientific_Programming_Austin_Jakes/python/dictionaries_and_strings/constants.txt', 'r')
    infile.readline()
    constants = {}
    
    for line in infile:
        words = line.split()
        print(words)
        #constants.append(words[0])
    infile.close()

if __name__ == '__main__':
    parse_constants_file()
