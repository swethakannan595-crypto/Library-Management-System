from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class IssueBook(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    issue_date = models.DateField(auto_now_add=True)

    return_date = models.DateField(null=True, blank=True)

    returned = models.BooleanField(default=False)

    def __str__(self):

        return self.student.name    
