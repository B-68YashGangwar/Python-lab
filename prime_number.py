n=int(input('Enter The Number'))
for i in range(2,n):
    if i % n == 0:
        print("Not a Prime.")
        break
else:
    print('Prime NO.')
    
