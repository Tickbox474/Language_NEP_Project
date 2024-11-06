from django.db import models
from django.contrib.auth.models import User

class QuizAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.CharField(max_length=100)
    selected_answer = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)
    score = models.IntegerField(default=0)  # Track score for each answer submission
    
    def __str__(self):
        return f"{self.user.username} - {self.quiz} - {self.selected_answer} - {self.score}"
    
class Score(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.points} points"
