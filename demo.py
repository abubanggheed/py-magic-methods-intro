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
    
    def __call__(self, newDis=None, newVel=None):
        if(newDis != None):
            self.displacement = newDis
        if(newVel != None):
            self.velocity = newVel
        return self
        # here calling the spring as a function will reset its value. Since we already have a __repr__ set up, when we return self we actually return the string returned by __repr__

    # the __neg__ and __pos__ methods occur when you would use a + or a - sign before asking for a __repr__ we use - a lot for numbers to make negative numbers.

    def __pos__(self):
        # we will use __pos__ to create a new Spring all number attributes set to non-negative values.
        newSpring = Spring(self.name, abs(self.displacement), abs(self.velocity))
        return newSpring

    def __neg__(self):
        # we will use __neg__ to create a new Spring all number attributes equal to this spring's opposite values.
        newSpring = Spring(self.name, -self.displacement, -self.velocity)
        return newSpring

    # normally we wouldn't be able to compare two Springs since they are no more than references to an object. However, with __eq__ and __ne__ we can allow for logic such as springOne == springTwo to sometimes return True.

    def __eq__(self, other):
        # we only want to compare two springs. We will return true if both strings have the same displacement and velocity
        if(type(other) == Spring):
            if(self.displacement == other.displacement and self.velocity == other.velocity):
                return True
        return False

    def __ne__(self, other):
        # for not equals, we return the opposite of whatever equals would return
        return not self == other

    pass

s1 = Spring('spring one')
s2 = Spring('spring two')
