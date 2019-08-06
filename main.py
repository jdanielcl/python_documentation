from vehicle import Vehicle


class TestClass:

    """
        General documentation
    """
    
    # <- this simbol is not used for it

    def function_one(self,test):

        """
            Documentation about function one
        """
        return "function_one "+test

    def function_two(self,a,b):

        """
            Documentation about function two
        """
        
        return f'function_one {a} {b}'

#Used for single methods

#print(function_one("test"))
#print(function_one.__doc__)
#help(function_one)

help(TestClass)
help(Vehicle)