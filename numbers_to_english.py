"""Given an int32 number, print it in English."""
def int_to_en(num):
    m = { 0 : 'zero',
          1 : 'one',
          2 : 'two',
          3 : 'three',
          4 : 'four',
          5 : 'five',
          6 : 'six',
          7 : 'seven',
          8 : 'eight',
          9 : 'nine',
          10 : 'ten',
          11 : 'eleven',
          12 : 'twelve',
          13 : 'thirteen',
          14 : 'fourteen',
          15 : 'fifteen',
          16 : 'sixteen',
          17 : 'seventeen',
          18 : 'eighteen',
          19 : 'ninteen',
          20 : 'twenty',
          30 : 'thirty',
          40 : 'fourth',
          50 : 'fifty',
          60 : 'sixty',
          70 : 'seventy',
          80 : 'eighty',
          90 : 'ninty',
          100 : 'hundred',
          1000 : 'thousand',
          1000000 : 'million',
          1000000000 : 'billion' }

    if (num < 20):
        return m[num]
    # 20 <= num and num < 100
    if (num < 100):
        if num % 10 == 0:
            return m[num]
        else:
            return m[num // 10 * 10] + '-' + m[num % 10]
    # 100 <= num and num < 1000
    if (num < 1000):
        if num % 100 == 0:
            return m[num // 100] + ' hundred '
        else:
            return m[num // 100] + ' hundred and ' + int_to_en(num % 100)
    # 1000 <= num and num < 1000_000
    if (num < 1000000):
        if num % 1000 == 0:
            return int_to_en(num // 1000) + ' thousand '
        else:
            return int_to_en(num // 1000) + ' thousand ' + int_to_en(num % 1000)
    # 1_000_000 < num and num < 1000_000_000
    if (num < 1000000000):
        if (num % 1000000) == 0:
            return int_to_en(num // 1000000) + ' million '
        else:
            return int_to_en(num // 1000000) + ' million ' + int_to_en(num % 1000000)

    if (num % 1000000000) == 0:
        return int_to_en(num // 1000000000) + ' billion '
    else:
        return int_to_en(num // 1000000000) + ' billion ' + int_to_en(num % 1000000000)

    assert(False)

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
