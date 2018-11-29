print('python is running')

class Spring:
    def __init__(self, name, displacement=0, velocity=0):
        # Springs have a name, a displacement and velocity. By default, the displacement and velocity are both 0. Technically __init__ is the magic method that corresponds to calling the constructor Spring
        self.name = name
        self.displacement = displacement
        self.velocity = velocity
        return

    # now that we have a spring set up, we can begin implementing methods. We will start with the __repr__ method. This method runs whenever we evaluate an instance of this class with no other context.

    def __repr__(self):
        return str(self.name) + ': { displacement: ' + str(self.displacement) + ', velocity: ' + str(self.velocity) + ' }'
        # this method will return the Spring object and print off information regarding its properties.

    # contains is used with the key word in. We might say something like if 5 in springOne: . . .
    def __contains__(self, value):
        if(value == self.displacement or value == self.velocity):
            return True
        else:
            return False
    
    # we will now set up __call__. __call__ allows us to add a behavior for when our Spring is called as a function. We will have call reassign the spring's attributes.
    
    def __call__(self, newDis=0, newVel=0):
        self.displacement = newDis
        self.velocity = newVel
        return self
        # here calling the spring as a function will reset its value. Since we already have a __repr__ set up, when we return self we actually return the string returned by __repr__

    pass

s1 = Spring('spring one')
