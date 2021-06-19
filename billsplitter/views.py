from django.shortcuts import render , redirect
from django.http import HttpResponse
import time
from copy import deepcopy
from .models import Photos
# Create your views here.
temper = []
temper1 = []
def home(request):
    return render(request , 'first.html')
def exit(request):
    global temper
    global namer
    global name_payer
    global name_nonpayer
    global amount_payer
    global temper1
    global u
    global frr
    global amount_decr
    global amount_debit1
    global amount_debit2
    global amount_tempdecr1
    global amount_tempdecr2
    global commpr 
    global commprall
    temper.clear()
    namer.clear()
    name_payer.clear()
    amount_payer.clear()
    temper1.clear()
    u = 0
    frr.clear()
    namer.clear()
    amount_decr= []
    amount_debit1= []
    amount_debit2 = []
    amount_tempdecr1 = []
    amount_tempdecr2 = []
    name_nonpayer = []
    commpr = []
    commprall = []
    return render(request , 'first.html')



def second(request):
    global temper
    return render(request , 'second.html' , {'checker':'False' , 'temp':temper})

def static(request):
    image = Photos()
    icon = "written"
    return render(request, 'bgb.html' , {'image':icon})

def secondback(request):
    global temper
    return render(request,'second.html',{'temp':temper})

def third(request):
    global temper
    global namer
    if(len(temper)==0):
        return render(request ,'second.html' ,{'errmsg' : 'Number of payers cannot be null', 'checker':'True'} )
    else:    
        return render(request ,'third.html',{'tempt':namer})
def thirdback(request):
    global namer
    global amount_payer
    for trt in range(len(amount_payer)-1 , -1 , -1):
        if(amount_payer[trt] == 0):
            amount_payer.pop(trt)

    return render(request,'third.html',{'tempt':namer})

def backtest(request):
    return render(request ,'third.html')
u = 0
frr = []
name_payer =[]
amount_payer = []
payer = []
def forth(request):
    global temper
    global temper1
    global u
    global frr
    global payer
    frr.append(u)
    global name_payer
    global amount_payer

    temp2 = request.POST.get('temp')
    temp1 = request.POST.get('temp1')
    if temp2.isalnum() == False or temp1.isnumeric() == False or temp1 == '0' :
        return render(request ,'modal.html' , {'checkblank' :'True' , 'blankmsg' : 'Please give proper input'})
    else:
        u+=1
        payer.append(u)
        name_payer.append(temp2)
        amount_payer.append(int(temp1))
        if(u>1 and (name_payer[u-2] == name_payer[u-1]) and (amount_payer[u-2] == amount_payer[u-1])):
            name_payer.pop(u-1)
            amount_payer.pop(u-1)
            payer.pop(u-1)
            u-=1
            return render(request,'second.html',{'temp':temper , 'temp1':temper1 , 'loop':frr , 'checker':'False'})
        
        else:
            temp = temp2 + '   -   Rs.'+ temp1
            temper.append(temp)
            temper1.append(temp1)
            return render(request,'second.html',{'temp':temper , 'temp1':temper1 , 'loop':frr , 'checker':'False'})


    
def modal(request):
    return render(request,'modal.html', { 'checkblank' :'False' })
def modalsec(request):
    return render(request,'modalsec.html',{ 'checkblanksec' :'True'})
namer =[]
count_nonpayer = 0
name_nonpayer = []
def fifth(request):
    global name_nonpayer
    global count_nonpayer
    global namer
    temp5 = request.POST.get('temp5')
    if temp5.isalnum() == False :
        return render(request ,'modalsec.html' , {'checkblanksec' :'True' , 'blankmsgsec' : 'Please give proper input'})
    else:
        count_nonpayer+=1
        namer.append(temp5)
        name_nonpayer.append(temp5)
        if(count_nonpayer >1 and (namer[count_nonpayer - 1] == namer[count_nonpayer - 2]) and (name_nonpayer[count_nonpayer -1] == name_nonpayer[count_nonpayer -2])):
            namer.pop(count_nonpayer -1 )
            name_nonpayer.pop(count_nonpayer -1)
            count_nonpayer-=1
            return render(request,'third.html',{'tempt':namer})
        else:
            return render(request,'third.html',{'tempt':namer})





def delete(request):
    global name_nonpayer
    global namer
    global count_nonpayer
    
    if(len(namer) > 0):
        kk = len(namer)-1
        namer.pop(kk)
        pp = len(name_nonpayer)-1
        name_nonpayer.pop(pp)
        count_nonpayer-=1

        return render(request,'third.html',{'tempt':namer})
    else:
        return render(request,'third.html')

