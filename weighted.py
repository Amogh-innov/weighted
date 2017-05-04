def enmal():
    adj=[]
    mat={}
    nod=[]

    stop = False

    print()
    no = int(input("Enter the number of vertices in the graph : "))
    print()
    for i in range(no):
        print("Enter",i+1,"node                               ",end=': ')
        a=input()
        nod.append(a)
    print()
    for i in range(no):
        print()
        print("For node ",nod[i]," ,")
        while not stop:
            try:
                adk = int(input("Enter the number of adjacent nodes        : "))
                if adk < no:
                    stop = True
                else:
                    print()
                    print("Enter the value lesser than total number of nodes ! ! !")
                    print()
            except :
                print()
                print("Enter a number ! ! !")
                print()
        print()
        for k in range(adk):
            p=0
            ok = False
            while p<6 and not ok:
                ad = input("Enter the adjacent vertex                 : ")
                if ad in nod and ad not in adj and ad != nod[i]:
                    adj.append(ad)
                    ok = True
                elif p+1 == 6:
                    print()
                    print("Maximum attempts exceeded ! ! !")
                    ok=True
                else:
                    print()
                    print("Enter correct node ! ! !")
                    print()
                    p=p+1
            if p==5:
                break
        
        if len(adj) != adk:
            print()
            print("Invalid inputs ! ! !")
            break
        
        mat[nod[i]] = adj
        adj = []
        print()
        print("Nodes with adjacents so far               :-")
        print(mat)
        stop = False

    if p==5:
        return
         
    big = 0
    for i in mat :
        if len(mat[i]) > big :
            big = len(mat[i])

    for i in mat :
        if len(mat[i]) == big :
            adj.append(i)

    print()
    print("Highest weighted nodes                    : ")
    print(adj)

def enfil():
    import os
    if not(os.path.exists('ffil.txt')) :
            print("please check for file 'ffil.txt'")
            menu()
    else:
        opn = open("ffil.txt")
        v=1
        m1={}
        m2={}
        for line in opn:
            vai=line.split(',')
            vai.pop()
            print(v,vai[0])
            m1[v]=vai[0]
            v=v+1
        print()
        opn.close()
        ch1=int(input("Enter your choice                         : "))
        x=m1[ch1]
        opn1 = open(str(x),'r')
        print()
        print("Graph :- ")
        for lin in opn1:
            v1=[]
            val=lin.split(',')
            val.pop()
            print(val)
            for k in range(len(val)-1):
                v1.append(val[k+1])
                m2[val[0]]=v1
        opn1.close()
    big = 0
    for i in m2 :
        if len(m2[i]) > big :
            big = len(m2[i])
            
    print()        
    print("Highest weighted nodes/node are          :-")
    for i in m2 :
        if len(m2[i]) == big :
            print(i)
    
def menu():
    done = False
    while not done:
        try:
            print()
            print()
            print("1.Enter value manually ")
            print("2.Choose from the file ")
            print("3.Exit")
            print()
            ch = int(input("Enter your choice(1-3)                    : "))
            if ch == 1:
                enmal()
            elif ch == 2:
                enfil()
            elif ch == 3:
                done = True
            else:
                print()
                print("Enter appropriate input ! ! !")
        except:
            print()
            print("Enter appropriate input ! ! !")
menu()
