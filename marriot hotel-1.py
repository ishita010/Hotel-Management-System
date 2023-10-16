import numpy as np
import pandas as pd
import matplotlib.pyplot as pl

ch=1
while ch!=-1:
    print('='*70)
    print("\t\t ST. MARRIOT HOTEL")
    print('\t\t\t 1. Rooms')
    print('\t\t\t 2. Staff')
    print('\t\t\t 3. Guests ')
    print('\t\t\t 4. Booking')
    print('\t\t\t-1. Exit')
    print('='*70)
    ch=int(input('enter your choice '))
    if ch==1:
        DF=pd.read_csv("Rooms.csv",index_col="Rid")
        opt=1
        while opt!=-1:
            print()
            print("ROOMS ")
            print()
            print(" 1. Add new Room")
            print(" 2. Remove a Room ")
            print(" 3. Change Room Rent")
            print(" 4. Display all Room details")
            print(" 5. Search by Roomid ")
            print(" 6. Sort the Data by category - Ascending")
            print(" 7. Sort the Data by category - Descending")
            print(" 8. vacantwise count of Room ")
            print(" 9. Pie Chart - Room in each category ")
            print("-1. Exit")
            print()
            opt=int(input("enter your choice "))
            if opt==1:
                s=input("enter Rid ")
                n=input("enter Category ")
                d=input("enter AC available or not ")
                cl=int(input("enter dailyrent "))
                h=input("enter vacant or not ")
                DF.loc[s]=[n,d,cl,h]
                DF.to_csv("Rooms.csv")
                print(DF)
                print("Room added successfully")
            elif opt==2:
                s=input("enter Rid ")
                DF.drop(s,inplace=True)
                DF.to_csv("Rooms.csv")
                print(DF)
                print("Room detail removed")
            elif opt==3:
                s=input("enter Rid ")
                print("Current  dailyrent is",DF.loc[s,"Dailyrent"])
                DF.loc[s,"Dailyrent"]=int(input("Enter new dailyrent "))
                DF.to_csv("Rooms.csv")
                print(DF)
                print("dailyrent changed")
            elif opt==4:
                print('='*70)
                print(DF)
                print('='*70)
            elif opt==5:
                s=input("enter Rid ")
                print(DF.loc[s])
            elif opt==6:
                print(DF.sort_values('Category'))
            elif opt==7:
                print(DF.sort_values('Category', ascending=False))
            elif opt==8:
                DF1=DF.groupby('Vacant')
                print(DF1.Category.count())
            elif opt==9:
                DF1=DF.groupby('Category')
                print(DF1)
                DF1.Category.count().plot(kind='pie', autopct="%d%%")
                pl.show()
                pl.title('Number of room in each category',fontsize=20)
            elif opt==-1:
                break
            else:
                print("choose the correct option")
    elif ch==2:
        DF=pd.read_csv("Staff.csv",index_col="stid")
        opt=2
        while opt!=-1:
            print()
            print("STAFF")
            print()
            print(" 1. Add new staff")
            print(" 2. Remove a staff ")
            print(" 3. Change staff salary")
            print(" 4. Display all staff details")
            print(" 5. Search by staffid ")
            print(" 6. Sort the Data by DOJ - Ascending")
            print(" 7. Sort the Data by age - Descending")
            print(" 8. Post wise count of staff ")
            print(" 9. Bar Chart - Staff member number of male & female ")
            print("-1. Exit")
            print()
            opt=int(input("enter your choice "))
            if opt==1:
                a=input("enter stid ")
                b=input("enter stname ")
                c=input("enter gender")
                d=int(input("enter  age"))
                e=input("enter  post ")
                f=input("enter DOJ")
                g=int(input("enter salary"))
                DF.loc[a]=[b,c,d,e,f,g]
                DF.to_csv("Staff.csv")
                print(DF)
                print("staff added successfully")
            elif opt==2:
                a=input("enter stid ")
                DF.drop(a,inplace=True)
                DF.to_csv("Staff.csv")
                print(DF)
                print("Staff detail removed")
            elif opt==3:
                a=input("enter stid ")
                print("Current  salary is",DF.loc[a,"salary"])
                DF.loc[a,"salary"]=int(input("Enter new salary "))
                DF.to_csv("Staff.csv")
                print(DF)
                print(" Staff Salary changed")
            elif opt==4:
                print('='*70)
                print(DF)
                print('='*70)
            elif opt==5:
                a=input("enter stid ")
                print(DF.loc[a])
            elif opt==6:
                print(DF.sort_values('doj'))
            elif opt==7:
                print(DF.sort_values('age', ascending=False))
            elif opt==8:
                DF1=DF.groupby('post')
                print(DF1.post.count())
            elif opt==9:
                DF1=DF.groupby('gender')
                DF1.gender.count().plot(kind='bar')
                pl.title('Number of male and female staff ',fontsize=20)
                pl.show()
            elif opt==-1:
                break
            else:
                print("choose the correct option")
    elif ch==3:
        DF=pd.read_csv("guest.csv",index_col="guestid")
        opt=1
        while opt!=-1:
            print()
            print("GUESTS")
            print()
            print(" 1. Add new guest")
            print(" 2. Remove a guest")
            print(" 3. Change phone number")
            print(" 4. Display all guest details")
            print(" 5. Search by guestid ")
            print(" 6. Sort the Data by gname - Ascending")
            print(" 7. gnamewise  count of guest ")
            print("-1. Exit")
            print()
            opt=int(input("enter your choice "))
            if opt==1:
                s=input("enter guestid")
                n=input("enter  gname")
                d=input("enter address")
                cl=int(input("enter phone no. "))
                DF.loc[s]=[n,d,cl]
                DF.to_csv("guest.csv")
                print(DF)
                print("guest added successfully")
            elif opt==2:
                s=input("enter guestid")
                DF.drop(s,inplace=True)
                DF.to_csv("guest.csv")
                print(DF)
                print("guest detail removed")
            elif opt==3:
                s=input("enter guestid")
                print("Current  phone no.  is",DF.loc[s,"phoneno"])
                DF.loc[s,"phoneno"]=input("Enter new phone no. ")
                DF.to_csv("guest.csv")
                print(DF)
                print("phone no. changed")
            elif opt==4:
                print('='*70)
                print(DF)
                print('='*70)
            elif opt==5:
                s=input("enter guestid")
                print(DF.loc[s])
            elif opt==6:
                print(DF.sort_values('gname'))
            elif opt==7:
                DF1=DF.groupby('gname')
                print(DF1.gname.count())
            elif opt==-1:
                break
            else:
                print("choose the correct option")
    elif ch==4:
        DF=pd.read_csv("Bookings.csv",index_col="Bookingid")
        opt=1
        while opt!=-1:
            print()
            print("BOOKINGS")
            print()
            print(" 1. Add new Booking  ")
            print(" 2. Remove a Booking")
            print(" 3. Change guest room")
            print(" 4. Display all booking details")
            print(" 5. Search by bookingid")
            print(" 6. Sort the Data by guestid- Ascending")
            print(" 7. Sort the Data by guestid - Descending")
            print(" 8. Check-in Date-wise count of booking ")
            print(" 9. Pie Chart - Discount on booking")
            print("-1. Exit")
            print()
            opt=int(input("enter your choice "))
            if opt==1:
                s=input("enter bookingid")
                n=input("enter  rid")
                e=input("enter guestid")
                d=input("enter checkin date")
                cl=input("enter checkoutdate ")
                h= int(input("enter rentamount"))
                g= int(input("enter discount"))
                v= int(input("enter netamount"))
                DF.loc[s]=[n,e,d,cl,h,g,v]
                DF.to_csv("Bookings.csv")
                print(DF)
                print("booking added successfully")
            elif opt==2:
                s=input("enter bookingid ")
                DF.drop(s,inplace=True)
                DF.to_csv("Bookings.csv")
                print(DF)
                print("booking detail removed")
            elif opt==3:
                s=input("enter bookingid")
                print("Current guestid is",DF.loc[s,"guestid"])
                DF.loc[s,"guestid"]=input("Enter new guestid")
                DF.to_csv("Bookings.csv")
                print(DF)
                print("guest room changed")
            elif opt==4:
                print('='*70)
                print(DF)
                print('='*70)
            elif opt==5:
                s=input("enter bookingid")
                print(DF.loc[s])
            elif opt==6:
                print(DF.sort_values('guestid'))
            elif opt==7:
                print(DF.sort_values('guestid', ascending=False))
            elif opt==8:
                DF1=DF.groupby('Checkin')
                print(DF1.Checkin.count())
            elif opt==9:
                DF1=DF.groupby('Discount')
                DF1.Discount.count().plot(kind='barh')
                pl.draw_all
                pl.title('Discount on booking',fontsize=20)
                pl.show()
            elif opt==-1:
                break
            else:
                print("choose the correct option")
    elif ch==5:
        break
    else:
        print("choose the correct option")
