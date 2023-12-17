# decorators

-deorators alow you to 'decorate' a function

-imagine you created a fucntion

    def simple_func():
        # do simple stuff
        return something

-now you want to add some new capabilities to the function

    def simple_func():
        #want to do more stuff!
        #do simple stuff
        return something

-you now have two options:

    add that extra code (functionality) to your old function.
    create a brand new function that contains the old code and then add new code to that

-but what if you then want to remove that extra 'functionality'.?
you would need to delete it manually or make sure to have the old function

-is there a better way? maybe an on/off switch to quickly add this functionality?

# python has decorators that allow you to tack on extra functionality to an already existing function

# they use the @ operator and are then placed on top of the original function

-now you can easily add on extra functionality with a decorator:

    @some_decorator
    def simple_func():
        #do simple stuff
        return something
