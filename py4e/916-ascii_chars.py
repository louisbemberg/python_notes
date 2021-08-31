print(ord('H'))
print(ord('p'))
print(ord('3'))
print(ord('T'))

# UTF-8 is the best way to send chars across the web
# more than 85% of the web is compressed in utf8

# in python3, all strings internally are UNICODE (best but inefficient)

# UNICODE => encode() to utf 8 => SEND()
# RESPONSE IN UTF8 => recv() => decode()
