#!/usr/bin/python3


from datetime import datetime
from uuid import uuid4

class BaseModel: 

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        # [<class name>] (<self.id>) <self.__dict__>
        obj_str = "[{}] ({}) {}"
        return obj_str.format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__
        obj_dict.update({'__class__': type(self).__name__})
        obj_dict.update({'id': self.id})
        obj_dict.update({'created_at': self.created_at})
        obj_dict.update({'updated_at': self.updated_at})
        return self.__dict__

    def to_json(self):
        pass
