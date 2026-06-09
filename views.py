from django.shortcuts import render
from .models import Book, Student
from .forms import BookForm
from django.shortcuts import redirect
from .forms import BookForm, StudentForm
from django.shortcuts import get_object_or_404
from .forms import IssueBookForm


def home(request):

    total_books = Book.objects.count()
    total_students = Student.objects.count()

    context = {
        'total_books': total_books,
        'total_students': total_students,
    }

    return render(request, 'home.html', context)


def book_list(request):

    books = Book.objects.all()

    return render(request, 'book_list.html', {'books': books})

def book_list(request):

    query = request.GET.get('q')

    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()

    return render(request, 'book_list.html', {'books': books})

def student_list(request):

    students = Student.objects.all()

    return render(request, 'student_list.html', {'students': students})
def add_book(request):

    if request.method == 'POST':

        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book_list')

    else:

        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

def add_student(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('student_list')

    else:

        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})

def edit_book(request, id):

    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':

        form = BookForm(request.POST, instance=book)

        if form.is_valid():

            form.save()

            return redirect('book_list')

    else:

        form = BookForm(instance=book)

    return render(request, 'add_book.html', {'form': form})

def delete_book(request, id):

    book = get_object_or_404(Book, id=id)

    book.delete()

    return redirect('book_list')
    
def issue_book(request):

    if request.method == 'POST':

        form = IssueBookForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('home')

    else:

        form = IssueBookForm()

    return render(request, 'issue_book.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404

def edit_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'add_book.html', {'form': form})


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('book_list')