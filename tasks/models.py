from django.db import models

def getChoices():
    return [("Low", "Low"), ("Medium", "Medium"), ("High", "High")]

class Todo(models.Model):
    name = models.CharField(max_length = 100)
    priority = models.CharField(choices = getChoices(), default = "Low", max_length = 50)
    description = models.TextField(max_length = 500)
    imgUrl = models.URLField()
    isCompleted = models.BooleanField()

    def __str__(self):
        return f"{self.name} {self.priority} {self.isCompleted}"
