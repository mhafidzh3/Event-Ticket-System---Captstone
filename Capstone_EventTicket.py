from tabulate import tabulate

# Event Ticket System

# data_event = {Event Name, Location, Seat Amount, Ticket Price, Date, Desc, Status}
data_event = [
            {'Event Name':'Concert AK',
            'Location':'JP Plaza Dome',
            'Date':'15-01-2026',
            'Seat Amount':150,
            'Ticket Price':6000,
            'Status':'',
            'Desc':'AK 3rd Anniversary Concert Festival', 
            'Code':'AK'},
            {'Event Name':'Concert WW',
            'Location':'Jaya Arena Dome',
            'Date':'20-03-2026',
            'Seat Amount':250,
            'Ticket Price':4500,
            'Status':'',
            'Desc':'WW Music Studio Debut Concert',
            'Code':'WW'},
            {'Event Name':'Concert UM',
            'Location':'Grand Hall Gedung Emas',
            'Date':'18-02-2026',
            'Seat Amount':0,
            'Ticket Price':7000,
            'Status':'',
            'Desc':'UM - 4th World Wide Tour: 2nd Spot',
            'Code':'UM'},
            {'Event Name':'Concert AB',
            'Location':'Merpati Studio Dome',
            'Date':'20-01-2026',
            'Seat Amount':325,
            'Ticket Price':4000,
            'Status':'Unavailable',
            'Desc':'AB Collab with CY Concert Duolive',
            'Code':'AB'}
            ] 

# data_event = {Event Name, Location, Date, Seat Amount, Ticket Price, Status, Desc, Code}
def event_listG():
    global list_event
    list_event = [[],[],[],[],[],[],[],[],[],[]]
    for n in range(len(data_event)):
        if data_event[n]['Status'] != 'Unavailable':
            if data_event[n]['Seat Amount'] == 0:
                data_event[n]['Status'] = 'Sold Out'
            else:
                data_event[n]['Status'] = 'Available'

        list_event[0].append((n+1))
        list_event[1].append(data_event[n]['Event Name'])
        list_event[2].append(data_event[n]['Location'])
        list_event[3].append(data_event[n]['Date'])
        list_event[4].append(data_event[n]['Seat Amount'])
        list_event[5].append(data_event[n]['Ticket Price'])
        list_event[6].append(data_event[n]['Status'])
        list_event[7].append(data_event[n]['Desc'])
        list_event[8].append(data_event[n]['Code'])

def show_eventG():
    event_listG()
    zip_event = list(zip(list_event[0], list_event[1], list_event[2], list_event[3], list_event[4], list_event[6], list_event[7]))
    tabulate_event = tabulate(tabular_data = zip_event,
                               headers = ["No", "Event Name", "Location", "Date", "Seat Amount", "Status", "Desc"],
                               tablefmt = "double_grid")
    print(tabulate_event)

def add_eventA():
    add_EventName = input('Input Event Name: ')
    add_Location = input('Input Event Location (Stage Name): ')
    add_SeatAmount = int(input('Input Seat Amount: '))
    add_TicketPrice = int(input('Input Ticket Price: '))
    add_Date = input('Input Event Date (DD-MM-YYYY): ')
    add_Desc = input('Input Event Description: ')
    add_Status = ''
    if add_SeatAmount == 0:
        add_Status = 'Sold Out'
    else:
        add_Status = 'Available'
    while True:
        add_Code = input('Input Event Code: ')
        for n in range(len(data_event)):
            if data_event[n]['Code'] == add_Code:
                print("\n<!> Code already exist | Input new one <!>\n")
                break
        break
    data_event.append({
        'Event Name':add_EventName,
        'Location':add_Location,
        'Seat Amount':add_SeatAmount,
        'Ticket Price':add_TicketPrice,
        'Date':add_Date,
        'Desc':add_Desc,
        'Status':add_Status,
        'Code':add_Code
    })

def event_codeG(event_code):
    for n in range(len(data_event)):
        if data_event[n]['Code'] == event_code:
            break
    return n
            
