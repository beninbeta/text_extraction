#imprt json and os libraries
import json
import os
#function to get files in dircetory that end in .json
#then call a function to extract text atoms
#@params none
def get_files():
    directory = input("What directory: ")
    for file in os.listdir(directory):
        if file.endswith(".json"):
            grab_text(file)
 #create function to extract only the text atoms from our files
 #@params file {string} filename to open and extract text from     
def grab_text(file):
    #Open a new file to write the text to when finshed 
    #and open the json file in read mode and load it 
    
    with open(file, 'r') as json_file:
        data = json.load(json_file)
    #store concepts instantiate the counters for atoms and text atoms
    course_title = data['title']
    f = open(f"{course_title}.txt", "a+")
    concepts = data['concepts']
    
    total_counter = 0
    text_counter = 0
    #loop through the lists in the json object to get to the text atoms
    for i in range(len(concepts)):
        atoms = concepts[i]['atoms']
        for j in range(len(atoms)):
            #need try/expect because not every concept has a text atom
            try:
                text = atoms[j]['text']
                concept = concepts[i]
                f.write(f"Concept title: {concept['title']}\n Concept Id: {concept['id']}\nAtom Text: {text}")
                text_counter += 1
                total_counter += 1
            except KeyError:
                f.write("There were was no text atom in this concept\n")
                total_counter += 1
    #write a final line into the txt file with stats close out the files
    f.write(f"\nThere were {text_counter} text atoms out of {total_counter} atoms in the file.")    
    f.close()
    json_file.close()
    print("Successful run")


if __name__ == "__main__":
    get_files()
    pass 