from datetime import date
from operations2 import Hotel

class Hotel:

    def __init__(self):
        self.rooms = {}
        self.available_rooms = {'std':[101,102,103],'delux':[201,202,203],'execu':[301,302,303],'suite':[401,402,403]}
        self.roomprice={1:2000,2:4000,3:5000,4:6000}

    def check_in(self, name,address,phone): 
        roomtype=int(input("room type:\n1.standard\n2.Deluxe\n3.Executive\n4.Suite\nselect a room type:"))
        if roomtype==1:
            if self.available_rooms['std']:
                room_no=self.available_rooms['std'].pop(0)
            else:
                print("sorry,standard room not available")    
                return
        elif roomtype==2:
            if self.available_rooms['delux']:
                room_no=self.available_rooms['delux'].pop(0)
            else:
                print("sorry,deluxe room not available")    
                return
        elif roomtype==3:
            if self.available_rooms['execu']:
                room_no=self.available_rooms['execu'].pop(0)
            else:
                print("sorry,executive room not available")    
                return        
        elif roomtype==4:
            if self.available_rooms['suite']:
                room_no=self.available_rooms['suite'].pop(0)
            else:
                print("sorry,suite room not available")    
                return
        else:
            print("choose a valid room type:")
        d,m,y=map(int,input('enter check-in-date in date,month,year: ').split())
        check_in=date(y,m,d)
        self.rooms[room_no] = {
            'name': name,
            'address':address,
            'phone':phone,
            'check_in_date':check_in,
            'room_type':roomtype,
            'roomservice':0
        } 
        print(f"cheked in {name},{address} to room: {room_no} on {check_in}")   

    def room_service(self,room_no):
            print('~~~~~~~~~~~~~~~~~~~~')
            print("||Royal Hotel Menu||")
            print('~~~~~~~~~~~~~~~~~~~~')
            print("1.Tea/coffee:Rs.100 2.Dessert:Rs.300 3.Breakfast:Rs.550 4.Lunch:Rs.800 5.Dinner:Rs.1000 6.Exit")
            while 1:
                c=int(input("select your choice: "))
                if c==1:
                    q=int(input("Enter the quantity: "))
                    self.rooms[room_no]['roomservice']+=100*q
                elif c==2:
                    q=int(input("Enter the quantity: "))
                    self.rooms[room_no]['roomservice']+=300*q
                elif c==3:
                    q=int(input("Enter the quantity: "))
                    self.rooms[room_no]['roomservice']+=550*q
                elif c==4:
                    q=int(input("Enter the quantity: "))
                    self.rooms[room_no]['roomservice']+=800*q
                elif c==5:
                    q=int(input("Enter the quantity: "))
                    self.rooms[room_no]['roomservice']+=1000*q  
                elif c==6:
                    break
                else:
                    print("Invalid option")
                print("Room service Rs:", self.rooms[room_no]['roomservice'],"\n")
            else:
                print('invaild room number:')                   

    def display_occupied(self):
        if not self.rooms:
            print("No rooms are occupied at the moment. ")
        else:
            print("Occupied Rooms:  ")
            print("-------------------------") 
            print('Rooms no.   Name.  Phone.')
            print("-------------------------")
            for room_number, details in self.rooms.items():
                print(room_number,'\t',details['name'],'\t',details['phone'])
                
    def check_out(self,room_number):
         if room_number in self.rooms:
            check_out_date = date.today()
            check_in_date = self.rooms[room_number] ['check_in_date']
            duration = (check_out_date - check_in_date) .days
            roomtype=self.rooms[room_number]['room_type']
            if roomtype==1:
                self.available_rooms['std'].append(room_number)
            if roomtype==2:
                self.available_rooms['delux'].append(room_number)
            if roomtype==3:
                self.available_rooms['execu'].append(room_number)
            if roomtype==4:
                self.available_rooms['suite'].append(room_number) 
            print('~~~~~~~~~~~~~~~~~~~~~~~')
            print('||Royal Hotel Recepit||')
            print('~~~~~~~~~~~~~~~~~~~~~~~')
            print(f"Name:{self.rooms[room_number] ['name']}\nAddress:{self.rooms[room_number] ['address']}")
            print(f"Phone:{self.rooms[room_number]['phone']}")
            print(f'Room Number:{room_number}')
            print(f"Check in date:{check_in_date.strftime('%d %B %Y')}")
            print(f'Check out date:{check_out_date.strftime("%d %B %Y")}')
            print(f'No.of Days:{duration}\tPrice per day:Rs.{self.roomprice[roomtype]}')
            roombill=self.roomprice[roomtype]*duration
            roomservice=self.rooms[room_number]['roomservice']
            print('Room bill:Rs.',roombill)
            print('Room service:Rs.',roomservice)
            print('Total bill: Rs.',roombill+roomservice)
            del self.rooms[room_number]
         else:
            print(f"Room(room_number) is not occupied.")

    def start_app(self):
        while True:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print('||Welcome To Royal Hotel||')
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("1.Check-in")
            print("2.Room service")
            print("3.Display Occupied Rooms")
            print("4.Check-out")
            print("5.Exit")
            choice = input("Enter your choice (1-5) : ")
            if choice == '1':
                name = input("Enter Client Name: ")
                address = input("Enter Address: ")
                phone = input("Enter contact no. ")
                self.check_in(name, address, phone)
            elif choice == '2':
                room_no = int(input("Enter room number: "))
                self.room_service(room_no)
            elif choice == '3':
                self.display_occupied()
            elif choice == '4':
                room_number = int(input("Enter room number: "))
                self.check_out(room_number)
            elif choice == '5':
                choice=input("||~~~I wish you all the best~~~||")
                break
            else:
                print("Invalid choice. Please try again. ")  

h=Hotel()
h.start_app()
