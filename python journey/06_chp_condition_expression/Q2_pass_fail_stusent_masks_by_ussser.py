sub1=int(input("enter the mark os sub1:"))
sub2=int(input("enter the mark os sub2:"))
sub3=int(input("enter the mark os sub3:"))
if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail study hard")
elif(sub1+sub2+sub3)/3<40:
    print("you are fail")
else:
    print("congulation! you are pass")