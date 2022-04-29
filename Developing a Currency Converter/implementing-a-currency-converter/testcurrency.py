"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Julissa Bonilla
Date:   1/26/22
"""
import introcs
import currency

def test_before_space():
    """Test procedure for before_space"""
    print("Testing before_space")
    results=currency.before_space('290 Dollars')
    introcs.assert_equals('290',results)

    results=currency.before_space('290 ')
    introcs.assert_equals('290',results)
    
    results=currency.before_space(' 345 Dollars')
    introcs.assert_equals('',results)
    
    results=currency.before_space(' ldkm')
    introcs.assert_equals('',results)
    
    results=currency.before_space('290  ')
    introcs.assert_equals('290',results)

    results=currency.before_space(' ')
    introcs.assert_equals('',results)

    
def test_after_space():
    """Test procedure for after_space"""
    print("Testing after_space")

    results=currency.after_space('290 Dollars')
    introcs.assert_equals('Dollars',results)

    results=currency.after_space('290 ')
    introcs.assert_equals('',results)
    
    results=currency.after_space(' 345 Dollars')
    introcs.assert_equals('345 Dollars',results)
    
    results=currency.after_space(' ldkm')
    introcs.assert_equals('ldkm',results)
    
    results=currency.after_space('290  ')
    introcs.assert_equals(' ',results)

    results=currency.after_space(' ')
    introcs.assert_equals('',results)
    

def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""
    print("Testing first_inside_quotes")

    results=currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C',results)

    results=currency.first_inside_quotes('"B C"')
    introcs.assert_equals('B C',results)

    results=currency.first_inside_quotes('A "B C" "D"')
    introcs.assert_equals('B C',results)

    results=currency.first_inside_quotes('A "B C"" D')
    introcs.assert_equals('B C',results)
    
    results=currency.first_inside_quotes('A ""B C" D')
    introcs.assert_equals('',results)


def test_get_src():
    """Test procedure for get_src"""
    print("Testing get_src")
    results= currency.get_src('{"success":false,"src":"","dst":"",'
    +'"error":"Source currency code is invalid."}')
    introcs.assert_equals('',results)
    
    results= currency.get_src('{"success": false, "src": "", "dst": "", "error": '
    +'"Source currency code is invalid."}')
    introcs.assert_equals('',results)   
    
    results=currency.get_src('{"success": true, "src": "2 United States Dollars",'
    +' "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars',results)
    
    results= currency.get_src('{"success":true, "src":"2 United States Dollars", '
    +'"dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('2 United States Dollars',results)
    

def test_get_dst():
    """Test procedure for get_dst"""
    print("Testing get_dst")
    results= currency.get_dst('{"success": true, "src": "2 United States Dollars",'
    +' "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros',results)
    
    results= currency.get_dst('{"success":false,"src":"","dst":"","error":"Source '
    +'currency code is invalid."}')
    introcs.assert_equals('',results)   
    
    results=currency.get_dst('{"success":true, "src":"2 United States Dollars", '
    +'"dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('1.772814 Euros',results)
    
    results= currency.get_dst('{"success": false,"src": "","dst": "","error":'
    +' "Source currency code is invalid."}')
    introcs.assert_equals('',results)


def test_has_error():
    """Test procedure for has_error"""
    print("Testing has_error")
    results= currency.has_error('{"success":false,"src":"","dst":"","error":'
    +'"Source currency code is invalid."}')
    introcs.assert_equals(True,results)
    
    results= currency.has_error('{"success": true, "src": "2 United States Dollars", '
    +'"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals(False,results)   
    
    results=currency.has_error('{"success":true, "src":"2 United States Dollars", '
    +'"dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals(False,results)

    results= currency.has_error('{"success": false,"src":"","dst": "","error": '
    +'"Source currency code is invalid."}')
    introcs.assert_equals(True,results)


def test_service_response():
    """Test procedure for service_response"""
    print("Testing service_response")
    
    results=currency.service_response('USD','EUR',2.5)
    introcs.assert_equals('{"success": true, "src": "2.5 United States Dollars", '
    +'"dst": "2.2160175 Euros", "error": ""}',results)

    results=currency.service_response('USD','EUR',-2.5)
    introcs.assert_equals('{"success": true, "src": "-2.5 United States Dollars",'
    +' "dst": "-2.2160175 Euros", "error": ""}',results)

    results=currency.service_response('UOD','YHS',2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": '
    +'"The rate for currency UOD is not present."}',results)

    results=currency.service_response('USD','YHS',-0.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": '
    +'"The rate for currency YHS is not present."}',results)


def test_iscurrency():
    """Test procedure for iscurrency"""
    print("Testing iscurrency")
    
    results=currency.iscurrency('WWW')
    introcs.assert_equals(False,results)
    
    results=currency.iscurrency('USD')
    introcs.assert_equals(True,results)


def test_exchange():
    """Test procedure for exchange"""
    print("Testing exchange")
    
    results=currency.exchange('USD','EUR',2.5)
    introcs.assert_floats_equal(2.2160175,results)

    results=currency.exchange('USD','EUR',-2.5)
    introcs.assert_floats_equal(-2.2160175,results)


test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()
print('All tests completed successfully.')
