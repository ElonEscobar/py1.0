import os
if os.path.exists('C:/Users/ADMIN/Desktop/shopping.txt'):
   os.remove('C:/Users/ADMIN/Desktop/shopping.txt')
else:
    print('this file does not exist')
