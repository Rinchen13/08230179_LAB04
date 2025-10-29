from django.db import models

class Profile(models.Model):
    """Details about the student (aboutMe page)"""
    full_name = models.CharField(max_length=200)
    student_id = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    bio = models.TextField(help_text="Short bio about yourself / study interests", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class LearningEntry(models.Model):
    """One entry in your learning journey (index page shows these)"""
    title = models.CharField(max_length=200)
    date = models.DateField()
    content = models.TextField(help_text="Describe what you learned or did.")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.date})"

