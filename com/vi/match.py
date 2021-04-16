# _*_ coding:UTF-8 _*_
import re

s = r'ABC\_-001'
# print re.match(r'^\d{3}-\d{3,8}$', '010-12345')
# print re.match(r'^\d{3}-\d{3,8}$', '010 12345')

m = re.match(r'^(\d{3})-(\d{3,8}$)', '010-12345')

# print m
# print m.group(0)
# print m.groups()
# print(s)


def is_valid_email(addr):
    # email = r'^[0-9a-zA-Z.-#]+@\w+.com$'
    if re.match('^[a-zA-Z\.]+@\w+.com$', addr):
        return True
    else:
        return False

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

def name_of_email(addr):
    email  = '^<*([\w+\s*]*)>*[\s*\w+]*@\w+.(com|org)'
    m = re.match(email,addr)
    print m.groups()
    if m:
        return m.group(1)
    else:
        return None
# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')