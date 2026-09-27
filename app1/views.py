from django.shortcuts import render, HttpResponse, redirect
from  . import models
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):
    return render(request, "index.html")

def login_method(request):
    return render(request, "login.html")
    #return HttpResponse("This is login page!")

def view_matches(request, matchid):
    #if request.method == "GET":
        
        #print(matchname)
        print(matchid)
    
        #get all matche with id equals 1 from DB
    
        #how to pass data to HTML and display it using Jinja2?
        wejdan = {
            'matchname' :  matchid,
            "clubs" : [ 'RealMadrid' , "Barcalona", "Ac Milan", "Manchester Unuted"]
        
        }
    
        return render(request, "viewmatches.html", wejdan)
    #else:
        

def login(requset):
    if requset.method == "POST":
        # do the work
        my_username = requset.POST['username']
        my_password = requset.POST['password']
        user_id = requset.POST['user-id']
                
        user = models.User.objects.filter( username = my_username  )
        
        if len(user) > 0: # if true this mean that user object above contains data else None
            print(f' {my_username} - {my_password} - {user_id}')

            logged_user = user[0]
            if bcrypt.checkpw(  my_password.encode()  , logged_user.password.encode()  ):
                
                # if user exists 
                requset.session['myusername'] = logged_user.username
                requset.session['isLoggedIn'] = True
        
                return redirect('p')
            else:
                return redirect('/login')
        else: # if user does no exsit, redirect the user to login form.
            
            return redirect('/login')
    else:
        return render(requset, "error.html")
    
    
def profile(request):
    if 'isLoggedIn' in request.session:
        return render( request, "profile.html")
    else:
        return render(request, "error.html")

def home(request):
    return render( request, "home.html")


def viewusers(request):
    context = {
        "users" : models.get_users()
    }
    
    return render( request , "viewusers.html" , context)

#Get request
def createuserview(request):
    return render(request, "createuser.html")
    
#post request
def createuser(request):
    if request.method == "POST":
        # we have to add somthing
        errors = models.User.objects.reg_validation(request.POST)
        if len(errors) > 0:
            # we have errors    for key, value in errors.items():
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/createuser')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash   
            models.create_new_user(request.POST , pw_hash)        
            return redirect("/viewallusers")
    else:
        return render(request, "index.html")
    
    
