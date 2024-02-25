# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    
    with open(datafile, "r") as f:
        header = f.readline().split(",")  #To get the header values
        #print(header)
        count =0
        for line in f:
            if count ==10:
                break
            
            item = line.split(",")
            entry = dict()
            
            
            for i, values in enumerate(item):
                entry[header[i].strip()] = values.strip()
            
            data.append(entry)
            #print(data)
            count+=1 
            
    
    #print(len(data))
    return data
