from person import Person
import math

class Model:
    def __init__(self):
        self.model = None
        # Auxiliary for distribution
        self.min_cholesterol = math.inf

    def read_file(self, path):
        with open(path) as file:
            file.readline()  # Remove first line
            lines = file.readlines()  # Read all lines

        persons = list()
        # Validate lines and convert to person object
        for line in lines:
            person = validate_line(line)
            if person is not None:
                persons.append(person)

                # Update minimum cholesterol
                if person.cholesterol < self.min_cholesterol:
                    self.min_cholesterol = person.cholesterol

        self.model = persons
        print(self.min_cholesterol)

    def get_ages(self):
        ages = list()
        for person in self.model:
            ages.append(person.age)

        return ages

    def get_cholesterol(self):
        cholesterol = list()

        for person in self.model:
            cholesterol.append(person.cholesterol)

        return cholesterol



def validate_line(line):
    line = line.replace("\n", "")
    line_split = line.split(',')

    if len(line_split) == 6 \
   and line_split[0].isdigit() \
   and validate_genre(line_split[1]) \
   and line_split[2].isdigit() \
   and line_split[3].isdigit() and validate_cholesterol(int(line_split[3])) \
   and line_split[4].isdigit() \
   and line_split[5].isdigit() and int(line_split[5]) == 1:
        return Person(int(line_split[0]),
                      line_split[1],
                      int(line_split[2]),
                      int(line_split[3]),
                      int(line_split[4]),
                      line_split[5])
    else:
        print('Invalid line: ' + line)

def validate_genre(str):
    return str == 'M' or str == 'F'

def validate_cholesterol(cholesterol):
    return cholesterol > 0