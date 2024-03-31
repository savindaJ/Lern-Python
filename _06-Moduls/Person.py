def sample_function():
    print("This is a sample function from Person.py")
    print(__name__) # __name__ is a special variable that contains the name of the module
    try:
        raise Exception("This is a custom exception") # throw custom exception using raise
    except Exception as e:
        print(e)