def change_eventA():
    while True:
        n = (int(input("Input Event Number to Change: "))-1)
        if n > len(data_event) or n < 0:
            print("\n<!>== Invalid Option ==<!>\n")
            continue
        else:
            break
        
    info_no = [i+1 for i in range(len(data_event[n]))]
    event_key = ['Event Name', 'Location', 'Seat Amount', 'Ticket Price', 'Date', 'Status', 'Desc', 'Code']
    event_info = [data_event[n]['Event Name'], 
                  data_event[n]['Location'],
                  data_event[n]['Seat Amount'], 
                  data_event[n]['Ticket Price'],
                  data_event[n]['Date'],
                  data_event[n]['Status'],
                  data_event[n]['Desc'],
                  data_event[n]['Code']]
    zip_info = list(zip(info_no, event_key, event_info))
    tabulate_info = tabulate(tabular_data = zip_info,
                                headers = ['No', 'Type', 'Info'],
                                tablefmt = 'double_grid')
        
    print(tabulate_info)

    while True:
        type_change = (int(input('Input Type No to change: ')))
        
        if type_change == 1:
            new_EventName = input('Input New Event Name: ')
            data_event[n]['Event Name'] = new_EventName
        elif type_change == 2:
            new_Location = input('Input New Location: ')
            data_event[n]['Location'] = new_Location
        elif type_change == 3:
            new_SeatAmount = int(input('Input New Seat Amount: '))
            data_event[n]['Seat Amount'] = new_SeatAmount
        elif type_change == 4:
            new_TicketPrice = int(input('Input New Ticket Price: '))
            data_event[n]['Ticket Price'] = new_TicketPrice
        elif type_change == 5:
            new_Date = input('Input New Date: ')
            data_event[n]['Date'] = new_Date
        elif type_change == 6:
            print("""
                Status Change Option:
                1. Available
                2. Unavailable
                3. Sold Out (Seat Amount set to Zero)
                    """)
            status_change = int(input('Input Status Change Option: '))
            if status_change == 1:
                data_event[n]['Status'] = 'Available'
                if data_event[n]['Seat Amount'] == 0:
                    while True:
                        add_SeatAmount = int(input('Add Seat Amount: '))
                        if add_SeatAmount == 0:
                            print("\n<!>== Cannot add zero ==<!>\n")
                            continue
                        else:
                            data_event[n]['Seat Amount'] = add_SeatAmount
                            break
            elif status_change == 2:
                data_event[n]['Status'] = 'Unavailable'
            elif status_change == 3:
                data_event[n]['Status'] = 'Sold Out'
                data_event[n]['Seat Amount'] = 0
            else:
                print("\n<!>== Invalid Option ==<!>\n")
                    
        elif type_change == 7:
            new_Desc = input('Input New Desc: ')
            data_event[n]['Desc'] = new_Desc 
        elif type_change == 8:
            while True:
                new_Code = input('Input New Code: ')
                for n in range(len(data_event)):
                    if data_event[n]['Code'] == new_Code.upper():
                        print("\n<!> Code already exist | Input new one <!>\n")
                        break
                break
            data_event[n]['Code'] = new_Code
        else:
            print("\n<!>== Invalid Option ==<!>\n")
            continue
    
        change_again = input('Change another data (y/n): ')
        if change_again.lower() == 'y':
            continue
        elif change_again.lower() == 'n':
            break
        else:
            print("\n<!>== Invalid Option ==<!>\n")
            continue

# data_ticket = {Name, Event Name, Location, Date, Seat, Price, Ticket Status, Code}
# ticket Status = In Cart, Pending Payment, Valid, Cancelled 
data_ticket = []
counter_ticket = 0

def ticket_listA():
    global list_ticketA
    list_ticketA = [[],[],[],[],[],[],[],[],[],[]]
    for n in range(len(data_ticket)):
        list_ticketA[0].append((n+1))
        list_ticketA[1].append(data_ticket[n]['Name'])
        list_ticketA[2].append(data_ticket[n]['Event Name'])
        list_ticketA[3].append(data_ticket[n]['Location'])
        list_ticketA[4].append(data_ticket[n]['Date'])
        list_ticketA[5].append(data_ticket[n]['Seat'])
        list_ticketA[6].append(data_ticket[n]['Ticket Price'])
        list_ticketA[7].append(data_ticket[n]['Ticket Status'])
        list_ticketA[8].append(data_ticket[n]['Code'])

