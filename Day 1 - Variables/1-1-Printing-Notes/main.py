#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests
#Write your code below this line 👇
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")






































#Copy Paste your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇
with open("testing_copy.py", "w") as file:
  file.write("def test_func():\n")
  with open("main.py", "r") as original:
    f2 = original.readlines()[0:30]
    for x in f2:
      file.write("    " + x)

import testing_copy
import unittest
from unittest.mock import patch
from io import StringIO
import os

class MyTest(unittest.TestCase):
  def test_1(self): 
    with patch('sys.stdout', new = StringIO()) as fake_out: 
      testing_copy.test_func()
      expected_print = "Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')\n"
      self.assertEqual(fake_out.getvalue(), expected_print) 

print("\n\n")
print('Checking if what you printed matches the target output *exactly*...')
print('Running some tests on your code:')
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)

os.remove("testing_copy.py") 


