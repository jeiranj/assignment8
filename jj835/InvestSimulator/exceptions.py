class Error(Exception):
    """Base class for exceptions.
    Attributes:
        -- expression: input expression in which the error occurred
        -- message: explanation of the error."""
    def __init__(self, message):
        self.message = message
        
    def __str__(self):
        return repr(self.message)

class IncorrectProbability(Error):
    #User-supplied probability is not between 0 and 1.
    pass

class IncorrectInvestment(Error):
    #User-supplied investment is not a number.
    pass
        
class IncorrectPosition(Error):
    #User-supplied investment position is not a number.
    pass
    
class IncorrectTrialNumber(Error):
    #User-supplied num_trials is not a number.
    pass