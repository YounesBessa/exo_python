import json

# Person class
class Person:
    def __init__(self, last_name, first_name, age, date_of_birth, gender):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.date_of_birth = date_of_birth
        self.gender = gender

# to_dict method
    def to_dict(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "age": self.age,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender
        }

# Main function to test the class Person
if __name__ == "__main__":
    person = Person("BESSA", "Younes", 24, "1998-07-08", "Male")
    person_dict = person.to_dict()
    person_json = json.dumps(person_dict)
    print(person_json)