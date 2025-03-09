"""
se3250lib Version 0.1.0

Copyright (c) 2024 FEONA MAE L. JOHNSON

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

    ''' A ship carrying anti-ship cruise missiles.

    Attributes:
        * type (str): the type of ship, for labeling purposes only.
        * op (int): the number of anti-ship cruise missiles the ship can fire in one salvo.
        * dp (int): the number of SAM the ship can fire in one salvo against incoming missiles.
        * sp (float): initial staying power in missile hits.
        * lmq (int): long range missile quantity/estimate
        * mmq (int): medium range missile quantity/estimate
        * hp (float): hit points remaining.
        * status (fraction): fraction of its staying power remaining. 1 is intact, 0 is OOA.
    '''

"""

ship_inv = {
    "LCS-Freedom": {
        "type": 'LCS-Freedom',
        "classtype": 'LCS',
        "op": 2.4,
        "dp": 2.1,
        "sp": 1.15,
        "lmq": 21,
        "mmq": 24,
        "age": 8,
        "training": 0.85,
    },
    "LCS-Independence": {
        "type": 'LCS-Independence',
        "classtype": 'LCS',
        "op": 3.2,
        "dp": 11,
        "sp": 1.27,
        "lmq": 8,
        "mmq": 24,
        "age": 6,
        "training": 0.88,
    },
    "DDG-Arleigh-Burke": {
        "type": 'DDG-Arleigh-Burke',
        "classtype": 'DDG',
        "op": 10.4,
        "dp": 9,
        "sp": 1.54,
        "lmq": 45,
        "mmq": 45,
        "age": 12,
        "training": 0.92,
    },
    "CVN-Enterprise": {
        "type": 'CVN-Enterprise',
        "classtype": 'CVN',
        "op": 20,
        "dp": 10,
        "sp": 2,
        "lmq": 0,
        "mmq": 0,
        "age": 35,
        "training": 0.65,
    },
}
