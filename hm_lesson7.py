def name():

    list1 = ['i','t','a','y']
    len_list1 = len(list1)

    for letter in range(len_list1):
        if letter%2==0:
           print(list1[letter].upper())
        else:
           print(list1[letter].lower())
    print(letter)
name()
