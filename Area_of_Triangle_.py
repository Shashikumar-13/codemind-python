a,b,c=map(int,input().split())
s=(a+b+c)/2
z=s*(s-a)*(s-b)*(s-c)
area=z**0.5
print("{:.2f}".format(area))
