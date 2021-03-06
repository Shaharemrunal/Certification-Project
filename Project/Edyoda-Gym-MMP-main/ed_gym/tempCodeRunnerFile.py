import random as rd

# Gym member class for data management and manipulation
class Gym_Member():
    def __init__(self):
        '''
        Creating variables for storing and managing data of members
        '''
        self.details = {'100':{'Membership ID': '100', 'Name': 'Mrunal Shahare', 'Age': '22' , 'Gender': 'Male', 'Mobile Number': '8668362158', 'Email': 'ShahareMrunal@gmail.com', 'BMI': '19', 'Membership Duration(Months)': '12', 'Status': 'Active'},'101':{'Membership ID': '101', 'Name': 'Aditya Shahare', 'Age': '26' , 'Gender': 'Male', 'Mobile Number': '8421547889', 'Email': 'aditya@gmail.com', 'BMI': '23', 'Membership Duration(Months)': '9', 'Status': 'Active'}}
        self.admin = {'admin123':'123admin'}
        self.user = {'100':'1234','101':'4321'}
        self.count = '102'
        self.regimen = {'100':{'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Cardio/Abs', 'Thu': 'Back', 'Fri': 'Triceps', 'Sat': 'legs', 'Sun': 'Rest'},'101':{'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Cardio/Abs', 'Thu': 'Back', 'Fri': 'Triceps', 'Sat': 'legs', 'Sun': 'Rest'}}
    
    ''' Data receiving and stroing method '''
    
    def add_mem(self):
        
        ''' BMI Calculator '''
        
        def bmi(w,h):
            b = w/(h * h)
            return b
        
        '''
        Taking user input for creating membership
        '''
        
        d = dict()
        d ['Membership ID'] = self.count
        d['Name']= input('Enter name: ')
        d['Age']= input('Enter age: ')
        d['Gender'] = input('Enter gender: ')
        d['Mobile Number'] = input('Enter mobile number: ')
        d['Email'] = input('Enter email: ')
        w = float(input('Enter weight (in Kg): '))
        h = float(input('Enter height (in M) [for eg; 1.40,1.64,etc.]: '))
        d['BMI'] = str(bmi(w,h))
        d ['Membership Duration(in Months)']= input('Enter Membership duration(in Months (1, 3, 6, or 12)): ')
        d ['Status'] = 'Active'
        self.details[self.count] = d
        pin = str(rd.randint(100,10000))
        print('\n\nWelcome to Edyoda Gym\nNow you have become a Elite Member of our World Class Gym\n')
        print('Your Membership ID is :', self.count,'\nyou login pin is :', pin)
        print('\nUse your Membership ID and your pin as your login credentials')
        print('\nPlease do not forget or share your pin with another person')
        self.user[self.count] = pin
        self.count = str(int(self.count)+1)
        
        '''
        Creating regimen intially only to make it editable later 
        '''
        
    def regi(self,id):
        self.details
        reg = dict()
        BMI = float(self.details[id]["BMI"])
        if BMI < 18.5:
            reg['Mon']='Chest'
            reg['Tue']='Biceps'
            reg['Wed']='Rest'
            reg['Thu']='Back'
            reg['Fri']='Triceps'
            reg['Sat']='Rest'
            reg['Sun']='Rest'
        elif BMI < 25.0:
            reg['Mon']='Chest'
            reg['Tue']='Biceps'
            reg['Wed']='Cardio/Abs'
            reg['Thu']='Back'
            reg['Fri']='Triceps'
            reg['Sat']='legs'
            reg['Sun']='Rest'
        elif BMI < 30.0:
            reg['Mon']='Chest'
            reg['Tue']='Biceps'
            reg['Wed']='Abs/Cardio'
            reg['Thu']='Back'
            reg['Fri']='Triceps'
            reg['Sat']='legs'
            reg['Sun']='Cardio'
        else:
            reg['Mon'] = 'Chest'
            reg['Tue'] = 'Biceps'
            reg['Wed'] = 'Cardio'
            reg['Thu'] = 'Back'
            reg['Fri'] = 'Triceps'
            reg['Sat'] = 'Cardio'
            reg['Sun'] = 'Cardio'
        
        # storing and assigning regimen to member
        self.regimen[id] = reg
