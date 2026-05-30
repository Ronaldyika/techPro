from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    service = models.CharField(max_length=200, blank=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    title = models.CharField(max_length=200, blank=True)
    comment = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.rating}★"
