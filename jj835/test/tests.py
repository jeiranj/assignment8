import unittest
from InvestSimulator.checks import *
from InvestSimulator.myfunctions import *

class checks_tests(unittest.TestCase):
    def test_pb_bad(self):
        args = ['','nevermore','never345','0.345never',1,-2]
        for a in args:
            self.assertFalse(check_pb(a))

    def test_pb(self):
        self.assertTrue(check_pb(0.1))

    def test_investment_bad(self):
        args = ['', 'nevermore','never345','0.345never',10]
        for a in args:
            self.assertTrue(check_investment,a)

    def test_investment(self):
        args = [100, 555.5]
        for a in args:
            self.assertTrue(check_investment,a)

    def test_positions_bad(self):
        args = ['','[10.1,100]', '[10..,1000.100]','[10a, 200, 1000]','[-10,100]',100]
        for a in args:
            self.assertFalse(check_positions(a))

    def test_positions(self):
        args = ['[10,100]', '(10,1000,100]','(10, 200, 1000]',]
        for a in args:
            self.assertTrue(check_positions,a)

    def test_num_trials_bad(self):
        args = ['',10.5,'100']
        for a in args:
            self.assertFalse(check_num_trials(a))

    def test_num_trials(self):
        self.assertTrue(check_num_trials,100)

suite = unittest.TestLoader().loadTestsFromTestCase(checks_tests)
unittest.TextTestRunner(verbosity=2).run(suite)            
    

##  


class myfunctions_tests(unittest.TestCase):
    """Test get_positions() function. """
    def test_get_positions(self):
        input = [' [ 2,10,100]', '[ 2,10, 100 ) ', '(2, 10, 100 ]', '(2, 10,100)']
        output = [[2, 10,100], [2, 10, 100], [2, 10, 100], [2, 10, 100]]
        for i in range(len(input)):
            self.assertEqual(get_positions(input[i]), output[i])

suite = unittest.TestLoader().loadTestsFromTestCase(myfunctions_tests)
unittest.TextTestRunner(verbosity=2).run(suite)            