def show_ticketA():
    ticket_listA()
    zip_ticketA = list(zip(list_ticketA[0], list_ticketA[1], list_ticketA[2], list_ticketA[3], list_ticketA[4], list_ticketA[5], list_ticketA[6], list_ticketA[7], list_event[8]))
    tabulate_ticketA = tabulate(tabular_data = zip_ticketA,
                               headers = ["No", "Name", "Event Name", "Location", "Date", "Seat", "Ticket Price", "Ticket Status", "Code"],
                               tablefmt = "double_grid")
    print(tabulate_ticketA)

def ticket_listB():
    global list_ticketB
    list_ticketB = [[],[],[],[],[],[],[],[],[],[]]
    for n in range(len(data_ticket)):
        if data_ticket[n]['Name'] == User:
            list_ticketB[1].append(data_ticket[n]['Name'])
            list_ticketB[2].append(data_ticket[n]['Event Name'])
            list_ticketB[3].append(data_ticket[n]['Location'])
            list_ticketB[4].append(data_ticket[n]['Date'])
            list_ticketB[5].append(data_ticket[n]['Seat'])
            list_ticketB[6].append(data_ticket[n]['Ticket Price'])
            list_ticketB[7].append(data_ticket[n]['Ticket Status'])
            list_ticketB[8].append(data_ticket[n]['Code'])
            
    for i in range(len(list_ticketB[1])):
        list_ticketB[0].append((i+1))

def show_ticketB():
    ticket_listB()
    zip_ticketB = list(zip(list_ticketB[0], list_ticketB[1], list_ticketB[2], list_ticketB[3], list_ticketB[4], list_ticketB[5], list_ticketB[6], list_ticketB[7]))
    tabulate_ticketB = tabulate(tabular_data = zip_ticketB,
                               headers = ["No", "Name", "Event Name", "Location", "Date", "Ticket Price", "Ticket Status", "Code", "Seat"],
                               tablefmt = "double_grid")
    print(tabulate_ticketB)

def buy_eventB():
    global counter_ticket
    
    event_listG()
    zip_buy = list(zip(list_event[0], list_event[1], list_event[4], list_event[5], list_event[6]))
    tabulate_buy = tabulate(tabular_data = zip_buy,
                                  headers = ['No', 'Event Name', 'Seat Amount', 'Ticket Price', 'Status'],
                                  tablefmt = 'double_grid')
    print(tabulate_buy)
    print('\n <> Admin Fee is not included | Validated Ticket Cannot be Cancelled or Refunded <>\n')

    while True:
        again_value = False
        buy_index = (int(input("Chose Event Number to Buy: "))-1)
        if buy_index > len(data_event) or buy_index < 0:
            print("\n<!>== Invalid Option ==<!>\n")
            continue
        else:
            if data_event[buy_index]['Status'] == 'Unavailable' or data_event[buy_index]['Status'] == 'Sold Out':
                if data_event[buy_index]['Status'] == 'Unavailable':
                    print("\n<>== Event Unavailable ==<>\n")
                    continue
                elif data_event[buy_index]['Status'] == 'Sold Out':
                    print("\n<>== Event Seat Sold Out ==<>\n")
                    continue

            counter_ticket += 1
            admin_fee = data_event[buy_index]['Ticket Price'] * 0.1
            ticket_price = data_event[buy_index]['Ticket Price'] + admin_fee
            custom_code = f'{data_event[buy_index]['Code']}-{User.upper()}-{str(counter_ticket)}'
            while True:
                seat_taken = False
                chose_seat = int(input("Insert Seat Number: "))
                if chose_seat > data_event[buy_index]['Seat Amount']:
                    print("\n<!>== Seat Number higher than provided | Chose another seat ==<!>\n")
                    continue
                for n in range(len(data_ticket)):
                    code_split = data_ticket[n]['Code'].split('-',1)
                    code_original = code_split[0]
                    status = data_event[n]['Status']                   
                    if chose_seat == data_ticket[n]["Seat"] and data_event[n]['Code'] == code_original:
                        if status == 'In Cart' or status == 'Cancelled':
                            pass
                        else:
                            print("\n<>== Seat Already Taken | Chose Another Seat Number ==<>\n")
                            seat_taken = True
                            break
                if seat_taken == True:
                    continue
                else:            
                    break

            ticket = {'Name':User,
                      'Event Name':data_event[buy_index]['Event Name'],
                      'Location':data_event[buy_index]['Location'],
                      'Date':data_event[buy_index]['Date'],
                      'Seat':chose_seat,
                      'Ticket Price':ticket_price,
                      'Ticket Status':'In Cart',
                      'Code':custom_code} 
            data_ticket.append(ticket)
            pass

        while True:
            buy_again = input('Buy Another Ticket (y/n): ')
            if buy_again.lower() == 'y':
                break
            elif buy_again.lower() == 'n':
                again_value = True
                break
            else:
                print("\n<!>== Invalid Option ==<!>\n")
                continue
        if again_value == True:
            show_ticketA()
            break
        else:
            continue

