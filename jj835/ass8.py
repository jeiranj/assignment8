# 
# Python ass8.py 
# 

from InvestSimulator.investSimulator import *
# from InvestSimulator.exception import *
# from InvestSimulator.checks import *
import sys

def main():
    try:
        investment = raw_input('Enter amount to invest, e.g. 1000: ')
        num_trials = raw_input('Enter number of trails, e.g. 10000: ')
        positions = raw_input('Enter investment positions, e.g. [1,10,100,1000]: ')
    except (KeyboardInterrupt, EOFError):
            print '\nAs you wish! \n'
            sys.exit()

    print 'Simulating with positions = {} ...'.format(positions)
    pb = 0.51
    invest = InvestSimulator(investment,positions,pb,num_trials)
    invest.simulate()
    print 'Done!  Check your results.'
        
            
if __name__ == '__main__':
    main()
    
    
    