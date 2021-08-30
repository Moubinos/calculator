sum=0
number=int(input('insert first number '))
sum = number
fin=(input('insert '))
while fin != '=' :
    if fin == "+" :
        num2=int(input('insert next number '))
        sum = sum+num2
        print(sum)
    elif fin == "-" :
        num2=int(input('insert next number '))
        sum = sum-num2
        print(sum)
    elif fin == "*" :
        num2=int(input('insert next number '))
        sum = sum*num2
        print(sum)
    elif fin == "/" :
        num2=int(input('insert next number '))
        sum = sum/num2
        print(sum)
    fin=(input('insert '))
else:
    print(sum)
