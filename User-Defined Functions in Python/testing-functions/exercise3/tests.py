"""
A test script to test the module func.py

Author: Julissa Bonilla
Date: 1/10/22
"""
import introcs      # For assert_equals and assert_true
import funcs        # This is what we are testing


def test_replace_first():
    """
    Test procedure for replace_first
    """
    print('Testing replace_first')
    
    # Put your tests below this line
    result=funcs.replace_first('crane','a','o') 
    introcs.assert_equals('crone',result)
    
    result=funcs.replace_first('poll','l','o')
    introcs.assert_equals('pool',result)

    result=funcs.replace_first('crane','cr','b')
    introcs.assert_equals('bane',result)
    
    result=funcs.replace_first('banana','a','o')
    introcs.assert_equals('bonana',result)

    result=funcs.replace_first('kiw','i','ow')
    introcs.assert_equals('koww',result)

    result=funcs.replace_first('orange','a','0')
    introcs.assert_equals('or0nge',result)
    
    result=funcs.replace_first('crane','cr','')
    introcs.assert_equals('ane',result)

# Script Code
# Do not write below this line
test_replace_first()
print('Module funcs is working correctly')
