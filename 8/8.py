#1
import pickle

with open('pi.txt') as file:
    pi = file.read()

bdate = '09012009'
if bdate in pi:
    bdate2 = int(bdate)
    print(f"{bdate2} Sizning tug'ulgan kuningiz ushbu jadvalda uchraydi")
else:
    print('Yo\'q uchramaydi')

#2
fayl = open('pi.txt')
pi = fayl.read()
pi = pi.replace('\n','')
pi = float(pi)
print(pi)
fayl.close()


#3
text = "3.14159"
number = float(text)

with open("pi_v2", "wb") as file:
    pickle.dump(number, file)
