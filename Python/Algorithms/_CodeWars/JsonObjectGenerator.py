import unittest
from datetime import datetime
import json
from pprint import pprint
    
class UserData(dict):
    def __init__(self):
        super(UserData, self).__init__()
            
    
def JsonObjectGenerator(jsonstr):
    jsondata = json.loads(jsonstr)
    print('jsondata', jsondata)
    user = UserData()
    
    def setattributes(user, jsondata, parent=None):
        for key in jsondata.keys():
            if type(jsondata[key]) == dict:
                newobject = UserData()
                setattr(user, key, newobject)
                user[key] = newobject
                setattributes(user, jsondata[key], parent=newobject)
            else:
                if parent == None:
                    parent = user
                setattr(parent, key, jsondata[key])
                parent[key] = jsondata[key]
    setattributes(user, jsondata)
    
    return user

    
class test_Solution(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now()-self.starttime
        print(str(t), self.id())
        
    def test_1(self):
        input = \
'''
{"name": "User1", 
   "fav_language": "python",
   "fav_tech": "kubernetes",
   "favorites": {
        "other_tech1": "unreal",
        "other_tech2": "nuke"
   }
}
'''
        result = JsonObjectGenerator(input)
        
        self.assertEqual(result.name,"User1")
        self.assertEqual(result.fav_language, "python")
        self.assertEqual(result.fav_tech,"kubernetes")
        self.assertEqual(result.favorites.other_tech1,"unreal")
        self.assertEqual(result.favorites.other_tech2,"nuke")
    
    def test_2(self):
        input = \
'''
{"name": "User2", 
   "fav_language": "java",
   "fav_tech": "servicemesh",
   "favorites": {
        "other_tech1": "kubernetes",
        "other_tech2": "vfx"
   }
}
'''
        result = JsonObjectGenerator(input)
        
        self.assertEqual(result.name,"User2")
        self.assertEqual(result.fav_language, "java")
        self.assertEqual(result.fav_tech,"servicemesh")
        self.assertEqual(result.favorites.other_tech1,"kubernetes")
        pprint(result)

        
if __name__ == '__main__':
    unittest.main()
