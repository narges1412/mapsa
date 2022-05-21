from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    class   Meta:
        unique_together = ("user", "name")

    def __str__(self) -> str:
        return self.name
   


class Todo(models.Model):
    title=models.CharField(max_length=255)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    due_date=models.DateField(null=True,blank=True)
    def __str__(self) -> str:
        return self.title

class Profile(User):
    
    img = models.ImageField(upload_to='profile/', null=True, blank=True)
    join_date = models.DateField(auto_now_add=True)
    age=models.PositiveIntegerField()
    
    class Meta:
        verbose_name = "Profile"
        