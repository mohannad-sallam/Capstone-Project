from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    USER_TYPES = [("admin", "Admin"), ("user", "User")]
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} ({self.user_type})"


class Parts(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image_url = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.brand})"


class Review(models.Model):
    part = models.ForeignKey(Parts, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()

    class Meta:
        unique_together = ("part", "user")

    def __str__(self):
        return f"{self.user.username} rated {self.part.name} {self.rating}/5"


class Comment(models.Model):
    part = models.ForeignKey(Parts, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment_text = models.TextField()

    def __str__(self):
        return f"Comment by {self.user.username} on {self.part.name}"
