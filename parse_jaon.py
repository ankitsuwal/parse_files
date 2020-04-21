# Python code to illustrate parsing of XML files TanmayBhat, Khalidjamonday(carryminaty) 
# importing the required modules and lib 
import sys
import csv 
import requests 
import xml.etree.ElementTree as ET 
import json

def save_to_txt(items, filename): 
    # writing to txt file
    # opening file in write mode
    path_textfile = "/home/dell/work/projects/parse_data/text_files/json/"
    with open(path_textfile + filename + ".txt", 'w') as file: 
        for value in items:
            if not isinstance(value, list):
                file.write(value + " ")
            else:
                for val in value:
                    file.write(str(val) + " ")
                file.write("\n")

def parseJSON(jsonfile):
    # Opening JSON file
    path_datafile = "/home/dell/work/projects/parse_data/data_files/json/" 
    file = open(path_datafile + jsonfile) 
    # returns JSON object as a dictionary 
    data = json.load(file)
    items = []
    len_recrd, records = len(data['shapes']), data['shapes'] 
    for record in records:
        items.append(record['label'])
        points_x, points_y = [], []
        for i, point in enumerate(record['points']):
            points_x.append(point[0])
            points_y.append(point[1])
        points_x.sort()
        points_y.sort()
        items.append([int(points_x[0]), int(points_y[0]), int(points_x[-1]), int(points_y[-1])])
    return items


def main():
    file_name = sys.argv[1]
    # parse xml file 
    items = parseJSON(file_name)
    # store items in a text file 
    save_to_txt(items, file_name.split(".")[0]) 
    
if __name__ == "__main__": 
    # calling main function 
    main() 
