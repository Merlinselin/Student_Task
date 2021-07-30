from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login,logout

# Create your views here.
from .models import Admin,StudentDetails,register_table

# Create your views here.

def home(request):
    return render(request,"index.html")


def studentdetails(request):
	return render(request,"studentdetails.html")

def studentdetails(request):
    try:
        Name=request.POST['Name']
        DOB=request.POST['DOB']
        Phone_Number=request.POST['Phone_Number']

        studdtls=StudentDetails(Name=Name,DOB=DOB,Phone_Number=Phone_Number)
		studdtls.save()
        return render(request,"studentdetails.html",{'msg5':"Details Added"})
    except Exception as e:
        print(e)
        return render(request,"studentdetails.html",{'msg6':"Cannot be Added"})


def admin(request):
	try:
		Name=request.POST['Name']
		DOB=request.POST['DOB']
		Phone_Number=request.POST['Phone_Number']
		
		admindtls=Admin(Name=Name,DOB=DOB,Phone_Number=Phone_Number)
		admindtls.save()
		return render(request,"admindetails.html")
	except Exception as e:
		print(e)
		return render(request,"admindetails.html")



def adminhome(request):
	return render(request,"adminhome.html")


def viewdetails(request):
	ob=StudentDetails.objects.all()
	return render(request,"viewdetails.html",{'ob':ob})



def deletedetails(request):
	try:
		Name=request.POST['Name']
		studdtls=StudentDetails.objects.filter(name=Name)
		studdtls.delete()
		return render(request,"studentdetails.html",{'msg3':Name+" ""Deleted"})
	except Exception as e:
		return render(request,"studentdetails.html",{'msg4':"Contact Cannot be Deleted"})
	


def updatename(request):
	try:
		old_name=request.POST['old_name']
		new_name=request.POST['new_name']
		studdtls=studentdetails.objects.get(name=Name)
		studdtls.Name=new_name
		studdtls.save()
		return render(request,"studentdetails.html",{'msg5':"Name Updated"})
	except Exception as e:
		return render(request,"studentdetails.html",{'msg6':"Name Cannot be Updated"})


def updatephonenumber(request):
	try:
		name=request.POST['name']
		new_number=request.POST['new_number']
		contactdtls=contacts.objects.get(name=name)
		contactdtls.phone_number=new_number
		contactdtls.save()
		return render(request,"contact.html",{'msg7':"Number Updated"})
	except Exception as e:
		return render(request,"contact.html",{'msg8':"Number Cannot be Updated"})

















def register(request):
	if request.method=="POST":
		fname=request.POST["first_name"]
		last=request.POST["last_name"]
		un=request.POST["username"]
		em=request.POST["email"]
		phn=request.POST["phn_number"]
		pwd=request.POST["psw"]
		rpwd=request.POST["psw-repeat"]
		tp=request.POST["utype"]

		usr=User.objects.create_user(username=un,email=em,password=pwd)
		usr.first_name=fname
		usr.last_name=last
		if tp=="admin":
			usr.is_staff=True
		usr.save()
		reg=register_table(user=usr,phone_number=phn)
		reg.save()
		return render(request,"registration/login.html",{"status":"{} Register Successfully".format(fname)})

	return render(request,"registration.html")



def user_login(request):
	if request.method=="POST":
		un=request.POST["username"]
		ps=request.POST["password"]
		
		user=authenticate(username=un,password=ps)
		if user:
			login(request,user)
			if user.is_superuser: 
				return redirect("/admin")
			if user.is_staff:
				return redirect("viewfeedback")
			if user.is_active:
				return redirect("adminhome")
	else:
		return render(request,'userlogin.html',{"status":"Invalid User Name or Password"})