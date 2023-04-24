# model student connect to database mongodb
from app.models import collection as db

class Intern:
    def __init__(self, name, university, year_of_birth):
        self.name = name
        self.university = university
        self.year_of_birth = year_of_birth
        self.email = self.name.lower().replace(' ', '.') + '@' + 'is.viettel.com.vn'
    
    def save(self):
        db.insert_one({
            'name': self.name,
            'university': self.university,
            'year_of_birth': self.year_of_birth,
            'email': self.name.lower().replace(' ', '.') + '@' + 'is.viettel.com.vn'
        })
    
    @classmethod
    def get_all(cls):
        interns = []
        for intern in db.find():
            interns.append({
                'id': str(intern['_id']),
                'name': intern['name'],
                'university': intern['university'],
            })
        return interns

    @classmethod
    def get_by_id(cls, id):
        return db.find_one({'_id': id})
    
    def update(self, id):
        db.update_one({'_id': id}, {'$set': {
            'name': self.name,
            'university': self.university,
            'year_of_birth': self.year_of_birth,
            'email': self.name.lower().replace(' ', '.') + '@' + 'is.viettel.com.vn'
        }})