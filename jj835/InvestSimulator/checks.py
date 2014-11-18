from .exceptions import *
import re

def check_pb(pb):
    """Check built-in probability 'pb'. 
       If not a number or pb<0 or pb>1, it returns False.
       Args:
            -- pb """
    if ((type(pb) == int or type(pb) == float) and pb>0 and pb<1):
        return True
    else:
        return False
        
def check_investment(investment):
    """Check user-supplied 'investment'.
       If not a number, it returns False.
       Args:
            -- investment """
    if type(investment) == str:
        investment = investment.strip()
        matches = bool(re.match('\d+',investment))
        return matches
    else: return False
    
def check_positions(positions):
    """Check user-supplied 'positions'.
       If not a number or not a list of integers, it returns False.
       Args:
            -- positions """
    if type(positions) == str:
        positions = positions.strip()
        matches = bool(re.match('^[\[\(]*[\s*\d+\.\d*\s*,]*\s*\d+\s*[\]\)]*$',positions))
        if not(re.findall('\d+\.',positions)):  #check for decimal points
            return matches
    else: return False
    
def check_num_trials(num_trials):
    """Check user-supplied 'num_trials'.
       If not a number, it returns False.
       Args:
            -- investment """
    if type(num_trials) == str:
        num_trials = num_trials.strip()
        matches = bool(re.match('\d+',num_trials))
        if not(re.findall('\d+\.',num_trials)):  #check for decimal points
            return matches
    else: return False
