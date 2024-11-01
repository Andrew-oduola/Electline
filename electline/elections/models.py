from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.exceptions import ValidationError



CustomUser = get_user_model()

# Create your models here.
class Election(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    allowed_prefix = models.CharField(
        max_length=100,
        help_text="Comma-separated list of matric prefixes allowed to vote (e.g., 'CSC, EEE, MTH').",
        null = True,
        blank=True
    )

    def __str__(self):
        return self.title
    
    def is_voter_allowed(self, matric_number):
        # Extract the first three letters of the matric number
        prefix = matric_number[:3].upper()
        # Check if the prefix is in the allowed prefixes list
        
        if self.allowed_prefix is not None:
            allowed_prefixes = [p.strip() for p in self.allowed_prefix.split(',')]
            return prefix in allowed_prefixes
        
        return True
    
    def get_absolute_url(self):
        return reverse("elections:vote", args=[self.slug])
    
    def clean(self) -> None:
        super().clean()
        if not (self.end_date > self.start_date):
            raise ValidationError("End date must be after start date.")
    


class Candidate(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE, related_name="candidates")
    name = models.CharField(max_length=100)
    matric_no = models.CharField(max_length=20, unique=True)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='candidate_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.election.title})"


class Vote(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="votes")
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='votes')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.matric_no} voted for {self.candidate.name} in {self.election.title}"

    class Meta:
        unique_together = ('user', 'election')

