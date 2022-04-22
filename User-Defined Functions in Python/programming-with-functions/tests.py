"""
The test script for the course project.

Author: Julissa Bonilla
Date: 1/14/22
"""
import funcs
import introcs
def test_matching_parens ():
    """
    Test procedure for matching_parens
    """
    print('Testing matching_parens')
    result=funcs.matching_parens('(ds)oaj')
    introcs.assert_equals(True,result)

    result=funcs.matching_parens('((((dooj))))')
    introcs.assert_equals(True,result)
    
    result=funcs.matching_parens(')))(vo))')
    introcs.assert_equals(True,result)
    
    result=funcs.matching_parens('(((j)')
    introcs.assert_equals(True,result)
    
    result=funcs.matching_parens('()((sd))')
    introcs.assert_equals(True,result)

    result=funcs.matching_parens('A()B')
    introcs.assert_equals(True,result)

    result=funcs.matching_parens(')')
    introcs.assert_equals(False,result)
    
    result=funcs.matching_parens('')
    introcs.assert_equals(False,result)


def test_first_in_parens():
    """
    Test procedure for first_in_parens
    """
    print('Testing first_in_parens')
    result=funcs.first_in_parens('(ds)oaj')
    introcs.assert_equals('ds',result)

    result=funcs.first_in_parens('((((dooj))))')
    introcs.assert_equals('(((dooj',result)
    
    result=funcs.first_in_parens(')))(vo))')
    introcs.assert_equals('vo',result)
    
    result=funcs.first_in_parens('(((j)')
    introcs.assert_equals('((j',result)
    
    result=funcs.first_in_parens('()((sd))')
    introcs.assert_equals('',result)


# Script Code
test_matching_parens()
test_first_in_parens()
print('Module funcs is working correctly')