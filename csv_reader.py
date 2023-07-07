import csv
import random
import os
import shutil

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

def csv_to_list(csvfilename, antilist=[], directory="./csvfiles/", lowerandstrip=0, delimiter=";", listoflistmode = False, skipheader = False, gender = "all"):
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
                        if(skipheader==True):
                                next(reader)
                        if(listoflistmode==True):
                                csvlist = list(reader)
                        else:
                                for row in reader:
                                        value = row[0]
                                        if( 
                                                (gender != "all" and row[1] == gender)
                                                or gender == "all"
                                                ):
                                                if(value.lower().strip() not in antilist):
                                                        if(lowerandstrip == 1):
                                                                csvlist.append(row[0].lower().strip())        
                                                        else:
                                                                csvlist.append(row[0])
                
        # do the add ons!
        if(directory=="./csvfiles/" or directory=="./csvfiles/special_lists/"):
                if(os.path.isfile(userfilesfolder + csvfilename + "_addon" + ".csv")):
                        with open(userfilesfolder + csvfilename + "_addon" + ".csv", "r", newline="",encoding="utf8") as file:
                                reader = csv.reader(file, delimiter=",")
                                if(skipheader==True):
                                        next(reader)
                                if(listoflistmode==True):
                                        csvlist.append(list(reader))
                                else:
                                        for row in reader:
                                                value = row[0]
                                                if( 
                                                (gender != "all" and row[1] == gender)
                                                or gender == "all"
                                                ):
                                                        if(value.lower().strip() not in antilist):
                                                                if(lowerandstrip == 1):
                                                                        csvlist.append(row[0].lower().strip())        
                                                                else:
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



def load_config_csv():
        csvlist = []
        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path_config_file = os.path.join(script_dir, "./userfiles/" )
        full_path_default_config_file = os.path.join(script_dir, "./csvfiles/config/" )
        config_file = full_path_config_file + 'config.csv'
        default_config_file = full_path_default_config_file + 'default_config.csv'

        if not os.path.exists(config_file):
                shutil.copy2(default_config_file, config_file)
                print("Config file created.")


        with open(config_file, "r", newline="",encoding="utf8") as file:
                reader = csv.DictReader(file, delimiter=";")
                csvlist = [list(row.values()) for row in reader if not any(value.startswith('#') for value in row.values())]
        return csvlist
        