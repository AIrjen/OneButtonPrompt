import csv
import random
import os

def random_read_from_csv(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
    full_path = os.path.join(script_dir, "./csvfiles/" )
    with open(full_path + filename + ".csv", "r",encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file)
            output = (random.choice([line[0] for line in csv_reader]))
    return output

def add_from_csv(completeprompt, csvfilename, addcomma, prefix, suffix):
        randomreadfromcsv = random_read_from_csv(csvfilename)
        #print(csvfilename+ ": " + randomreadfromcsv)
        addtoprompt = prefix + " " + randomreadfromcsv + " " + suffix
        if(addcomma == 1):
                return ", ".join([completeprompt,addtoprompt])
        return " ".join([completeprompt,addtoprompt])

def csv_to_list(csvfilename, antilist=[], directory="./csvfiles/", lowerandstrip=0, delimiter=";", listoflistmode = False):
        userfilesdirectory = "./userfiles/"
        userfileaddonname = csvfilename + "_addon.csv"
        userfilereplacename = csvfilename + "_replace.csv"
        csvlist = []
        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(script_dir, directory )
        userfilesfolder = os.path.join(script_dir, userfilesdirectory )
        # check if there is a replace file
        if(directory=="./csvfiles/" or directory=="./csvfiles/special_lists/" or directory=="./csvfiles/templates/"):      
                for filename in os.listdir(userfilesfolder):
                        if(filename == userfilereplacename):
                                # Just override the parameters, and let it run normally
                                full_path = os.path.join(script_dir, userfilesdirectory )
                                csvfilename = csvfilename + "_replace"
                        

        # return empty list if we can't find the file. Build for antilist.csv
        if(os.path.isfile(full_path + csvfilename + ".csv")):
                with open(full_path + csvfilename + ".csv", "r", newline="",encoding="utf8") as file:
                        reader = csv.reader(file, delimiter=delimiter)
                        if(listoflistmode==True):
                                csvlist = list(reader)
                        else:
                                for row in reader:
                                        value = row[0]
                                        if(value.lower().strip() not in antilist):
                                                if(lowerandstrip == 1):
                                                        csvlist.append(row[0].lower().strip())        
                                                csvlist.append(row[0])
                
        # do the add ons!
        if(directory=="./csvfiles/" or directory=="./csvfiles/special_lists/"):
                if(os.path.isfile(userfilesfolder + csvfilename + "_addon" + ".csv")):
                        with open(userfilesfolder + csvfilename + "_addon" + ".csv", "r", newline="",encoding="utf8") as file:
                                reader = csv.reader(file, delimiter=",")
                                if(listoflistmode==True):
                                        csvlist.append(list(reader))
                                else:
                                        for row in reader:
                                                value = row[0]
                                                if(value.lower().strip() not in antilist):
                                                        if(lowerandstrip == 1):
                                                                csvlist.append(row[0].lower().strip())        
                                                        csvlist.append(row[0])


        # remove duplicates, but check only for lowercase stuff
        deduplicated_list = []
        lowercase_elements = set()
        if(listoflistmode==False):
                for element in csvlist:
                        lowercase_element = element.lower()
                        if lowercase_element not in lowercase_elements:
                                lowercase_elements.add(lowercase_element)
                                deduplicated_list.append(element)
        else:
                deduplicated_list = csvlist
        
        return deduplicated_list

def artist_category_csv_to_list(csvfilename,category):
        csvlist = []
        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(script_dir, "./csvfiles/" )
        with open(full_path + csvfilename + ".csv", "r", newline="",encoding="utf8") as file:
                reader = csv.DictReader(file, delimiter=",")
                for row in reader:
                        if(row[category] == "1"):
                                csvlist.append(row["Artist"])
        return csvlist



