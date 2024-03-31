class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f"CustomException: {self.message}"

def sample_function():
    try:
        raise CustomException("This is a custom exception") # throw custom exception using raise
    except Exception as e:
        print(e)
        
sample_function()
print("End of program")