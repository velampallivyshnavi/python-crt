'''Write a python program
-->Add confirmed guests to the list
-->Remove a guest who cancels
-->Check if a friend is on list
-->Sort and print the final guest list'''

Guest_List=[]
while(True):
    print("***********MENU**********")
    print("1.Add the Guest") 
    print("2.Remove the guest who can cancels")
    print("3.Check if a Guest is attending the party or not")
    print("4.View the Final Guest List")
    print("5.Exit")
    print("-------------------------")
    Choice=int(input("Enter your choice :"))
    if(Choice>=1 and Choice<=5):
        if(Choice==1):
            GuestName=input("Enter the Guest Name :")
            Guest_List.append(GuestName)
            print(f"{GuestName} is Added to Guest List...!")
        elif(Choice==2):
            CancelledGuest=input("Enter the Cancelled Guest Name :")
            if CancelledGuest in Guest_List:
                Guest_List.remove(CancelledGuest)
                print(f"{CancelledGuest} is removed from Guest List...!")
            else:
                print(f"{CancelledGuest} is not in Guest List...!")
        elif(Choice==3):
            CheckGuest=input("Enter the guest name to check :")
            if CheckGuest in Guest_List:
                print(f"{CheckGuest} is Attending the party...!")
            else:
                print(f"{CheckGuest} is Not Attending the party...!")
        elif(Choice==4):
            if(len(Guest_List)==0):
                print("Guest List is Empty...!")
            else:
                Guest_List.sort()
                print("Hurray Here's Your Final Guest List")
                print(Guest_List)
        else:
            print("Enjoy Your Party...!")
            break
    else:
        print("In-Valid Input")


