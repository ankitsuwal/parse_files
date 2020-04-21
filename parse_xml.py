# Python code to illustrate parsing of XML files TanmayBhat, Khalidjamonday(carryminaty) 
# importing the required modules and lib 
import sys
import csv 
import requests 
import xml.etree.ElementTree as ET 


def parseXML(xmlfile): 
    # create element tree object 
    tree = ET.parse(xmlfile) 
    # get root element  
    root = tree.getroot() 
    # create empty list for items 
    items = [] 
    # iterate items 
    for item in root.iter("annotation"): 
        # iterate child elements of item 
        for child in item: 
            if child.tag == "object":
                for vals in child:
                    if vals.tag == 'name':
                        item = vals.text
                        items.append(item)
                    elif vals.tag == 'bndbox':
                        bbox = []
                        for val in vals:
                            bbox.append(val.text)
                        items.append(bbox)
    # return items list 
    print(">>>: ", items)
    return items 

def save_to_txt(items, filename): 
    # writing to txt file
    # opening file in write mode
    with open(filename + ".txt", 'w') as file: 
        for value in items:
            if not isinstance(value, list):
                file.write(value + " ")
            else:
                for val in value:
                    file.write(val + " ")
                file.write("\n")


def main():
    file_name = sys.argv[1]
    # parse xml file 
    items = parseXML(file_name) 
    # store items in a text file 
    save_to_txt(items, file_name.split(".")[0]) 
    
if __name__ == "__main__": 
    # calling main function 
    main() 
