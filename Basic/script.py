#name = "hovlo"
#age = 25.555
#print(f"hello,{name},qo tariqna {age}")

#print('%d is ok' % (age))

#print ('%s is %d years old' % ('Joe', 42))


#str_lower = 'abcdefjhy'
#str_uper = 'ABCDEFJS'

#print(str_lower.upper())
#print(str_uper.lower())

#string = "geeks for geeks geeks geeks geeks" 
   
# Prints the string by replacing geeks by Geeks  
#print(string.replace("geeks", "Geeks"))  
  
# Prints the string by replacing only 3 occurrence of Geeks   
#print(string.replace("geeks", "GeeksforGeeks", 2)) 
# for integers

#print(float(10),'for integers')

# for floats
#print(float(11.22),'for floats')

# for string floats
#print(float("-13.33"),'for string floats')

# for string floats with whitespaces
#print(float("     -24.45\n"),'for string floats with whitespaces')

# string float error
#print(float("abc"),'string float error')

#class Parent():

#    arg = 5

#    def __init__(self):
#        print('decorator class')
        
#   def __call__(self, cls):
#        print('call parent call function')


#class Child(Parent):
    
#    def __init__(self):
#        print('child class')
        

#    def new_method(self, value):
#        return value * 3
        
#x = Child()
#print(x.arg)


def tester(start):
    state = start 
        
    def nerqin_funkcia():
        #nonlocal state
        
        state += 1
        
        return state 
    
    return nerqin_funkcia()
			
print(tester(5))