def deleter(request):
    global name_payer
    global temper
    global amount_payer
    global payer
    global u 
    if(len(payer) > 0):
        u-=1
        ss = len(amount_payer) -1 
        amount_payer.pop(ss)
        rr = len(temper)-1
        temper.pop(rr)
        qq = len(name_payer)-1
        name_payer.pop(qq)
        mmm = len(payer) -1
        payer.pop(mmm)
        c = len(payer)
        return render(request,'second.html',{'temp':temper} )
    else:
        return render(request,'second.html')

def test(request):
    amount_decr = []
    amount_debit1 = []
    amount_debit2 = []
    amount_tempdecr1 = []
    amount_tempdecr2 = []
    commpr =[]
    commprall =[]
    pers_get_count = 0 
    global amount_payer
    global name_payer
    global name_nonpayer
    global payer
    for pp in range(0,len(amount_payer)-1):
        for qq in range(0,len(amount_payer)-1):
            if(amount_payer[qq]-amount_payer[qq+1]<0):
                temp_swap = amount_payer[qq+1]
                amount_payer[qq+1] = amount_payer[qq]
                amount_payer[qq] = temp_swap
                temp_swap_name = name_payer[qq+1]
                name_payer[qq+1] = name_payer[qq]
                name_payer[qq] = temp_swap_name
    amount_total = 0
    num = len(name_payer) + len(name_nonpayer)
    payer1 = len(payer)
    diff = num - len(payer)

    for ff in range(0,diff):
        amount_payer.append(0)
    for i in range(0,payer1):
        amount_total = amount_total + amount_payer[i]

    amount_each = amount_total//num

    for i in range(0,num):
        temp2 = amount_payer[i] - amount_each
        amount_decr.append(temp2)
    for p in range(0,payer1):
        if(amount_decr[p] >= 0):
            pers_get_count+=1
            first_pr = "\n"+ ' ' + name_payer[p]+' ' + "will get a total amount of Rs." + ' ' + str(abs(amount_decr[p])) + '\n'
            commprall.append(first_pr)
 

    for i in range(0,pers_get_count):
        temp10 = amount_decr[i]
        amount_tempdecr1.append(temp10)
        for j in range(pers_get_count,num):
            temp11 = amount_decr[j]
            amount_tempdecr2.append(temp11)
            if(amount_decr[j]!=0):
                if((amount_tempdecr1[i]-(0-amount_decr[j]))==0):
                    if(payer1 >= j+1):
                        second_pr = "\n" + ' ' + name_payer[i]+ ' ' + "will get Rs." + ' ' + str(abs(0-amount_decr[j])) + ' ' + "from" + ' ' + name_payer[j] + ' '
                    else:
                        k = j- payer1
                        second_pr = "\n" + ' ' + name_payer[i]+ ' ' + "will get Rs." + ' ' + str(abs(0-amount_decr[j])) + ' ' + "from" + ' ' + name_nonpayer[k] + ' '                   
                    commpr.append(second_pr)
                    amount_tempdecr1[i] = 0
                    amount_decr[j] = 0
                    break
                
                if((amount_tempdecr1[i]-(0-amount_decr[j]))>0):
                                
                    temp4 = 0-amount_decr[j]
                    amount_debit1.append(temp4)
                    if(payer1 >= j+1):
                        third_pr = "\n" + ' ' + name_payer[i] + ' ' + "will get Rs." + ' ' + str(abs(temp4)) + ' ' + "from" + ' ' + name_payer[j]
                    else:
                        k= j- payer1
                        third_pr = "\n" + ' ' + name_payer[i] + ' ' + "will get Rs." + ' ' + str(abs(temp4)) + ' ' + "from" + ' ' + name_nonpayer[k]
                    commpr.append(third_pr)
                    amount_tempdecr1[i] = amount_tempdecr1[i] + amount_decr[j]
                    amount_decr[j]=0
                    
                
                if((amount_tempdecr1[i]-(0-amount_decr[j]))<0):
                
                    temp5 = (amount_tempdecr1[i]+amount_decr[j])
                    if(payer1 >= j+1):
                        fourth_pr = "\n" + ' ' + name_payer[i] + ' ' + "will get Rs." + ' ' + str(abs(amount_tempdecr1[i])) + ' ' + "from"+ ' ' + name_payer[j]
                    else:
                        k= j- payer1
                        fourth_pr = "\n" + ' ' + name_payer[i] + ' ' + "will get Rs." + ' ' + str(abs(amount_tempdecr1[i])) + ' ' + "from"+ ' ' + name_nonpayer[k]
                        
                    commpr.append(fourth_pr)
                    amount_debit2.append(amount_tempdecr1[i])
                    amount_decr.pop(j)
                    amount_decr.insert(j,temp5)
                    amount_tempdecr1[i] = 0
                    break

    return render(request ,'test.html' , {'commpr' : commpr , 'commprall': commprall } )