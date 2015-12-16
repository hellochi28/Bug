with open('inputbug.txt') as f:
    text=f.readlines()
f.close()
len_text = len(text)    

line0=text[0].split()
numBug=int(line0[0])
numPatch=int(line0[1])
Patch=[0]*numPatch
Bug=''
emp=''
table=[0]*(2**numBug)
tabletime=[0]*(2**numBug)
tabletimef=[0]*(2**numBug)
for i in range(0,numBug):
    Bug+='+'
    emp+=' '
for i in range(0,numPatch):
    Patch[i]=text[i+1].split()

table[0]=Bug

for i in range(1,len(table)):
    table[i]=emp



def search(P,tabletime):
    sec=0
    for a in range(0,len(table)):
        bug=list(table[a])
        for k in range(0,numPatch):
            
            j=0
            bugfix=''
            patchlaw=list(P[k][1])
            for i in range(0,numBug):
                if(patchlaw[i]=='O' or patchlaw[i]==bug[i] ):
                    j+=1
        #print j
            if j==numBug:
                ans=list(P[k][2])
                for i in range(0,numBug):
                    if(ans[i]=='O'):
                        bugfix+=bug[i]
                    elif(ans[i]=='+'):
                        bugfix+='+'
                    elif(ans[i]=='-'):
                        bugfix+='-'

                #print bugfix
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
                            print bugfix
                            
                            break
        print '\n'
    print table
    print tabletime
    flag=0
    for i in range(0,len(table)):
        if table[i]=='---':
            print 'Fastest sequence takes %d seconds'%tabletime[i]
            flag=1
       
    if flag==0:
        print 'Bugs cannot be fixed'
