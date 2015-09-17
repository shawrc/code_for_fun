"""Given an int32 number, print it in English."""
def int_to_en(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'ninteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'fourth', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninty' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert(0 <= num)

    if (num < 20): return d[num]
    if (20 <= num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + '-' + d[num % 10]

    if (num < k):
        if num % 100 == 0: return d[num // 100] + ' hundred'
        else: return d[num // 100] + ' hundred and ' + int_to_en(num % 100)

    if (num < m):
        if num % k == 0: return int_to_en(num // k) + ' thousand'
        else: return int_to_en(num // k) + ' thousand ' + int_to_en(num % k)

    if (num < b):
        if (num % m) == 0: return int_to_en(num // m) + ' million'
        else: return int_to_en(num // m) + ' million ' + int_to_en(num % m)

    if (num < t):
        if (num % b) == 0: return int_to_en(num // b) + ' billion'
        else: return int_to_en(num // b) + ' billion ' + int_to_en(num % b)

    if (num % t == 0): return int_to_en(num // t) + ' trillion'
    else: return int_to_en(num // t) + ' trillion ' + int_to_en(num % t)

    raise AssertionError('num is too large: %s' % str(num))

print(0, int_to_en(0))
print(3, int_to_en(3))
print(10, int_to_en(10))
print(11, int_to_en(11))
print(19, int_to_en(19))
print(20, int_to_en(20))
print(23, int_to_en(23))
print(34, int_to_en(34))
print(56, int_to_en(56))
print(80, int_to_en(80))
print(97, int_to_en(97))
print(99, int_to_en(99))
print(100, int_to_en(100))
print(101, int_to_en(101))
print(110, int_to_en(110))
print(117, int_to_en(117))
print(120, int_to_en(120))
print(123, int_to_en(123))
print(172, int_to_en(172))
print(199, int_to_en(199))
print(200, int_to_en(200))
print(201, int_to_en(201))
print(211, int_to_en(211))
print(223, int_to_en(223))
print(376, int_to_en(376))
print(767, int_to_en(767))
print(982, int_to_en(982))
print(999, int_to_en(999))
print(1000, int_to_en(1000))
print(1001, int_to_en(1001))
print(1017, int_to_en(1017))
print(1023, int_to_en(1023))
print(1088, int_to_en(1088))
print(1100, int_to_en(1100))
print(1109, int_to_en(1109))
print(1139, int_to_en(1139))
print(1239, int_to_en(1239))
print(1433, int_to_en(1433))
print(2000, int_to_en(2000))
print(2010, int_to_en(2010))
print(7891, int_to_en(7891))
print(89321, int_to_en(89321))
print(999999, int_to_en(999999))
print(1000000, int_to_en(1000000))
print(2000000, int_to_en(2000000))
print(2000000000, int_to_en(2000000000))
