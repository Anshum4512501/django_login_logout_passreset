from django.shortcuts import render,redirect
from .models import User as M_User,Ticket
from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.models import User as DB_User
# Create your views here.


def signup(request,id=None):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        print(username)
        print(email)
        print(password)
        user = M_User(username=username,email=email,password=password)
        user.save()
        print("User from sign up ",user)
        return redirect('../signin')

    else:
        try:
            print("Inside try",id)
            user = M_User.objects.get(id=id)
            print("Inside try",id,user)
            return render(request,'register/signup.html',{"user":user})

        except:
            ObjectDoesNotExist
            return render(request,'register/signup.html')
def signin(request):
    if request.method=='GET':
        return render(request,'register/signin.html')
    else:    
        print("I am Inside singin else part")
        usrname=request.POST['username']
        password= request.POST['password']
        print("USERNAME IS",usrname)
        print("USERNAME IS",password)
        try:
            user = M_User.objects.get(username=usrname)
            print("FOUND USER NAME IN DB ",user)
            if user.username==usrname and user.password==password:
                print("User Found")
                print(user)
                return render(request,'register/signinsuccess.html',{"users":user})
            else:
                return render(request,'register/signin.html')
        except ObjectDoesNotExist:
            print("Either the entry or blog doesn't exist.") 
            return render(request,'register/signup.html')  
def signinsuccess(request):
    user_one = M_User.objects.all()
    print("User in sign in success",user_one)
    context = {
        "users":user_one
           }
    return render(request,'register/signinsuccess.html',context)            
def forgetpassword(request):
    return render(request,'register/forgetpassword.html')

def emailsuccess(request):
    return render(request,'register/emailsucces.html')

def taskinfo(request):
    return render(request,'register/department.html',{"department":""})
def ticketraising(request):
    if request.method=='POST':
        ticketnumber= request.POST['ticketnumber']
        date= request.POST['issue_creation_date']
        issue = request.POST['issue']
        issuedepatment= request.POST['issue_department']
        
        ticket = Ticket(ticketNumber=ticketnumber,issue_department=issuedepatment,issue=issue,issue_creation_date=date,is_this_new_ticket='y')
        print("Ticket is",ticket)
        ticket.save()
        return redirect('../raiseticket')
    else:
        return render(request,'register/raiseticket.html')    

def assignticket(request):
    ticket =Ticket.objects.all()
    totaltickets=Ticket.objects.count()
    print("Total tickets are ",totaltickets)
    context = {
        "tickets":ticket,
        "totaltickets":totaltickets
    }
    return render(request,'register/assignticket.html',context)        