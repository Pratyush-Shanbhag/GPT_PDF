file = open('ocr_to_text.txt', 'rb')
#s = file.read().replace(b'\n', b'   ')
s = file.read()
'''a = b''
for c in range(len(s)):
    if s[c:c+1] != b'\n':
        a += s[c:c+1]'''

#print(s)
l = s.split(b'\n')
'''
for word in s.split(b'\n'):
    print(word)

print(len(s.split(b'\n')))
'''

for i in range(len(l)):
    if b'Service For' in l[i]:
        l[i] = b'Your Account Summary ' + b'Service For: ' + l[i+1][:l[i+1].index(b' Amount Due')]
        l[i+1] = l[i+1][l[i+1].index(b'Amount Due'):]
    if b'Account Number' in l[i]:
        d2 = l[i+1].split(b' ')
        l[i] = b'Account Number: ' + d2[0] + b' Due Date: ' + d2[1] + b' Total Amount Due: ' + d2[2] + b' Amount Enclosed: ' + d2[3]
        l.pop(i+1)
        break

f = open('ocr_text_filtered.txt', 'wb')
f.write(l[0])
for i in range(1, len(l)):
    f.write(b'\n')
    f.write(l[i])
    
f.close()