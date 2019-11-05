# Python Text Extraction Tool for JSON

## Requirements

- Python 3.7
    - Libraries
        - OS
        - JSON

At work we ran into a situation where we needed to extract specific texts from a
complex set of JSON files. These files had multiple parts of text we needed to pull
from mulitiple parts of the JSON file. Some of these were easily accessible using 
Key: Value pairs. 

Unfortunately there were several objects inside of lists which made
this more difficult. It was futher complicated because sometimes the values we were
looking for were not not part of the file. I also added an error handler to 
make sure the script would run if they value we needed was missing. 

Lastly, I also added the abilit to run from the command line and to specify what directory
you would like to pull the JSON files from. 

The script will grab the values specified by the script and write them to a txt file. If 
there are multiple JSON files it will write multiple txt. One for each file.

I hope you find it useful. 
