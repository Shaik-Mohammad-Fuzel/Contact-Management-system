from django.db import connection
from django.shortcuts import render, redirect,get_object_or_404
from .models import ContactModel
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.urls import reverse
'''
def dashboard(request):
    contacts = ContactModel.objects.all().order_by("first_name")
    return render(request,'dashboard.html', {"contacts": contacts})
'''
def dashboard(request):
    contacts = []
    sql_query="""select * from contactsapp_contactmodel order by first_name ASC """
    with connection.cursor() as cursor:
            cursor.execute(sql_query)
            results=cursor.fetchall()
    for i in results:
        contacts.append({
            "slno": i[0],
            "first_name": i[1],
            "last_name": i[2],
            "email": i[3],
            "number": i[4],
            "address": i[5],
            "gender": i[6],
        })


    return render(request,'dashboard.html', {"contacts": contacts})
def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  
    else:
        form = ContactForm()
    return render(request, "add_contact.html", {"form": form})
'''
def contact_list(request):
    contacts = ContactModel.objects.all()  # Fetch all contacts
    return render(request, "contact_list.html", {"contacts": contacts})
'''

def update_contact(request, pk):
    if request.method == "POST":
    
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        address = request.POST.get("address")
        gender = request.POST.get("gender")

        
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE contactsapp_contactmodel 
                SET first_name=%s, last_name=%s, email=%s, number=%s, address=%s, gender=%s
                WHERE slno = %s
            """, [first_name, last_name, email, number, address, gender, pk])

        return HttpResponseRedirect(reverse('dashboard'))  
    

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM contactsapp_contactmodel WHERE slno = %s", [pk])
        contact = cursor.fetchone()

    if contact:
        contact_data = {
            "slno": contact[0],
            "first_name": contact[1],
            "last_name": contact[2],
            "email": contact[3],
            "number": contact[4],
            "address": contact[5],
            "gender": contact[6],
        }
    else:
        contact_data = {}

    return render(request, "update_contact.html", {"contact": contact_data})
"""
def delete_contact(request, pk):
    contact = get_object_or_404(ContactModel, slno=pk)  # Use slno instead of id
    contact.delete()
    return HttpResponseRedirect(reverse('dashboard'))"
    """""
def delete_contact(request, pk):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM contactsapp_contactmodel WHERE slno = %s", [pk])

    return HttpResponseRedirect(reverse('dashboard'))

def search_contact(request):
    search_param = request.GET.get("search", "").strip()
    contacts = []

    if search_param:
        sql_query = """
            SELECT slno, first_name, last_name, email, number, address, gender
            FROM contactsapp_contactmodel 
            WHERE first_name LIKE %s OR last_name LIKE %s 
        """
        search_value = f"%{search_param}%"

        with connection.cursor() as cursor:
            cursor.execute(sql_query, [search_value, search_value])
            results = cursor.fetchall()

        for result in results:
            contacts.append({
                "slno": result[0],
                "first_name": result[1],
                "last_name": result[2],
                "email": result[3],
                "number": result[4],
                "address": result[5],
                "gender": result[6],
            })

    return render(request, "dashboard.html", {"contacts": contacts, "search_query": search_param})
def view_contact(request, pk):
    contact = None
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM contactsapp_contactmodel WHERE slno = %s", [pk])
        result = cursor.fetchone()

    if result:
        contact = {
            "slno": result[0],
            "first_name": result[1],
            "last_name": result[2],
            "email": result[3],
            "number": result[4],
            "address": result[5],
            "gender": result[6],
        }

    return render(request, "view_contact.html", {"contact": contact})