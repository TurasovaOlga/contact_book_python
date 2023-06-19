
contact={}



def display_contact():
    print("имя\t\t контактный номер")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
while True:
    choice = int(input("1. добавьте новый контакт \n 2.найдите контакт \n 3.показать контакт \n 4.отредактируйте контакт \n 5.удалите контакт \n 6.выход \n нажмите enter"))
    if choice == 1:
        name=input("введите имя контакта")
        phone=input("введите номер телефона")
        contact[name] = phone
    elif choice == 2:
        search_name = input("введите имя контакта")
        if search_name in contact:
            print(search_name,"'контактный номер пользователя",contact[search_name])  
        else :
            print("имени нет в книге контактов")    
    elif choice == 3:
        if not contact:
            print("пустая книга контактов")     
        else:
            display_contact()     
    elif choice == 4: 
        edit_contact = input("введие номер контакта который нужно отредактировать")
        if edit_contact in contact:
            phone = input ("введите номер мобильного телефона")  
            contact [edit_contact]=phone
            print("контакт обновлен")
            display_contact()
        else:
            print("имя не найдено в контактах") 
    elif choice == 5: 
        del_contact = input("введите контакт который нужно удалить")  
        if del_contact in contact:
            confirm = input("удалить этот контакт да/нет")    
            if confirm == 'да' or confirm == 'ДА':
                contact.pop(del_contact)   
            display_contact() 
        else:
            print("такой контакт не найден")    
    else:
        break        