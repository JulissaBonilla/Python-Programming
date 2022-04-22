"""
A test script to test the module funcs.py

Author: Julissa Bonilla
Date: 1/10/22
"""
import introcs      # For assert_equals
import funcs        # This is what we are testing


# Put your code below this line
#test 1
result=funcs.has_a_vowel('aeiou')
introcs.assert_equals(True,result)

#test 2
result=funcs.has_a_vowel('car')
introcs.assert_equals(True,result)

#test 3
result=funcs.has_a_vowel('the')
introcs.assert_equals(True,result)

#test 4
result=funcs.has_a_vowel('indeed')
introcs.assert_equals(True,result)

#test 5
result=funcs.has_a_vowel('open')
introcs.assert_equals(True,result)

#test 6
result=funcs.has_a_vowel('u')
introcs.assert_equals(True,result)

#test 7
result=funcs.has_a_vowel('keep')
introcs.assert_equals(True,result)

#test 8
result=funcs.has_a_vowel('i')
introcs.assert_equals(True,result)

#test 9
result=funcs.has_a_vowel('y')
introcs.assert_equals(False,result)

#test 10
result=funcs.has_a_vowel('squirt')
introcs.assert_equals(True,result)
# Do not write below this line
print('Module funcs is working correctly')
