from logging import raiseExceptions
from multiprocessing import context
from this import d
from xml.dom.minidom import Document
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import logout,authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import DebtorForm, DocumentsForm, IntrestAmountForm
from .models import Debtor, DocumentImage, Documents, DocumentAmount, IntrestAmount, PaidUnpaid
from datetime import date, timedelta
from rest_framework.response import Response
from django.http import JsonResponse
import itertools
import datetime


# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user = authenticate(username=username, password=password)
        try:
            user = authenticate(username=User.objects.get(email = username), password=password)
        except:
            user = authenticate(username=username, password=password)

        # if len(username)==0:
        #     messages.success(request,"fill user name.")
        #     return render(request,"index.html")

        # elif len(password)==0:
        #     messages.success(request,"fill password.")
        #     return render(request,"index.html")

        
        if user:
            login(request, user)
            # messages.success(request, f"You are now logged in as {username}.")
            return redirect("home")
        else:
            messages.info(request,"Invalid username or password.")
            return render(request,"index.html")
    else:
        return render(request,"index.html")

def home(request):
    date = datetime.date.today() 
    todaymin = datetime.datetime.combine(datetime.date.today(),datetime.time.min)
    todaymax = datetime.datetime.combine(datetime.date.today(),datetime.time.max)
    month  = date.replace(
        month = date.month,
        day = 1 )
    monthmin = datetime.datetime.combine(month,datetime.time.min)
    monthmax = datetime.datetime.combine(last_day_of_month(date),datetime.time.max)
    
    dayduelist = PaidUnpaid.objects.filter(duedate__range=(todaymin,todaymax))
    daydue = dayduelist.count()
    dayduepaid = PaidUnpaid.objects.filter(duedate__range=(todaymin,todaymax),paid = True)
    dayduepaidcount=dayduepaid.count()
    daydueunpaid = PaidUnpaid.objects.filter(duedate__range=(todaymin,todaymax),paid = False)
    daydueunpaidcount=daydueunpaid.count()
    
    duemonthlist = PaidUnpaid.objects.filter(duedate__range=(monthmin,monthmax))
    duemonthlistcount =duemonthlist.count()

    duemonthpaidlist = PaidUnpaid.objects.filter(duedate__range=(monthmin,monthmax),paid = True)
    duemonthpaidlistcount =duemonthpaidlist.count()

    duemonthunpaidlist = PaidUnpaid.objects.filter(duedate__range=(monthmin,monthmax),paid = False)
    duemonthunpaidlistcount =duemonthunpaidlist.count()


    
    total = Documents.objects.all()
    a= int(0)
    for t in total :
        y = t.totalamount
        x= a+y
        a=x

    totalamount = a
    

    b=int(0)
    for p in total:
        y = p.paidamount
        x = b+y 
        b = x
    totalpaidamount = b

    unpaid = totalamount -totalpaidamount

    
    


    context = {'daydue':daydue,
    'dayduelist':dayduelist,
    'dayduepaid':dayduepaid,
    'daydueunpaid':daydueunpaid,
    'daypaidcount':dayduepaidcount,
    'dayunpaidcount':daydueunpaidcount,
    'duemonthlist':duemonthlist,
    'duemonthlistcount':duemonthlistcount,
    'duemonthpaidlist':duemonthpaidlist,
    'duemonthpaidlistcount':duemonthpaidlistcount,
    'duemonthunpaidlist': duemonthunpaidlist,
    'duemonthunpaidlistcount':duemonthunpaidlistcount,
    'totalamount':totalamount,
    'totalpaidamount':totalpaidamount,
    'unpaid':unpaid
    }

    return render(request=request, template_name="home.html",context=context)

def edit(request,pk):
    document = Documents.objects.get(id= pk)
    amount = DocumentAmount.objects.filter(debtor_id = document.id).last()
    print(amount)
	
    if request.method == 'POST':
        document = Documents.objects.get(id= pk)
        amount = DocumentAmount.objects.filter(debtor_id = document.id).last()
        document.totalamount = request.POST.get('totalamount')
        document.percentage = request.POST.get('percentage')
        document.save()
        
        messages.success(request, f'Your post has been updated!')

        return redirect('home')
    else:
        return render(request,"edit.html", {'document':document,'amount':amount})

def view(request,id):
   
    document = Documents.objects.get(id= id)

    documentamount = IntrestAmount.objects.filter(amount_id = id).last()

    img = DocumentImage.objects.filter(document_id = document.id)
    
    return render(request,"view.html",{'document':document,'img':img, 'documentamount':documentamount})

