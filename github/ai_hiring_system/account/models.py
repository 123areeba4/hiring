from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# ✅ Job Model
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255)  # ✅ Ensure this field is present
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # ✅ Ensure this field is present
    skills_required = models.CharField(max_length=500, null=True, blank=True)  # ✅ Optional field
    experience_required = models.IntegerField(default=0)
    posted_at = models.DateTimeField(default=now)

    def _str_(self):
        return self.title

# ✅ Expert Model (Find Experts Feature)
class Expert(models.Model):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    location = models.CharField(max_length=255)  # Pakistan / Germany
    visa_status = models.CharField(max_length=255)  # "Yes" / "No"
    skills = models.TextField()  # Comma-separated skills
    experience = models.CharField(max_length=255)  # Beginner / Intermediate / Expert

    def _str_(self):
        return self.name

# ✅ Applicant Model (Job Seekers)
class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.CharField(max_length=500)
    experience = models.IntegerField(default=0)
    preferred_location = models.CharField(max_length=100)

    def _str_(self):
        return self.user.username

# ✅ Resume Analysis Model (AI Feature)
class Resume(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    resume_file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Resume of {self.applicant.user.username}"