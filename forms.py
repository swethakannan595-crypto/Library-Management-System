from django import forms
from .models import Book
from .models import IssueBook

class BookForm(forms.ModelForm):

    class Meta:

        model = Book

        fields = ['title', 'author', 'quantity']

from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = ['name', 'department']

class IssueBookForm(forms.ModelForm):

    class Meta:

        model = IssueBook

        fields = ['student', 'book']       

from django import forms
from .models import Book, Student, IssueBook


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class IssueBookForm(forms.ModelForm):
    class Meta:
        model = IssueBook
        fields = '__all__'