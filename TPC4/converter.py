import re
import statistics
import json
import sys

json_list = [] # JSON list
validators = [] # Regexes used to validate each field
fields = [] # Names of fields

f = open(sys.argv[1], "r") # Open file and reading
lines = list(f.readlines())

matches = re.finditer(r"(\w+)(?:\{(\d+)(?:,(\d+))?})?(?:::)?(\w+)?", lines[0]) # Regexing first line

for match in matches:
    # Group 1: Name
    # Group 2: Size / min_size
    # Group 3: max_size 
    # Group 4: modifiers
    
    fields.append(match.group(1)) # Add the name of the field

    if (match.group(2)!= None): # Validator for lists
        raw_string = r""
        for i in range(0, int(match.group(2))):
                raw_string += r",(\d+)"
        
        if (match.group(3) != None):
            for i in range(int(match.group(2)), int(match.group(3))):
                raw_string += r",(\d+)?"

        if (match.group(4)!= None):
            validators.append((raw_string, match.group(4)))
        else:
            validators.append((raw_string,None))
    else: # Validator for simple field 
        validators.append((r"([\w ]+)", None))

for line in lines[1:]:
    size = len(fields)
    
    obj = {}
    for i,(validator,mod) in enumerate(validators):
        if validator != r"([\w ]+)": # Lista
            splits = re.split(validator, line, 1)
            line = splits[-1]
            l = []
            for s in splits[1:len(splits)-1]:
                if s is not None:
                    l.append(int(s))

            if mod == 'media':
                value = statistics.mean(l)
            elif mod == 'sum':
                value = sum(l)
            elif mod == 'min':
                value = min(l)
            elif mod =='max':
                value = max(l)
            elif mod == None:
                value = l

            obj[fields[i]] = value
        else:
            splits = re.split(r"([\w ]+)", line, 1)
            line = splits[2]
            obj[fields[i]] = splits[1]

    if line == "\n" or line == "": # If there is nothing to read line is valid
        json_list.append(obj)

json.dump(json_list, open(sys.argv[1][:-3] + ".json", "w"), indent=4, ensure_ascii=False)
    

