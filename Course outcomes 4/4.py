class Time:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
    def __add__(self, other):
        self.hour=self.hour+other.hour
        self.minute=self.minute+other.minute
        self.second=self.second+other.second
        return self.hour,self.minute,self.second
ob1=Time(10,00,00)
ob2=Time(10,10,00)

print("sum of times=",ob1+ob2)