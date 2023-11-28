import pickle
from dictionary import load, save

def save(dict_to_save,file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(dict_to_save,f)

def load(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)
    

testdict = {1 : 'test1', 2 : 'test', 3 : 'test'}
save(testdict,'testdict.pickle')
print(load('testdict.pickle'))