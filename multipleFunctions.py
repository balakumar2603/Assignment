class multipleFunctions:
    def Subfields():
        ai=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for items in ai:
            print (items)
    
    def OddEven():
        number=int(input("Enter a number: "))
        if(number%2==0):
            print( number, " is Even number")
        else:
            print(number, " is Odd number")        
            
    def Eligible():
        person=input("Your Gender: ")
        age=int(input("Your Age: "))
        if((person=="Male" and age>20) or (person=="Female" and age>17)):
            print("Eligible")
        else:
            print("Not Elible")

    def Percentage():
        subject1=int((input("Subject1: ")))
        subject2=int((input("Subject2: ")))
        subject3=int((input("Subject3: ")))
        subject4=int((input("Subject4: ")))
        subject5=int((input("Subject5: ")))
        Total= subject1 + subject2 + subject3 + subject4 + subject5
        print("Total: ", Total)
        print('%.13f' % (Total/5))

    def Triangle():
        height=int(input("Height: "))
        breadth=int(input("Breadth: "))
        print("Area of formulae: (Height*Breadth/2)")
        print("Area of Triangle: ", height*breadth/2)
        height1=int(input("Height1: "))
        height2=int(input("Height2: "))
        breadth1=int(input("Breadth: "))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ", height1+height2+breadth1)