def ticket_codeG(ticket_code):
    for n in range(len(data_ticket)):
        if data_ticket[n]['Code'] == ticket_code:
            break
    return n

def check_ticketB():
    show_ticketB()
    while True:
        if len(data_ticket) < 1:
            print("\n<!> No Ticket has been Purchased <!>\n")
            break

        select_ticket = (int(input("Input Ticket Number: "))-1)
        if select_ticket > len(list_ticketB[0]) or select_ticket < 0:
            print("\n<!>== Invalid Option ==<!>\n")
            continue
        else:
            ticket_no = ticket_codeG(list_ticketB[8][select_ticket])
            ticket_status = data_ticket[ticket_no]['Ticket Status']
            if ticket_status == 'Valid' or ticket_status == 'Cancelled':
                if ticket_status == 'Valid':
                    print('\n<> Ticket already Valid | Print your Ticket to enter Event <>\n')
                elif ticket_status == 'Cancelled':
                    print('\n<> Ticket has been cancelled <>\n')
                    del_cancel = input("Would you like to delete this Ticket (y/n): ")
                    if del_cancel.lower() == 'y':
                        data_ticket.pop(ticket_no)
                        break
                    elif del_cancel.lower() == 'n':
                        break
                    else:
                        print("\n<!>== Invalid Option ==<!>\n")
                        continue
            else:
                zip_select = [(list_ticketB[0][select_ticket],
                                list_ticketB[1][select_ticket],
                                list_ticketB[2][select_ticket],
                                list_ticketB[3][select_ticket],
                                list_ticketB[4][select_ticket],
                                list_ticketB[5][select_ticket], 
                                list_ticketB[6][select_ticket],
                                list_ticketB[7][select_ticket],
                                list_ticketB[8][select_ticket],)]
                selected_ticket = tabulate(tabular_data = zip_select,
                                            headers = ["No", "Name", "Event Name", "Location", "Date", "Seat", "Ticket Price", "Ticket Status", "Code", ],
                                            tablefmt = "double_grid")
                print(selected_ticket) 

            if ticket_status == 'In Cart':
                while True:
                    purchase_check = int(input("""
                                1. Proceed to buy Event Ticket
                                2. Cancel Event Ticket
                                3. Done Checking
                                
                                Input Option: """))

                    if purchase_check == 1:
                        data_ticket[ticket_no]['Ticket Status'] = 'Pending Payment'
                        pay_check = input(("\nWould you like to pay now (y/n): "))
                        if pay_check.lower() == 'y':
                            if data_user[no_user]['Balance'] > data_ticket[ticket_no]['Ticket Price']:
                                data_user[no_user]['Balance'] -= data_ticket[ticket_no]['Ticket Price']
                                no_event = event_codeG(data_ticket[ticket_no]['Code'])
                                data_event[no_event]['Seat Amount'] -= 1
                                data_ticket[ticket_no]['Ticket Status'] = 'Valid'
                                print("\n<>== Payment Successful | Print Ticket to Enter Event ==<>\n")
                                break
                            else:
                                print('\n<!>== Balance is not enough | Top Up Balance First ==<!>\n')
                                break
                        elif pay_check.lower() == 'n':
                            break
                        else:
                            print("\n<!>== Invalid Option ==<!>\n")
                            continue
                    elif purchase_check == 2:
                        cancel_check = input("\nAre you sure to Cancel this Event Ticket (y/n): ")
                        if cancel_check.lower() == 'y':
                            data_ticket[ticket_no]['Ticket Status'] = 'Cancelled'
                            break
                        elif cancel_check.lower() == 'n':
                            break
                        else:
                            print("\n<!>== Invalid Option ==<!>\n")
                            continue 
                    elif purchase_check == 3:
                        break
                    else:
                        print("\n<!>== Invalid Option ==<!>\n")
                        continue

            elif ticket_status == 'Pending Payment':
                while True:
                    pay_check = int(input("""
                                1. Proceed to pay Event Ticket
                                2. Cancel Event Ticket
                                3. Done Checking
                                          
                                Input Option: """))
                    if pay_check == 1:
                        if data_user[no_user]['Balance'] > data_ticket[ticket_no]['Ticket Price']:
                            data_user[no_user]['Balance'] -= data_ticket[ticket_no]['Ticket Price']
                            no_event = event_codeG(data_ticket[ticket_no]['Code'])
                            data_event[no_event]['Seat Amount'] -= 1
                            data_ticket[ticket_no]['Ticket Status'] = 'Valid'
                            break
                        else:
                            print('\n<!> Balance is not enough | Top Up Balance First <!>\n')
                            break
                    elif pay_check == 2:
                        cancel_check = input("Are you sure to Cancel this Event Ticket (y/n): ")
                        if cancel_check.lower() == 'y':
                            data_ticket[ticket_no]['Ticket Status'] = 'Cancelled'
                            break
                        elif cancel_check.lower() == 'n':
                            break
                        else:
                            print("\n<!>== Invalid Option ==<!>\n")
                            continue 
                    elif pay_check.lower() == 3:
                        break
                    else:
                        print("\n<!>== Invalid Option ==<!>\n")
                        continue
        break