def billing(request):
    debt = Debtor.objects.all()
    if request.method == "POST":
                                    # deb = request.POST.get('debtor')
                                    # debtor = Debtor.objects.filter(id = deb)
                                    # totalamount = request.POST.get('totalamount')
                                    # percentage = request.POST.get('percentage')
                                    # documentamount = DocumentAmount(debtor=debtor,totalamount=totalamount,percentage=percentage)
                                    # documentamount.save()

        d = request.POST.get('debtor')
       
        form = DocumentsForm(request.POST,request.FILES)
        if form.is_valid():
           
            document = form.save()
            balance = document.totalamount
            to = datetime.date.today()
            due_date = to.replace(
            month = to.month + 1,
            day = to.day)
            print (due_date)
            # document.objects.create(document = document,duedate = due_date)
            document.duedate = due_date
            document.intamount = int(0)
            document.pendingdate = '0'
            document.reason = '0'
            document.result = '0'
            document.paid = int(0)
            document.paidamount = int(0)
            
            document.balanceamount = balance
            document.save()
            paid = PaidUnpaid(debtor= document,duedate =due_date)
            paid.save()


            files = request.FILES.getlist('file')
            for file in files:
                DocumentImage.objects.create(document = document,file = file)
            messages.info(request,'bill added') 
            return redirect('home')  
        else:
            print(form.errors)
            messages.info(request,'User Registration Failed')
            
            return render(request,'billing.html',{'form': form,'debt':debt})
    else:
        return render(request,"billing.html",{'debt':debt,'billno':incrementbillno()})

def billpayment(request):

    debt = Debtor.objects.all()

    if request.method == 'POST':


        id = request.POST.get('amount')
        print(id)
        pay = request.POST.get('pay')
        print(pay)
        duedate = request.POST.get('duedate')

        paid = request.POST.get('intrestamount')
        print(paid)
        debtor = Documents.objects.get(id=id)
        # total = debtor.totalamount
        # print(total)
        # print(type(total))

        damount = DocumentAmount.objects.filter(debtor_id=id).last()
        # try:
        #     total = damount.balanceamount
            
        # except:
        #     total = debtor.totalamount

        total = debtor.totalamount
        paidam = debtor.paidamount
        if pay=='0':
            # try:
            #     paidamount = damount.paidamount
            # except:
            #     paidamount = paid

            paidamount = paidam + int(paid)
            balance = total-int(paidamount)
            print(balance)
            duedate = request.POST.get('duedate')
            result = request.POST.get('result')
            print(result)
            pendingdate = request.POST.get('pendingdate')
            reason = request.POST.get('reason')
            fineamount = request.POST.get('fineamount')
            da = DocumentAmount(debtor =debtor,paidamount = paidamount,duedate =duedate,balanceamount = balance,fineamount =fineamount,reason = reason,pendingdate = pendingdate,result = result )
            da.save()
            debtor.paidamount = paidamount
            debtor.balanceamount = balance
            debtor.intamount = paid
            debtor.save()

            deb =Documents.objects.get(id=id)
            paidamount = deb.paidamount
            total = deb.totalamount

            # if paidamount==total:
            #     due_date = ''
            #     deb.duedate = due_date
            #     deb.save()
            messages.success(request, f'Bill has been updated!')
            return redirect('home')
            
        else:
        
            form = IntrestAmountForm(request.POST or None,request.FILES, )
           
                
            if form.is_valid():
                result = request.POST.get('result')
                duedate = request.POST.get('duedate')
            
                pendingdate = request.POST.get('pendingdate')
                reason = request.POST.get('reason')
                fineamount = request.POST.get('fineamount')
                
                form.save()

                paidamount = paidam + int(paid)
                
                due_date = debtor.duedate
                to = datetime.date.today()
                due_date = to.replace(
                month = to.month + 1,
                day = due_date.day)
                print (due_date)

                unpaid = PaidUnpaid.objects.filter(debtor_id = debtor.id).last()
                unpaid.paid = True
                unpaid.save()

                PaidUnpaid.objects.create(debtor = debtor,duedate = due_date)
                


                debtor.duedate = due_date
                
                debtor.result = result
                debtor.pendingdate = pendingdate
                debtor.reason = reason
                debtor.fineamount = fineamount
                debtor.intamount = paid

                debtor.save()
                messages.success(request, f'Your post has been updated!')
                return redirect('home')
            else:
                print(form.errors)
                messages.info(request, f'failed!')
                return redirect('home')

    else:
        return render(request,"billpayment.html",{'debt':debt})

        


