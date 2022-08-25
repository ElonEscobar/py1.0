class Human:
  def __init__(self, name, age, height):
    self.height = height
    self.age = age
    self.name = name
    
    #print output in a single line format
  def __str__(self):
    return "name : {}, age :{}, height :{}".format(self.name, self.age, self.height)
      

x= Human("dr. dan",2 ,33)
print(x.age)
print(x.height) 
print(x.name) 

print(x)

#Inheritance
class worker(Human):
  def __init__(self, name , age, height, salary):
    super(worker , self).__init__(name, age, height)
    self.salary = salary
    
  def __str__(self):
    text =super(worker, self).__str__()
    text += ", salary: {}".format(self.salary)
    return text
  
  def yr_salary(self):
    return self.salary *12
  
worker2 =worker("henry",12,23,20000)

print (worker2.yr_salary()) 
print(worker2)
    