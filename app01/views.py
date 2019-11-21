from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
from .models import *


def books(request):
    book_list = Book.objects.all()
    return render(request, 'books.html', locals())


def book_add(request):
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get("price")
        date = request.POST.get('date')
        publish_id = request.POST.get('publish_id')
        author_pk_list = request.POST.getlist('author_pk_list')
        book_obj=Book.objects.create(title=title,price=price,date=date,publish_id=publish_id)
        book_obj.authors.add(*author_pk_list)
        return redirect('/book/')
    # return HttpResponse('add')
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    return render(request, "add.html", locals())


def book_edit(request, edit_book_id):
    if request.method=="POST":
        title=request.POST.get('title')
        price=request.POST.get('price')
        date=request.POST.get('date')
        publish_id = request.POST.get('publish_id')
        author_pk_list = request.POST.getlist('author_pk_list')
        Book.objects.filter(pk=edit_book_id).update(title=title,price=price,date=date,publish_id=publish_id)
        book_obj=Book.objects.filter(pk=edit_book_id).first()
        book_obj.authors.set(author_pk_list)
        return redirect('/book/')
    edit_book=Book.objects.filter(pk=edit_book_id).first()
    publish_list=Publish.objects.all()
    author_list=Author.objects.all()

    return render(request,"edit.html",locals())
