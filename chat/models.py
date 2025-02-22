from django.db import models

class Session(models.Model):
    session_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session_id

class Message(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    sender = models.CharField(max_length=10)  # 'user' lub 'bot'
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} [{self.timestamp}]: {self.content[:50]}"

class Report(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    reported_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Report for Session {self.session.session_id} at {self.reported_at}"

class Prompt(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.name

class Context(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    embedding = models.BinaryField(blank=True, null=True)  # Można przechowywać wektor jako binarny

    def __str__(self):
        return self.title
