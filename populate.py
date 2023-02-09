import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

import django
django.setup()

from main.models import Project, Tech, Img

Img.objects.all().delete()
Project.objects.all().delete()
Tech.objects.all().delete()

# Populate the Project model
projects = [
    {'name': 'Artificial Img', 'date': 2022},
    {'name': 'Crypto Tracker', 'date': 2021},
    {'name': 'Elysium E-Commerce Site', 'date': 2022},
    {'name': 'Emulated Self Driving Car', 'date': 2022},
    {'name': 'Easy Shopping', 'date': 2021},
    {'name': 'Ticket Scraper', 'date': 2021},
]
for project in projects:
    p = Project(name=project['name'], date=project['date'])
    p.save()

# Populate the Tech model
techs = [
    'Python',
    'AI',
    "Twitter's API",
    'Deep Learning',
    'C#',
    '.NET',
    'Web Scraping',
    'Cordova',
    'JavaScript',
    'JQuery',
    'HTML & CSS',
    'PowerShell',
    'React',
    'Contentful',
    'Algolia API',
    'Computer Vision',
    'Machine Learning'
]
for tech in techs:
    t = Tech(name=tech)
    t.save()

# Assign techs to projects
project_techs = [
    ('Artificial Img', 'Python'),
    ('Artificial Img', "Twitter's API"),
    ('Artificial Img', 'AI'),
    ('Crypto Tracker', 'Python'),
    ('Crypto Tracker', "Twitter's API"),
    ('Crypto Tracker', 'PowerShell'),
    ('Elysium E-Commerce Site', 'React'),
    ('Elysium E-Commerce Site', 'Contentful'),
    ('Elysium E-Commerce Site', 'Algolia API'),
    ('Emulated Self Driving Car', 'Deep Learning'),
    ('Emulated Self Driving Car', 'Machine Learning'),
    ('Emulated Self Driving Car', 'Computer Vision'),
    ('Emulated Self Driving Car', 'AI'),
    ('Easy Shopping', 'Cordova'),
    ('Easy Shopping', 'HTML & CSS'),
    ('Easy Shopping', 'JQuery'),
    ('Easy Shopping', 'JavaScript'),
    ('Ticket Scraper', 'C#'),
    ('Ticket Scraper', '.NET'),
    ('Ticket Scraper', 'Web Scraping')
]
for project, tech_name in project_techs:
    project = Project.objects.get(name=project)
    tech = Tech.objects.get(name=tech_name)
    tech.project.add(project)

# List of image urls and alt texts
imgs = [
    {"project": "Artificial Img", "url": "Artificial_Img_1.png", "alt": "Artificial Intelligence Image 1"},
    {"project": "Artificial Img", "url": "Artificial_Img_2.png", "alt": "Artificial Intelligence Image 2"},
    {"project": "Artificial Img", "url": "Artificial_Img_3.png", "alt": "Artificial Intelligence Image 3"},
    {"project": 'Crypto Tracker', "url": "Crypto_Tracker_1.png", "alt": "Crypto Tracker Image 1"},
    {"project": 'Crypto Tracker', "url": "Crypto_Tracker_2.png", "alt": "Crypto Tracker Image 2"},
    {"project": 'Crypto Tracker', "url": "Crypto_Tracker_3.png", "alt": "Crypto Tracker Image 3"},
    {"project": 'Elysium E-Commerce Site', "url": "Project40_1.png", "alt": "Project 40 Image 1"},
    {"project": 'Elysium E-Commerce Site', "url": "Project40_2.png", "alt": "Project 40 Image 2"},
    {"project": 'Elysium E-Commerce Site', "url": "Project40_3.png", "alt": "Project 40 Image 3"},
    {"project": 'Emulated Self Driving Car', "url": "AI_Car_1.png", "alt": "AI Car Image 1"},
    {"project": 'Emulated Self Driving Car', "url": "AI_Car_2.png", "alt": "AI Car Image 2"},
    {"project": 'Emulated Self Driving Car', "url": "AI_Car_3.png", "alt": "AI Car Image 3"},
    {"project": 'Easy Shopping', "url": "Easy_Shopping_1.png", "alt": "Easy Shopping Image 1"},
    {"project": 'Easy Shopping', "url": "Easy_Shopping_2.png", "alt": "Easy Shopping Image 2"},
    {"project": 'Easy Shopping', "url": "Easy_Shopping_3.png", "alt": "Easy Shopping Image 3"},
    {"project": "Ticket Scraper", "url": "Scraper_1.png", "alt": "Scraper Image 1"},
    {"project": "Ticket Scraper", "url": "Scraper_2.png", "alt": "Scraper Image 2"},
    {"project": "Ticket Scraper", "url": "Scraper_3.png", "alt": "Scraper Image 3"},
]

for img in imgs:
    project = img["project"]
    url = img["url"]
    alt = img["alt"]
    
    project = Project.objects.get(name=project)
    img = Img(url=url, alt=alt, project=project)
    img.save()