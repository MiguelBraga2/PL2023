class Person:
    def __init__(self, age, sex, blood_pressure, cholesterol, heartbeat, has_disease):
        self.age = age
        self.sex = sex
        self.blood_pressure = blood_pressure
        self.cholesterol = cholesterol
        self.heartbeat = heartbeat
        self.has_disease = has_disease

    def __str__(self):
        return f"""Age: {self.age}
Sex: {self.sex}
Blood Pressure: {self.blood_pressure}
Cholesterol: {self.cholesterol}
Heartbeat: {self.heartbeat}
Has Disease? {self.has_disease}"""

    def __repr__(self):
        return f"""Age: {self.age}
Sex: {self.sex}
Blood Pressure: {self.blood_pressure}
Cholesterol: {self.cholesterol}
Heartbeat: {self.heartbeat}
Has Disease? {self.has_disease}"""
