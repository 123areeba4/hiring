from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now  # For setting timestamp
from .forms import JobForm
from .models import Job
from django.http import HttpResponse

def apply_for_job(request):
    return HttpResponse("This is the Apply for Job page.")


from django.http import JsonResponse
from .models import Expert 

def job_list(request):
    jobs = Job.objects.all()  # Sab jobs fetch karo
    return render(request, 'accounts/job_list.html', {'jobs': jobs})
# Home View
def home(request):
    return render(request, 'accounts/home.html')

# Signup View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, 'signup.html')

        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        messages.success(request, "Signup successful! Please login.")
        return redirect('login')  # Redirect to login page

    return render(request, 'accounts/signup.html')

# Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})

# Logout View
def user_logout(request):
    logout(request)
    return redirect('home')

# Dashboard View
@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

# Post Job View
@login_required
def post_job(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)  # Save but don't commit yet
            job.posted_at = now()  # Set posted_at timestamp
            job.save()  # Save job after setting timestamp
            return redirect('dashboard')  # Redirect after posting job
    else:
        form = JobForm()
    
    return render(request, 'accounts/post_job.html', {'form': form})

# Job Recommendations View
@login_required
def job_recommendations(request):
    query = request.GET.get('query', '')
    jobs = Job.objects.filter(title__icontains=query)
    
    return render(request, 'accounts/recommendations.html', {'jobs': jobs, 'query': query})

from django.shortcuts import render, get_object_or_404
from .models import Job

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'accounts/job_detail.html', {'job': job})

from django.shortcuts import render
from .models import Expert

def find_expert(request):
    query = request.GET.get('query', '')  # Search query
    experts = Expert.objects.filter(profession__icontains=query) if query else Expert.objects.all()
    return render(request, 'accounts/find_expert.html', {'experts': experts, 'query': query})

from django.http import JsonResponse

from django.http import JsonResponse
from .models import Expert  # Tumhara expert ka model

def search_experts(request):
    profession = request.GET.get("profession", "")
    location = request.GET.get("location", "")
    visa_status = request.GET.get("visa_status", "")
    skills = request.GET.get("skills", "")
    experience = request.GET.get("experience", "")

    experts = Expert.objects.all()

    if profession:
        experts = experts.filter(profession__icontains=profession)

    if location:
        experts = experts.filter(location__icontains=location)

    if visa_status:
        experts = experts.filter(visa_status__icontains=visa_status)

    if skills:
        skills_list = skills.split(",")
        for skill in skills_list:
            experts = experts.filter(skills__icontains=skill)

    if experience:
        experts = experts.filter(experience__icontains=experience)

    expert_list = [
        {"name": e.name, "profession": e.profession, "location": e.location, "visa_status": e.visa_status, "skills": e.skills, "experience": e.experience}
        for e in experts
    ]
    return JsonResponse({"experts": expert_list})



def experts_page(request):
    return render(request, "accounts/experts.html")



def welcome_page(request):
    return render(request, 'accounts/welcome.html')  # Welcome Page ko show karega


def ai_hiring(request):
    return render(request, 'ai_hiring.html')

from django.shortcuts import render

def learn_more(request):
    return render(request, 'accounts/learn-more.html')

def get_started(request):
    return render(request, 'accounts/get-started.html')
from django.shortcuts import render

def services(request):
    return render(request, 'accounts/services.html') 
# utils.py (AI Matching Algorithm)
def match_jobs(applicant):
    matched_jobs = Job.objects.filter(
        skills_required__icontains=applicant.skills,
        location__icontains=applicant.preferred_location
    )
    return matched_jobs

# views.py
from django.shortcuts import render
from .models import Job, Applicant
from .utils import match_jobs

def recommended_jobs(request):
    applicant = Applicant.objects.get(user=request.user)
    jobs = match_jobs(applicant)
    return render(request, 'accounts/recommended_jobs.html', {'jobs': jobs})

import spacy

nlp = spacy.load("en_core_web_sm")

def analyze_resume(resume_text):
    doc = nlp(resume_text)
    skills = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    return skills

def resume_analysis(request):
    if request.method == "POST":
        resume_text = request.POST.get("resume_text")
        extracted_skills = analyze_resume(resume_text)
        return render(request, 'accounts/resume_analysis.html', {'skills': extracted_skills})
    return render(request, 'accounts/upload_resume.html')

import openai

openai.api_key = "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"

# accounts/views.py
from django.http import JsonResponse
from django.shortcuts import render
import openai

from django.shortcuts import render

import openai
import json
from django.views.decorators.csrf import csrf_exempt


def chatbot_page(request):
    # Your view logic here
    return render(request, 'chatbot.html')  # Example response

# Handle chatbot response
@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": user_message}
                ]
            )
            ai_reply = response["choices"][0]["message"]["content"]
            return JsonResponse({"reply": ai_reply})
        except Exception as e:
            return JsonResponse({"reply": f"Error: {str(e)}"}, status=500)
    return JsonResponse({"error": "Invalid request"}, status=400)




