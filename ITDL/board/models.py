from django.db import models

# 1. 제목(title) - CharField
# 2. 내용(content) - TextField
# 3. 작성일자(created_at) - DateTimeField
# 4. 수정일자(updated_at) - DateTimeField

class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class TodoItem(models.Model):
    content = models.CharField(max_length=200)
    date = models.DateField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f"{self.date}: {self.content}"