"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Julissa Bonilla
Date:   1/26/22
"""
import currency
src=input('3-letter code for original currency: ')
dst=input('3-letter code for the new currency: ')
amt=input('Amount of the original currency: ')
print('You can exchange '+amt+' '+src+' for '+str(round(currency.exchange(src,dst,float(amt)),3))+' '+dst+'.')
