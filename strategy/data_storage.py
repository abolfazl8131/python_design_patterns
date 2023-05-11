
class DataStorsgeStrategy:
    def store(self):
        pass



class MemoryStore(DataStorsgeStrategy):

    def store(self , data):
        print(f"stored {data['name']} in RAM.")




class DiskStore(DataStorsgeStrategy):

    def store(self , data):
        print(f"stored {data['name']} in Disk")




data = [{'name':'sth1','data_volume':30000} , {'name':'sth2','data_volume':250},{'name':'sth3','data_volume':1500}]

for d in data:
    if d['data_volume'] <= 1500:
        MemoryStore().store(d)
    else:
        DiskStore().store(d)