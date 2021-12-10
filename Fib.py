n = int(input("no of terms"))
n1=0
n2=1
count = 0
if n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       nxt = n1 + n2
       n1 = n2
       n2 = nxt
       count+=1
