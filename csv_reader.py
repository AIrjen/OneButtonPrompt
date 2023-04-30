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

def csv_to_list(csvfilename, antilist=[], directory="./csvfiles/", lowerandstrip=0):
        csvlist = []
        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(script_dir, directory )
        # return empty list if we can't find the file. Build for antilist.csv
        if(os.path.isfile(full_path + csvfilename + ".csv")):
                with open(full_path + csvfilename + ".csv", "r", newline="",encoding="utf8") as file:
                        reader = csv.reader(file, delimiter=",")
                        for row in reader:
                                value = row[0]
                                if(value.lower().strip() not in antilist):
                                        if(lowerandstrip == 1):
                                                csvlist.append(row[0].lower().strip())        
                                        csvlist.append(row[0])
        return csvlist

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


