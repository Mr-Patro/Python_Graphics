def patro(str):
    lst=['a','e','i','o','u','A','E','I','O','U']
    for i in str:
        for x in lst:
            if i==x:
                print(i)
str=('peetabas is a good boy')
patro(str)
