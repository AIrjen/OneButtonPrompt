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

def csv_to_list(csvfilename, antilist=[], directory="./csvfiles/", lowerandstrip=0, delimiter=";", listoflistmode = False, skipheader = False, gender = "all", insanitylevel = -1):
        replacing = False
        userfilesdirectory = "./userfiles/"
        userfileaddonname = csvfilename + "_addon.csv"
        userfilereplacename = csvfilename + "_replace.csv"
        lightfilename = csvfilename + "_light.csv"
        mediumfilename = csvfilename + "_medium.csv"
        csvlist = []
        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(script_dir, directory )
        userfilesfolder = os.path.join(script_dir, userfilesdirectory )
        directoryfilesfolder = os.path.join(script_dir, directory )
        
        # check if there is a replace file
        if(directory=="./csvfiles/" or directory=="./csvfiles/special_lists/" or directory=="./csvfiles/templates/"):      
                for filename in os.listdir(userfilesfolder):
                        if(filename == userfilereplacename):
                                # Just override the parameters, and let it run normally
                                full_path = os.path.join(script_dir, userfilesdirectory )
                                csvfilename = csvfilename + "_replace"
                                replacing = True


                # Go check for light or medium files if there is no override and there is an insanitylevel
                if(replacing == False and insanitylevel > 0):
                        if(insanitylevel < 4):   
                                for filename in os.listdir(directoryfilesfolder):
                                        if(filename == mediumfilename):
                                                # Just override the parameters, and let it run normally
                                                full_path = os.path.join(script_dir, directory )
                                                csvfilename = csvfilename + "_light"
                                                replacing = True
                        # under 7, than only SOMETIMES take the full list
                        if(insanitylevel < 7 and random.randint(0,13) < 12 and replacing == False):   
                                for filename in os.listdir(directoryfilesfolder):
                                        if(filename == lightfilename):
                                                # Just override the parameters, and let it run normally
                                                full_path = os.path.join(script_dir, directory )
                                                csvfilename = csvfilename + "_medium"
                                                replacing = True
                        
                        

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
                                                gender != "all" and (row[1] == gender or row[1] == "genderless" or row[1] == "both")
                                                or gender == "all"
                                                ):
                                                if(value.lower().strip() not in antilist):
                                                        if(lowerandstrip == 1):
                                                                csvlist.append(row[0].lower().strip())        
                                                        else:
                                                                csvlist.append(row[0])
        # dirty hack for possible .txt files
        if(os.path.isfile(full_path + csvfilename + ".txt")):
                with open(full_path + csvfilename + ".txt", "r", newline="",encoding="utf8") as file:
                        reader = csv.reader(file, delimiter=delimiter)
                        if(skipheader==True):
                                next(reader)
                        if(listoflistmode==True):
                                csvlist = list(reader)
                        else:
                                for row in reader:
                                        value = row[0]
                                        if( 
                                                gender != "all" and (row[1] == gender or row[1] == "genderless" or row[1] == "both")
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
                                reader = csv.reader(file, delimiter=delimiter)
                                if(skipheader==True):
                                        next(reader)
                                if(listoflistmode==True):
                                        csvlist.append(list(reader))
                                else:
                                        for row in reader:
                                                value = row[0]
                                                if( 
                                                gender != "all" and (row[1] == gender or row[1] == "genderless" or row[1] == "both")
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

def artist_category_by_category_csv_to_list(csvfilename,artist):
        csvlist = []
        mediumlist = []
        descriptionlist = []
        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(script_dir, "./csvfiles/" )
        with open(full_path + csvfilename + ".csv", "r", newline="",encoding="utf8") as file:
                reader = csv.DictReader(file, delimiter=",")
                for row in reader:
                        if(row["Artist"] == artist):
                                csvlist.append(row["Tags"])
                                mediumlist.append(row["Medium"])
                                descriptionlist.append(row["Description"])
        return csvlist, mediumlist, descriptionlist

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

def artist_descriptions_csv_to_list(csvfilename):
        csvlist = []
        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(script_dir, "./csvfiles/" )
        with open(full_path + csvfilename + ".csv", "r", newline="",encoding="utf8") as file:
                reader = csv.DictReader(file, delimiter=",")
                for row in reader:
                        csvlist.append(row["Description"])
        return csvlist

def load_config_csv(suffix=""):
        csvlist = []
        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path_config_file = os.path.join(script_dir, "./userfiles/" )
        full_path_default_config_file = os.path.join(script_dir, "./csvfiles/config/" )
        if(suffix != ""):
                config_file = full_path_config_file + 'config_' + suffix + '.csv'
                default_config_file = full_path_default_config_file + 'default_config_' + suffix + '.csv'
        else:
                config_file = full_path_config_file + 'config.csv'
                default_config_file = full_path_default_config_file + 'default_config.csv'

        if not os.path.exists(config_file):
                shutil.copy2(default_config_file, config_file)
                print("Config file created.")


        with open(config_file, "r", newline="",encoding="utf8") as file:
                reader = csv.DictReader(file, delimiter=";")
                csvlist = [list(row.values()) for row in reader if not any(value.startswith('#') for value in row.values())]
        return csvlist

def load_negative_list():
        primerlist = []
        negativelist = []
        primeraddonlist = []
        negativeaddonlist = []

        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        full_path_default_negative_file = os.path.join(script_dir, "./csvfiles/special_lists/" )
        negative_file = full_path_default_negative_file + 'negativewords.csv'

        full_path_replace_negative_file = os.path.join(script_dir, "./userfiles/" )
        replace_negative_file = full_path_replace_negative_file + 'negativewords_replace.csv'

        full_path_addon_negative_file = os.path.join(script_dir, "./userfiles/" )
        addon_negative_file = full_path_addon_negative_file + 'negativewords_addon.csv'


        if(os.path.isfile(replace_negative_file)):
                negative_file = replace_negative_file

        with open(negative_file, "r", newline="",encoding="utf8") as file:
                reader = csv.DictReader(file, delimiter=";")
                primerlist = [row["primer"] for row in reader]
        with open(negative_file, "r", newline="",encoding="utf8") as file:
                reader = csv.DictReader(file, delimiter=";")
                negativelist = [row["negative"] for row in reader]


        if(os.path.isfile(addon_negative_file)):
                with open(addon_negative_file, "r", newline="",encoding="utf8") as file:
                        reader = csv.DictReader(file, delimiter=";")
                        primeraddonlist = [row["primer"] for row in reader]
                with open(addon_negative_file, "r", newline="",encoding="utf8") as file:
                        reader = csv.DictReader(file, delimiter=";")
                        negativeaddonlist = [row["negative"] for row in reader]
        
        primerlist += primeraddonlist
        negativelist += negativeaddonlist


        return primerlist, negativelist

def load_all_artist_and_category():
        artistlist = []
        categorylist = []
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        full_path_default_artist_file = os.path.join(script_dir, "./csvfiles/" )
        artist_file = full_path_default_artist_file + 'artists_and_category.csv'

        with open(artist_file, "r", newline="",encoding="utf8") as file:
                reader = csv.DictReader(file, delimiter=",")
                artistlist = [row["Artist"] for row in reader]
        with open(artist_file, "r", newline="",encoding="utf8") as file:
                reader = csv.DictReader(file, delimiter=",")
                categorylist = [row["Tags"] for row in reader]

        return artistlist, categorylist

def sort_and_dedupe_csv_file():
        tokenlist = csv_to_list(csvfilename="tokens",skipheader=False)
        tokenlist = sorted(set(tokenlist))
        newlist = []
        for i in tokenlist:
                j = i.lower()
                result = all(c == i[0] for c in i)
                if result:
                        print("String {} have all characters same".format(i))
                else:
                        newlist.append(j)
        
        
        newlist = sorted(set(newlist))

        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        full_path = os.path.join(script_dir, "./csvfiles/special_lists/tokenwriter.csv" )
        with open(full_path, 'w', encoding="utf8") as fp:
                for item in newlist:
                        # write each item on a new line
                        fp.write("%s\n" % item)


# sort_and_dedupe_csv_file()