def print_ticket():
    show_ticketB()
    while True:
        if len(data_ticket) < 1:
            print("\n<!> No Ticket has been Purchased <!>\n")
            break
        select_ticket = (int(input("Input Ticket Number: "))-1)
        if select_ticket > len(list_ticketB[0]) or select_ticket < 0:
            print("\n<!>== Invalid Option ==<!>\n")
            continue
        else:
            ticket_no = ticket_codeG(list_ticketB[7][select_ticket])
            ticket_status = data_ticket[ticket_no]['Ticket Status']
            if ticket_status == 'In Cart':
                print("\n<!> Validate your Ticket First before printing <!>\n")
                break
            elif ticket_status == 'Pending Payment':
                print("\n<!> Validate your Ticket First before printing <!>\n")
                break
            elif ticket_status == 'Cancelled':
                print("\n<!> Ticket is cancelled and cannot be printed <!>\n")
                break 
            elif ticket_status == 'Valid':
                data_one = (list_ticketB[1][select_ticket], list_ticketB[2][select_ticket], list_ticketB[3][select_ticket])
                data_two = (list_ticketB[0][select_ticket], list_ticketB[7][select_ticket], f'Seat Number = {list_ticketB[8][select_ticket]}')
                zip_print = [data_one, data_two]
                tabulate_print = tabulate(tabular_data = zip_print,
                                          headers = ['Event Entry Ticket', 'Enjoy the Event!'],
                                          tablefmt = 'fancy_grid')
                print(tabulate_print)
                break

# data_user = {Name, Password, Balance}   
data_user = []

def check_accountB():
    zip_user = [(data_user[no_user]['Name'],
                 data_user[no_user]['Balance'])]
    tabulate_user = tabulate(tabular_data = zip_user,
                             headers = ["Name", "Balance"],
                             tablefmt = 'double_grid')
    print(tabulate_user)

    pay_up = input('Would you like to Top Up (y/n): ')
    while True:
        if pay_up.lower() == 'y':
            top_up = int(input("Input Top Up amount: "))
            data_user[no_user]['Balance'] += top_up
            print("\n<> Top Up Successful <>\n")
            break
        elif pay_up.lower() == 'n':
            break

def menu_adminA():
    print("""
        Menu Option:
        1. Show Event Schedule
        2. Add Event
        3. Change Event Data
        4. Delete Event 
        5. Show Ticket
        6. Logout Account
        7. Exit System
        """)
    menu_option = int(input("Enter Menu Option: "))
    return menu_option

def menu_buyerB():
    print("""
          Menu Option:
          1. Show Event Schedule
          2. Buy Event Ticket
          3. Check Ticket 
          4. Print Ticket
          5. Check Account
          6. Logout Account
          7. Exit System
          """)
    menu_option = int(input("Enter Menu Option: "))
    return menu_option

