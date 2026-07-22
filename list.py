# Adding Items to  List :
brand = ['Quark']
brand.append('X')
brand.insert(0,'Astra')  # list.insert(index,value)
brand.extend([3,4,5])    # brand = ['Astra','Quark','X',3,4,5]
brand.extend('xy')       # brand = ['Astra','Quark','X',3,4,5,'x','y']

# Deleting Items from List :
del brand[1]  # del list[index]
     # brand = ['Astra','X',3,4,5,'x','y']
popped_value = brand.pop(1)   # popped_val = list.pop(index) {pop() returns the popped value}
     # brand = ['Astra',3,4,5,'x','y']
     # popped_value = 'X'
brand.remove('x')  # list.remove(value)
     # brand = ['Astra',3,4,5,'y']
     # It removes only the first occurrence of the value
