"""  
A test script for the function iso_8601.

Author: Julissa Bonilla
Date: 2/23/22
"""
import func
import introcs


def test_iso_8601():
    """
    Test procedure for the function iso_8601()
    """
    print('Testing iso_8601()')
    
    # Put your test cases here
    result=func.iso_8601('00:00:0')
    introcs.assert_equals(False,result)

    result=func.iso_8601('00:0:00')
    introcs.assert_equals(False,result)

    result=func.iso_8601('0:00:00')
    introcs.assert_equals(True,result)

    result=func.iso_8601('00:00:00')
    introcs.assert_equals(True,result)
    
    result=func.iso_8601('00:020:00')
    introcs.assert_equals(False,result)
    
    result=func.iso_8601('00:00:000')
    introcs.assert_equals(False,result)

    result=func.iso_8601('000:00:00')
    introcs.assert_equals(True,result)

    result=func.iso_8601('00:00:')
    introcs.assert_equals(False,result)

    result=func.iso_8601('00::00')
    introcs.assert_equals(False,result)

    result=func.iso_8601('00:020:00')
    introcs.assert_equals(False,result)

    result=func.iso_8601('00:70:00')
    introcs.assert_equals(False,result)

    result=func.iso_8601('25:00:00')
    introcs.assert_equals(False,result)

    result=func.iso_8601('00:00:70')
    introcs.assert_equals(False,result)

    result=func.iso_8601('::')
    introcs.assert_equals(False,result)


if __name__ == '__main__':
    test_iso_8601()
    print('Module func passed all tests.')