def EntryG(access):
    if access.lower() == 'a':
        password = input("Enter password: ")
        if password == 'admin':
            return access
        else:
            print("\n <!>== Wrong Password ==<!>")
            return 'e'
    elif access.lower() == 'b':
        return access
    else:
        print("\n<!>== Invalid Entry Code ==<!>\n")
        return access

def buyer_accountB():
    while True:
        select_account = int(input("""
                    1. Log In
                    2. Register
                            
                    Input Option: """))
        print()
        
        if select_account == 1:
            user = input("Enter User Name: ")
            check_user = False
            for n in range(len(data_user)):
                if data_user[n]['Name'] == user:
                    check_user = True
                    user_index = n
                    break
                else:
                    continue
            if check_user != True:
                print("\n<!> User Name Is Not Registered <!>\n")
                continue
            user_password = input("Enter Password: ") 
            if user_password == data_user[user_index]['Password']:
                break    
            else:
                print("\n<!>== Wrong Password ==<!>\n")   
                continue
            
        elif select_account == 2:
            register_name = input("Register Name: ")
            user_exist = False
            for n in range(len(data_user)):
                if data_user[n]['Name'] == register_name:
                    print('\n<!> User Name Already Registered <!>\n')
                    user_exist = True
                    break
                else:
                    continue
            if user_exist == True:
                continue
            
            register_password = input("Register Password: ")
            input_balance = int(input('Input Initial Balance: '))
            add_account = {
                'Name':register_name,
                'Password':register_password,
                'Balance':input_balance,
                'Ticket':[]}
            data_user.append(add_account)
            continue
    return user_index

# <O>=====/\/\ || Main program || /\/\=====<O>

while True:
    exit_value = False
    print("\n<> == Main System == <>\n")
    entry = input("Enter as Admin or Buyer (a/b): ")
    account = EntryG(entry)

    # Access Admin
    if account.lower() == 'a':      
        while True:
            opsi_pilih = menu_adminA()
            opsi_pilih

            if opsi_pilih == 1:
                print("\n===== Show Event Schedule =====\n")
                show_eventG()
            elif opsi_pilih == 2:
                print("\n===== Add Event =====\n")
                add_eventA()                
                show_eventG()
                continue
            elif opsi_pilih == 3:
                print("\n===== Change Event Data =====\n")
                show_eventG()
                change_eventA()
                show_eventG()
                continue
            elif opsi_pilih == 4:
                print("\n===== Delete Event =====\n")
                show_eventG()
                del_index = (int(input("Input Event Number to Delete: "))-1)
                data_event.pop(del_index)
                show_eventG()
                continue
            elif opsi_pilih == 5:
                print("\n===== Show Ticket =====\n")
                show_ticketA()
                continue
            elif opsi_pilih == 6:
                print("\n===== Logout Account =====\n")
                break
            elif opsi_pilih == 7:
                print("\n===== Exit System =====\n") 
                exit_value = True
                break
            else:
                print("\n<!>== Invalid Option ==<!>\n")
                continue
    
    #Access Buyer
    elif account.lower() =='b':
        no_user = buyer_accountB()
        User = data_user[no_user]['Name']

        while True:
            opsi_pilih = menu_buyerB()
            opsi_pilih

            if opsi_pilih == 1:
                print("\n===== Show Event Schedule =====\n")
                show_eventG()
            elif opsi_pilih == 2:
                print("\n===== Buy Event Ticket =====\n")
                buy_eventB()
                continue
            elif opsi_pilih == 3:
                print("\n===== Check Ticket =====\n")
                check_ticketB()
                continue
            elif opsi_pilih == 4:
                print("\n===== Print Ticket =====\n")
                print_ticket()
                continue
            elif opsi_pilih == 5:
                print("\n===== Check Account =====\n") 
                check_accountB()
                continue  
            elif opsi_pilih == 6:
                print("\n===== Logout Account =====\n")
                break
            elif opsi_pilih == 7:
                print("\n===== Exit System =====\n")
                exit_value = True
                break
            else:
                print("\n<!>== Invalid Option ==<!>\n")
                continue
        
    else:
        print(exit_value)
        continue

    if exit_value == True:
        break
    