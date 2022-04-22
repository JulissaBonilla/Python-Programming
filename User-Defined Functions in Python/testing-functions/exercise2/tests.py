"""
A test script to test the module funcs.py

Author: Julissa Bonilla
Date:1/10/22
"""
import introcs      # For assert_equals and assert_true
import funcs        # This is what we are testing
def test_has_a_vowel():
    """
    Test procedure for has_a_vowel
    """
    print('Testing has_a_vowel')
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
def test_has_y_vowel():
    """
    Test procedure for has_y_vowel
    """
    print('Testing has_y_vowel')
    #test 1
    result=funcs.has_y_vowel('aeiou')
    introcs.assert_equals(False,result)
    #test 2
    result=funcs.has_y_vowel('yy')
    introcs.assert_equals(True,result)
    #test 3
    result=funcs.has_y_vowel('they')
    introcs.assert_equals(True,result)
    #test 4
    result=funcs.has_y_vowel('py')
    introcs.assert_equals(True,result)
    #test 5
    result=funcs.has_y_vowel('openy')
    introcs.assert_equals(True,result)
    #test 6
    result=funcs.has_y_vowel('wy')
    introcs.assert_equals(True,result)
    #test 7
    result=funcs.has_y_vowel('osiejfey')
    introcs.assert_equals(True,result)
    #test 8
    result=funcs.has_y_vowel('sky')
    introcs.assert_equals(True,result)
    #test 9
    result=funcs.has_y_vowel('y')
    introcs.assert_equals(False,result)
    #test 10
    result=funcs.has_y_vowel('yell')
    introcs.assert_equals(False,result)
# Script Code
test_has_a_vowel()
test_has_y_vowel()
print('Module funcs is working correctly')
