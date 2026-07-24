# Tuples are immutable
numbers = (2,3,4,5)

# Tuple Comprehensions : 
  # Normal Method :
     squares = ()
     for i in range(1,10):
         squares += (i**2,)
  # List Comprehension Method (One Line) :
     squares = tuple(i**2 for i in range(1,10))
  # Normal Method : 
     numbers = (2,4,6,8)
  # List Comprehension Method :
     numbers = tuple(range(2,9,2))
