def name():
   list1 = ['i','t','a','y']
   len_list1 = len(list1)

   for letter in range(len_list1):
      if letter%2==0:
         print(list1[letter].upper(),end = "")
      else:
         print(list1[letter].lower(),end = "")
name()

def division():
   num1 = int(input("enter a number:",))
   num2 = int(input("enter a number:",))

   if num2==0:
      print("num1/num2=-1")
   else:
      print(num1/num2)
division()

def combain():
   str1 = str(input("enter a string:",))
   str2 = str(input("enter a string:",))

   if len(str1)>len(str2):
      print(str1+str2) 
   else:
      print(str2+str1)
combain()

