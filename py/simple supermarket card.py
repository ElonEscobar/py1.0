print('WELCOME TO TUAMINI SUPERMARKET')
next_customer=input('is there another customer? :')

if next_customer in ('y','yes','Y'):
    name = input('customer name :')
    import os

    file = open("C:/Users/ADMIN/Desktop/r2.txt", 'w')
    file.write("thank you for shopping at Tuamini supermarket ")
    file = open("C:/Users/ADMIN/Desktop/r.txt", 'a')
    file.write(name)
elif next_customer in ('n','no','N'):
    print('ook')
