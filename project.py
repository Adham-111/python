class person :
    def __init__(self,name,money,mode,healthRate):
        self.name=name
        self.money=money
        self.mode=mode
        self.healthRate=healthRate
    def sleep(self,hours):
        if hours == 7:
            print("happy")
        elif hours < 7 :
            print("tired")
        else:
            print("lazy")       
    def eat(self,meals):
        if meals== 3 :
            self.healthRate = 100
            print(self.healthRate)
        elif meals==2 :
            self.healthRate = 75
            print(self.healthRate)
        elif meals ==1:
            self.healthRate = 50
            print(self.healthRate)
        else :
            print("unfefined number of meals enter from 1 to 3")           
    
    def buy(self,items):
        self.money=self.money - 10*items
        print(self.money)
        
class car :
    def __init__(self,name,fuelrate,velocity):
        self.name=name
        self._fuelrate=min(max(fuelrate,0),100)
        self._velocity=min(max(velocity,0),200)
    @property   
    def fuelRate(self):
        return self._fuelrate
    @fuelRate.setter
    def fuelRate (self,value):
        self._fuelrate=min(max(value,0),100)
    @property   
    def velocity(self):
        return self._velocity
    @velocity.setter
    def velocity(self,value):
        self._velocity=min(max(value,0),200)
     
    def run(self,velocity,distance):
        self.velocity=velocity
        max_disstance=self.fuelRate /0.01
        if max_disstance > distance :
            self.fuelRate-=distance*0.01
            self.stop(0)
        else:
            self.fuelRate=0
            distance_car_coverd=max_disstance
            self.stop(distance-distance_car_coverd)
    def stop(self,distance_remain):
        self.velocity=0
        if distance_remain == 0 :
            print("you arrive to the destination ")
        else:
            print(f"the remain distance is {distance_remain}")
    
              
class employee(person):
    def __init__(self, name, money, mode, healthRate,Id,car,email,salary,distancetowork):
        super().__init__(name, money, mode, healthRate)
        self.Id=Id
        self.car=car
        self.email=email
        self.salary=salary
        self.distancetowork=distancetowork

    def work(self,hours):
        if hours ==8 :
            self.mode="happy"
        elif hours>8:
            self.mode="tired"
        else :
            self.mode="lazy" 
    def drive(self,distance,speed):
        self.car.run(distance,speed) 
    
    def refuel(self,gasAmount=100) :
        self.car.fuelRate= gasAmount
    
class office :
    employees_number=0
    def __init__(self,name):
        self.name=name
        self.employees= []
    def get_all_employee (self):
        return self.employees
    def get_employee_id(self,empID):
        for emp in self.employees:
            if emp.Id==empID:
                return emp
        return None
    def hire_employee(self,Employee_name):
        self.employees.append(Employee_name)
        office.employees_number+=1
    def fire(self,empId):
        for emp in self.employees :
            if emp.Id==empId :
                office.employees_number-=1
                self.employees.remove(emp)
                print(f"employee with {empId} is fired ")
        print("id is not found on employees list")
    def deduct(self,empid,detuction):
        emp=self.get_employee_id(empid)
        if emp :
            emp.salary-=detuction
    def reward(self,empid,reward):
        emp=self.get_employee_id(empid)      
        if emp:
            emp.salary+=reward
    def checklatens(self,empid,move_hour):
        emp=self.get_employee_id(empid)
        if emp: 
            late_employee=office.calculate_latence(9,move_hour,emp.distancetowork,emp.car.velocity)
            if late_employee :
                self.deduct(empid,10)
                print("your salary decreased by 10 ")
            else:
                self.reward(empid,10)
                print("your salary increased by 10 ")
    @staticmethod 
    def calculate_latence(targetHour , moveHour, distance, velocity):
        arriveToOffice=moveHour+distance/velocity
        return arriveToOffice > targetHour   
        
    @classmethod
    def  change_emps_num(cls,num):
        cls.employees_number=num
        
fiat = car("Fiat 128", 100, 60)
bmw=car("Bmw",90,95)
samy = employee("Samy", 300, "neutral", 80, 1, fiat, "samy@iti.org", 4000, 20)
ali= employee("ahmed",200,"neutral",70,2,"bmw","samy@iti.org",3000,30)
iti_office = office("ITI Smart Village")
iti_office.hire_employee(samy)
samy.drive(20,60)
print(samy.eat(4))
print(iti_office.employees_number)
iti_office.hire_employee(ali)
print(iti_office.employees_number)
print(office.employees_number)
print(iti_office.get_all_employee())