from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:29634' % (username, password))
        self.database = self.client['AAC']

    # Creates collection document if passed an object "dmhunter" "Devdarb 3358!"
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False
            
    # Gets document when passed in a specific key-value pair
    def read(self, criteria):
        if criteria is not None:
            animal = self.database.animals.find(criteria, {"_id":False})
            if animal.count() == 0:
                raise Exception("Sorry, could not find that entry because it does not exist.")
            else:
                return animal
        else:
            raise Exception("Nothing to read, because data parameter is empty")
            
    # Updates document(s) when passed in criteria to find a document and what to update to
    def update(self, criteria, values):
        if criteria is not None:
            updatedAnimal = self.database.animals.update(criteria, values)
            return updatedAnimal
        else:
            raise Exception("Nothing to read, because data parameter is empty")
            
    # Deletes document(s) when passed a specific key-value pair
    def delete(self, criteria):
        if criteria is not None:
            deletedAnimal = self.database.animals.remove(criteria)
            if deletedAnimal['n'] == 0:
                raise Exception("Sorry, could not delete that entry because it does not exist.")
            else:
                return deletedAnimal
        else:
            raise Exception("Nothing to read, because data parameter is empty")


