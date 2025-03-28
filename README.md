Follow these steps to run your AI Hiring System project on your local machine and open it in the browser:


---

1. Move to GitHub Folder (if your project is in GitHub)

If your project is inside a GitHub folder, open the terminal (or Command Prompt) and navigate to your project directory:

cd path/to/your/github/folder

(Replace path/to/your/github/folder with the actual path where your AI Hiring System is located.)


---

2. Activate Virtual Environment (venv)

Your project has a virtual environment (venv). You need to activate it:

For Windows (CMD or PowerShell):

venv\Scripts\activate

For Mac/Linux:

source venv/bin/activate

After activation, you should see (venv) appear before your command prompt.


---

3. Move to AI Hiring System Folder

Now, navigate to your AI Hiring System project directory:

cd ai-hiring-system


---

4. Run Django Server on Port 8001

Since you are using Django, start the server on port 8001:

python manage.py runserver 8001


---

5. Open in Browser

Once the server starts successfully, open your browser and go to:

http://127.0.0.1:8001/

This will open your AI Hiring System in your browser.


---

Optional: Superuser Login (if needed)

If you need to log in as an admin, run:

python manage.py createsuperuser

Then enter your username, email, and password.

Now, you can log in at:

http://127.0.0.1:8001/admin


---

All Steps in One Flow

cd path/to/your/github/folder
venv\Scripts\activate   # For Windows
# OR
source venv/bin/activate   # For Mac/Linux

cd ai-hiring-system
python manage.py runserver 8001

Now, visit http://127.0.0.1:8001/ in your browser.

Let me know if you need further help!

AI Hiring System - Step-by-Step Development Process

1. Project Setup

Installed Python & Django as the core framework.

Created a new Django project and a separate Django app for user accounts, jobs, and AI functionalities.

Set up virtual environment (venv) and installed the required dependencies (pip install django).

Configured database settings (SQLite for development).



---

2. User Authentication (Signup, Login, Logout)

Created signup and login forms using Django’s built-in authentication system (UserCreationForm & AuthenticationForm).

Implemented session-based login/logout to keep users authenticated.

Added login_required decorator to protect certain pages.


✅ Files Updated:

views.py (Signup, Login, Logout)

accounts/signup.html, accounts/login.html, accounts/dashboard.html



---

3. Dashboard Design & Navigation

Designed a responsive dashboard where users see job recommendations.

Added navigation links (Home, About, Services, Logout).

Used HTML, CSS, and Bootstrap for an attractive UI.

Included background images, AI-related GIFs, and icons.


✅ Files Updated:

accounts/dashboard.html

static/css/style.css



---

4. Job Posting System (Recruiters Side)

Created a Job model with fields like title, description, skills, location, salary, etc.

Built a Post Job form where recruiters can post jobs.

Implemented a Job Listing Page that shows all available jobs.

Added a timestamp (posted_at = now()) when a job is created.


✅ Files Updated:

models.py (Job Model)

forms.py (Job Form)

views.py (Post Job, Job List)

accounts/post_job.html, accounts/job_list.html



---

5. AI Matching System (Job Seekers Side)

Developed a search system where users can search for jobs based on keywords.

Implemented AI-based job recommendations using similarity matching.

Used Django QuerySet filtering (Job.objects.filter(title__icontains=query)).


✅ Files Updated:

views.py (Job Search, Job Recommendations)

accounts/recommendations.html



---

6. Expert Finder Feature

Added a Find Expert feature where users can search for experts from Germany.

Created an Expert Model with fields like profession, skills, experience, visa status.

Built a search form to find experts based on profession, location, skills, etc.

Integrated dynamic filtering using Django QuerySets.


✅ Files Updated:

models.py (Expert Model)

views.py (Find Expert, Search Experts)

accounts/find_expert.html



---

7. AI Recruiter Chatbot Integration

Created a chatbot that suggests jobs to recruiters.

Allowed recruiters to ask the chatbot for hiring recommendations.

Integrated OpenAI API (or a local AI model) for chatbot responses.

Used AJAX & JavaScript for real-time chatbot interaction.


✅ Files Updated:

views.py (Chatbot Logic)

static/js/chatbot.js

accounts/chatbot.html



---

8. Improving UI & User Experience

Updated Welcome Page with a bold heading: "Get Hired by Top Companies in Germany in Minutes"

Added attractive buttons ("Learn More", "Get Started")

Placed an AI-related GIF in the background to make it look engaging.

Styled all forms and pages with CSS, Bootstrap, and animations.

Used responsive design to ensure it works on mobile & desktop.


✅ Files Updated:

accounts/welcome.html

static/css/style.css



---

9. Final Deployment

Tested the system locally using python manage.py runserver.

Fixed bugs & layout issues.

Deployed the project to a live server (e.g., Heroku, AWS, or DigitalOcean).

Configured a custom domain and SSL certificate for security.


✅ Files Updated:

settings.py (Allowed Hosts, Static Files)

.gitignore (Excluded venv, DB files)

Deployed on live server

Final Thoughts

Now, the AI Hiring System is fully functional with:
✔ User authentication
✔ Job posting & search
✔ AI-powered job recommendations
✔ Expert Finder
✔ Recruiter Chatbot
✔ Attractive UI & Dashboard
✔ Live Deployment

This is a professional-level project that can be expanded into a real-world HR solution. Let me know if you need any modifications or additional features!
