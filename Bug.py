with open('inputbp2.txt') as f:
    text=f.readlines()
f.close()
len_text = len(text)    

line0=text[0].split()
numBug=int(line0[0])
numPatch=int(line0[1])
P=[0]*numPatch
Bug=''
emp=''
table=[0]*(2**numBug)
tabletime=[0]*(2**numBug)
tabletimef=[0]*(2**numBug)
for i in range(0,numBug):
    Bug+='+'
    emp+=' '
for i in range(0,numPatch):
    P[i]=text[i+1].split()

table[0]=Bug

for i in range(1,len(table)):
    table[i]=emp

def search():
    global P
    sec=0
    for a in range(0,len(table)):
        bug=list(table[a])
        for k in range(0,numPatch):    
            j=0
            bugfix=''
            patch_condition=list(P[k][1])
            for i in range(0,numBug):
                if(patch_condition[i]=='O' or patch_condition[i]==bug[i] ):
                    j+=1
            if j==numBug:
                ans=list(P[k][2])
                for i in range(0,numBug):
                    if(ans[i]=='O'):
                        bugfix+=bug[i]
                    elif(ans[i]=='+'):
                        bugfix+='+'
                    elif(ans[i]=='-'):
                        bugfix+='-'
                flag=0
                for i in range(0,len(table)):
                    if table[i]==bugfix:
                        flag=1
                        sec=tabletime[a]+int(P[k][0])
                        if tabletime[i]>=sec :
                            tabletime[i]=int(P[k][0])                 
                if flag==0:
                    for i in range(0,len(table)):
                        if table[i]==emp:
                            table[i]=bugfix
                            tabletime[i]=tabletime[a]+int(P[k][0])
                            break
    flag=0
    for i in range(0,len(table)):
        if table[i]=='---':
            print 'Fastest sequence takes %d seconds'%tabletime[i]
            flag=1
       
    if flag==0:
        print 'Bugs cannot be fixed'
