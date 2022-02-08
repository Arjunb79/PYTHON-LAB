class employee:
    def __init__(self,name,salaryPerDay):
        self.name=name
        self.salaryPerDay=salaryPerDay
    def salaryCal(self,days):
        self.days=days
        self.salary=self.salaryPerDay*self.days
        return self.salary
    def __lt__(self, other):
        if self.salary<other.salary
            return True
        else:
            return False


emp1=employee("ARJUN B",1500)
print("salary=",emp1.salaryCal(int(input("enter the number of days worked by employee 1:"))))
emp2=employee("ARUN",1500)
print("salary=",emp2.salaryCal(int(input("enter the number of days worked by employee 2:"))))
#print(emp1<emp2)

