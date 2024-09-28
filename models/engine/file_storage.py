#!/usr/bin/python3


import json

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    @property
    def objects(self):
        return self.__objects

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, file_path):
        self.__file_path = file_path

    @objects.setter
    def objects(self, objects):
        self.__objects = objects

    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        key = type(obj).__name__ 
        key = key + obj.id
        self.__objects.update({key: str(obj) })
 
    def save(self):
        json_string = json.dumps(self.objects)
        try: 
            json_file = open(self.file_path, "w") 
            json_file.write(json_string)
        except FileNotFoundError:
            pass
  
    def reload(self):
        try: 
            json_file = open(self.file_path, "r") 
            json_string = json_file.read(json_string)
            self.objects = json.loads(data)
        except FileNotFoundError:
            return {}
