
#Conditional Logic
is_old = True
is_licenced = True

if is_old and is_licenced:
    print('you are old enough to drive and you have  a license')
# elif is_licenced:
#     print('You have license')
else:
    print('You cant drive')

print('nice')
#Ternary Operator
#condition_1 if condition_2
condition_1 = True
condition_2 ='message allowed' if condition_1 else 'not allowed message'
print(condition_2)
#short Circuiting
if condition_1 or condition_2:
    print('it works')
#Logical Operator < > == <= >= != and or not


#Magic exercise
is_magician= False
is_experienced= True

if is_experienced and is_magician:
    print('you are a master magician')
elif is_magician and not(is_experienced):
    print('atleast you are getting it')
elif  not(is_magician):
    print('you need magic')
