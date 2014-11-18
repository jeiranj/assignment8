import numpy as np
import matplotlib.pyplot as plt
import sys
from .exceptions import *
from .myfunctions import *
from .checks import *

class InvestSimulator(object):
    """This class generates random draws from a binomial pdf and stores mean, std and
    generates histogram of samples.
    Attributes:
        -- pb: probability of win, e.g. 0.51
        -- num_trials: number of random draws, e.g. 10000
        -- investment: money to invest, e.g. 1000$
        -- positions: investment denominations, e.g. [1,10,100,1000]$
        -- position_value: size of each investment for each position in positions, e.g. 
                           investment/positions = [1000,100,10,1]
        -- cumu_ret: cumulative return for each draw, e.g. 0 or investment*2
                     matrix of size len(positions) x num_trials. 
        -- daily_ret: daily return for each draw
                      matrix of size len(positions) x num_trials.
        -- mean_dr: mean of daily returns; vector of length len(positions) 
        -- std_dr: std of daily returns; vector of length len(positions)
    Methods:
        -- simulate()"""
        
    def __init__(self,investment,positions,pb,num_trials):
    # class constructor. 
        if (check_pb(pb) == False):
            raise IncorrectProbability('Probability should be a number between 0 and 1 %s'%pb)
        elif (check_investment(investment) == False):
            raise IncorrectInvestment('Investment should be a number %s'%investment)
        elif (check_positions(positions) == False): 
            raise IncorrectPositions('Investment position(s) should be a number (or a list of numbers) %s'%positions)
        elif (check_num_trials(num_trials) == False):
            raise IncorrectTrialNumber('Number of trials should be an integer %s'%num_trials)
        else:
            self.pb = pb
            self.investment = int(investment)
            self.positions = np.array(get_positions(positions))
            self.num_trials = int(num_trials)
            self.position_value = float(self.investment)/self.positions
        
    def simulate(self):
        open('results.txt','w')
        for ind in self.positions:
            # Simulate samples for each investment position in 'positions'
            daily_ret = np.random.binomial(1,self.pb,(self.num_trials,ind))
            daily_ret[daily_ret==0] = -1
            cumu_ret = (daily_ret + 1)*self.investment/float(ind)  #position_value=investment/positions
            mean_daily_ret = np.mean(np.sum(daily_ret,axis=1))
            std_daily_ret = np.std(np.sum(daily_ret,axis=1))
             
            # Write results: mean and standard deviation of daily returns to file 'results.txt'
            with open('results.txt', 'a') as f:
                f.write("Investment positions: {} and investment value per position (dollar): {} \n".format(ind,self.investment/ind))
                f.write("\t Mean of daily return is {} \n".format(mean_daily_ret))
                f.write("\t Standard deviation of daily return is {} \n".format(std_daily_ret))
                f.write("\n \n")
            
            # Generate and save histogram plots of daily returns for each investment position
            plt.hist(np.sum(daily_ret,axis=1),100,color='gray')
            plt.xlabel('Total Daily Return')
            plt.ylabel('Frequency')
            plt.title('Histogram of Total Daily Returns (summed over different positions)')
            hist_name = 'histogram_{:04}.png'.format(ind)
            plt.savefig(hist_name)    
        f.close()
            