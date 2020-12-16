#Closures

'''

A Closure is a function object that remembers values in enclosing scopes 
even if they are not present in memory.

A Closure is a record storing a function together with an environment: a mapping
associating with each free variable of the function with the value or storage location 
to which the name as bound when the closure was created. A closure, unlike a plain function,
allows the function to access those variables through the closure's reference to them, even when
the function is invoked outside their scope.

TL:DR; 

Closures are when a function remembers the environment it was created in, 
specifically the variables around it.  

A closure is an inner function that remembers 
and has access to variables in the local scope in which it was created even after 
the outer function has finished executing.

'''