def billingselect(request):
    if request.method == "POST": 
        name = request.POST.get('name')
        print(name)
        user = Debtor.objects.filter(id=name)
        users = Debtor.objects.get(id=name)
        print(users)

        data ={"user_id": users.user_id,'mobilenumber':users.mobilenumber,'address':users.address,'pic':users.profile.url}
        return JsonResponse(data)

def billpaymentselect(request):
    if request.method == "POST": 
        name = request.POST.get('name')
        
        users = Debtor.objects.get(id=name)
        user = Documents.objects.filter(debtor_id=users.id)



        options = {}
        for x in user:
            options[x.id] = x.docno



        data ={"user_id": users.user_id,
        'mobilenumber':users.mobilenumber,
        'address':users.address,
        'pic':users.profile.url,
        'bills':options
        }
        

        print(data)
        return JsonResponse(data)


def billselect(request):
    if request.method == "POST": 
        id = request.POST.get('id')
        print(id)
        bill = Documents.objects.get(id=id)
        d = bill.created_at
        dd = d.strftime('%d-%m-%Y')
        balance =bill.balanceamount
        




        data ={'totalamount':bill.totalamount,
        'percentage':bill.percentage,
        'date':dd,
        'balance':balance,
        }
        

        print(data)
        return JsonResponse(data)


def calculate(request):
    return render(request,"calculate.html")

def searchbase(request):
    return render(request,"search.html")

def adddatabase(request):
    if request.method == "POST": 
        first = request.POST["first_name"]  
        last = request.POST["last_name"]  
        form = DebtorForm(request.POST,request.FILES)
        if form.is_valid():  
                # form.cleaned_data['name'] = form.cleaned_data['first_name'] + form.cleaned_data['last_name']

                debtor = form.save() 
                full = first +" "+ last
                debtor.fullname = full
                debtor.save() 
                
                messages.success(request,f'{full}  Profile Created Successfully! ')
                return redirect('billing')  
        else:
            print(form.errors)
            messages.info(request,'User Registration Failed')
            
            return render(request,'adddatabase.html',{'user_id':increment_user_id(),'form': form})  
    else:
        return render(request,"adddatabase.html", {'user_id':increment_user_id()})   

def search(request):
    users = Debtor.objects.all()
    if request.method == "POST":   
        data = request.POST["data"]    
        if not data:
            messages.error(request,'Please Enter the correct Number ')
            return redirect('searchbase') 
        else:
            
            users1 = Debtor.objects.filter(user_id__iexact = data)
            users2 = Debtor.objects.filter(first_name__iexact = data)
            users3 = Debtor.objects.filter(fullname__iexact = data)
            users4 = Debtor.objects.filter(mobilenumber__iexact = data)
            users5 = Debtor.objects.filter(last_name__iexact = data)

            
            if users1:
                users=users1
            elif users2:
                users=users2
            elif users3:
                users=users3
            elif users4:
                users=users4
            elif users5:
                users=users5
            else:
                messages.info(request,'Not Match')
                return render(request, 'search.html',{'data':data});
            for use in users:
                users = Documents.objects.filter(debtor_id =use.id)

                if users:
                    return render(request, 'search.html',{'users':users,'data':data});
                else:
                    messages.info(request,'Not Match')
                    return render(request, 'search.html',{'data':data});
    else :  
        return render(request, 'search.html',{'users':users});
    # return render(request,"search.html")

def notification(request):
    post1 = IntrestAmount.objects.all()
    post2 = Debtor.objects.all()
    post3 = Documents.objects.all().order_by('-updated_at')
    post4 = DocumentAmount.objects.all()
    mairu = []
    print(post1)

    # for x in post1:
    #     mairu.append(x)

    # for x in post2:
    #     mairu.append(x)

    # for x in post3:
    #     mairu.append(x)

    # for x in post4:
    #     mairu.append(x)

    # print(mairu)
    # a =[]
    # for x in mairu:
    #     # print(x.updated_at)
    #     a.append(x.updated_at)

    # print(a)

      

    post = post3 
    return render(request,"notification.html", {'post':post})

def logout_request(request):
	logout(request)
	return redirect("index") 


def delete(request,id):   
    document = Documents.objects.get(id= id)
    document.delete()
    return redirect('home') 


def increment_user_id():
    last = Debtor.objects.last()
    if last == None:
        last = 0
    else:
        last = last.id
    last+=1
    return ( "DB022" "%03d" % last)

def incrementbillno():
    last = Documents.objects.last()
    if last == None:
        last = 0
    else:
        last = last.id
    last+=1
    return ( "BL022" "%04d" % last)



def last_day_of_month(date):
    next_month = date.replace(day=28) + datetime.timedelta(days=4)
    return next_month - datetime.timedelta(days=next_month.day)

 