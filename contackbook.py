contacts={}

while True:
    print('Contact book application')
    print('1.create contact')
    print('2.View contact')
    print('3.Update contact')
    print('4.Delete contact')
    print('5.Search contact')
    print('6.Count contact')
    print('7.Exit')

    choice =input('Enter your choice=')
    if choice=='1':
        name=input('Enter you name=')
        if name in contacts:
            print(f'Contacts name {name}alredy exists!')
        else:
            age=input('Enter age=')
            email=input('enter email=')
            mobile=input('Enter mobile number=')
            contacts[name]={'age':int(age),'email':email,'mobile':mobile}
            print(f'contact name {name} has been create succesflly')
    
    elif choice=='2':
        name=input('Enter view the contact=')
        if name in contacts:
            contact=contacts[name]
            print(f'Name:{name},Age:{age},Mobile number;{mobile}')
        else:
            print('contact not found!')
    elif choice=='3':
        name=input('Enter name to update contact=')
        if name in contacts:
            age=input(' Enter update age=')
            email=input('enter update email=')
            mobile=input('Enter update mobile number=')
            contacts[name]={'age':int(age),'email':email,'mobile':mobile}
        else:
            print('Contact not found!')

    elif choice=='4':
        name=input('Enter the delete contact=')
        if name in contacts:
            del contacts[name]
            print(f'contact name{name} has been delete successfully')
        else:
            print('contact not found')
    
    elif choice=='5':
        search_name=input('Enter the Search contact=')
        found=False
        for name,contacts in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found-Name{name},Age:{age},moblie number:{mobile},email:{email}')
                found=True
            if not found:
                print('no contact found with that name')
    elif choice=='6':
        print(f'Total contacts in your book:{len(contacts)}')

    elif choice=='7':
        print('Good byy.. you closeing the contact application')
        break
    else:
        print('invalid choice')


                




              





