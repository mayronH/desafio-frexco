import csv
import xlsxwriter
import io

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext

from users.models import CustomUser
from users.forms import SignUpForm

# Create your views here.

def index(request):
    """Index"""
    user = request.user
    return render(request, 'index.html', {
        "user": user,
    })
    
def signup(request):
    """User Sign Up"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            password = form.cleaned_data.get('password1')
            
            if not password:
                password = CustomUser.make_password()
                user.set_password(password)   
            
            user.refresh_from_db()
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def dashboard(request):
    """List of Users"""
    user_list = CustomUser.objects.order_by('date_joined')

    return render(request, 'dashboard.html', {'users' : user_list})

@login_required
def jsonUsers(request):
    user_list = list(CustomUser.objects.values())
    
    return JsonResponse(user_list, safe=False)

@login_required
def csvUsers(request):
    users = CustomUser.objects.all().values_list('username', 'birthdate', 'date_joined', 'last_login')
    
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="users.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['username', 'birthdate', 'date_joined', 'last_login'])
    
    for user in users: 
        writer.writerow(user)
        
    return response
    
@login_required
def xlsxUsers(request):  
    output = io.BytesIO()
    
    workbook = xlsxwriter.Workbook(output)
    
    title = workbook.add_format({
        'bold': True,
        'font_size': 18,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
    })
    header = workbook.add_format({
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'text_wrap': True,
        'border': 1
    })
    cell = workbook.add_format({
        'color': 'black',
        'text_wrap': True,
        'top': 1,
        'bottom': 1
    })
    
    worksheet = workbook.add_worksheet()
    
    title_text = u"Usuários Cadastrados"
    worksheet.merge_range('A2:E2', title_text, title)
    
    worksheet.write(2, 0, ("N"), header)
    worksheet.write(2, 1, ("username"), header)
    worksheet.write(2, 2, ("birthdate"), header)
    worksheet.write(2, 3, ("date_joined"), header)
    worksheet.write(2, 4, ("last_login"), header)

    users = CustomUser.objects.all()
    for index, user in enumerate(users): 
        row = 3 + index
        worksheet.write_number(row, 0, index + 1, cell)
        worksheet.write_string(row, 1, user.username, cell)
        worksheet.write(row, 2, user.birthdate.strftime('%d/%M/%Y'), cell)
        worksheet.write(row, 3, user.date_joined.strftime('%d/%M/%Y'), cell)
        if user.last_login != None:
            worksheet.write(row, 4, user.last_login.strftime('%d/%M/%Y'), cell)
        else:
            worksheet.write(row, 4, str(user.last_login), cell)
    
    workbook.close()

    output.seek(0)
    
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        headers={'Content-Disposition': 'attachment; filename="users.xlsx"'},
    )
    
    return response