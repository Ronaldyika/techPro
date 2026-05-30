# TechPro Engineering — Full-Stack Django Web Application

A production-ready corporate website for a professional engineering and technical services company, built with Django, Django REST Framework, and Bootstrap 5.

---

## 🚀 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 4.2, Django REST Framework |
| Auth | JWT (SimpleJWT) + Session Auth |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Frontend | Django Templates, Bootstrap 5, JavaScript |
| Animations | AOS (Animate On Scroll) |
| Static | WhiteNoise |
| Media | Pillow |

---

## 📁 Project Structure

```
techpro/
├── manage.py
├── requirements.txt
├── .env.example
├── techpro_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── core/          # Site settings, team, context processors
│   ├── services/      # Services + DRF API
│   ├── projects/      # Portfolio + DRF API
│   ├── reviews/       # Ratings system + DRF API
│   ├── contact/       # Inquiry form + DRF API
│   ├── blog/          # Blog posts + DRF API
│   └── dashboard/     # Custom admin dashboard
├── templates/
│   ├── base.html
│   ├── core/
│   ├── services/
│   ├── projects/
│   ├── reviews/
│   ├── contact/
│   ├── blog/
│   └── dashboard/
├── static/
│   └── css/main.css
└── media/             # User-uploaded files
```

---

## ⚙️ Setup Instructions

### 1. Clone & Enter Project
```bash
cd techpro
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
```bash
cp .env.example .env
# Edit .env with your settings
```

### 5. Database Setup
```bash
python manage.py makemigrations core services projects reviews contact blog dashboard
python manage.py migrate
```

### 6. Create Admin User
```bash
python manage.py createsuperuser
```

### 7. Load Demo Data (Optional)
Run the seed script from Django shell:
```bash
python manage.py shell < seed_data.py
```

### 8. Collect Static Files
```bash
python manage.py collectstatic
```

### 9. Run Development Server
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000

---

## 🔐 Default Credentials (Demo)

| Account | Username | Password |
|---|---|---|
| Admin Dashboard | admin | admin1234 |

**⚠️ Change immediately in production!**

---

## 🌐 URL Routes

| URL | Description |
|---|---|
| `/` | Home page |
| `/about/` | About page |
| `/services/` | Services listing |
| `/services/<slug>/` | Service detail |
| `/projects/` | Project portfolio |
| `/projects/<slug>/` | Project detail |
| `/reviews/` | Reviews & ratings |
| `/blog/` | Blog listing |
| `/blog/<slug>/` | Blog post detail |
| `/contact/` | Contact form |
| `/dashboard/` | Custom admin dashboard |
| `/dashboard/login/` | Dashboard login |
| `/admin/` | Django admin panel |
| `/api/services/` | Services API |
| `/api/projects/` | Projects API |
| `/api/reviews/` | Reviews API |
| `/api/contact/` | Contact/Inquiry API |
| `/api/blog/` | Blog API |
| `/api/token/` | JWT Token Obtain |
| `/api/token/refresh/` | JWT Token Refresh |

---

## 🗄️ Switching to PostgreSQL

In `.env`, set:
```
DB_NAME=techpro_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

Then in `settings.py`, uncomment the PostgreSQL DATABASES block and comment out the SQLite one.

---

## 📧 Email Configuration

Update `.env` with your SMTP settings:
```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

For production, change `EMAIL_BACKEND` in settings.py from `console` to `smtp`.

---

## 🏭 Production Checklist

- [ ] Set `DEBUG=False` in `.env`
- [ ] Set strong `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS` with your domain
- [ ] Switch to PostgreSQL
- [ ] Configure real SMTP email
- [ ] Set up SSL/HTTPS
- [ ] Configure proper media file hosting (S3 or similar)
- [ ] Change admin credentials
- [ ] Run `collectstatic` and serve with Nginx/Gunicorn

### Gunicorn Command
```bash
gunicorn techpro_project.wsgi:application --bind 0.0.0.0:8000 --workers 3
```

---

## 🛠️ Company Services Covered

1. ☀️ Solar light & panel installation
2. ⚡ Electrical house wiring
3. 🏭 Industrial electrical systems
4. 🔧 Electrical troubleshooting & maintenance
5. 🏗️ Iron bending for construction
6. 🔩 Rod tying services
7. 📹 CCTV / security camera installation
8. 📡 Wireless network installations
9. 🏠 Smart home & security solutions
10. 📋 General engineering consultation

---

## 📞 Support

WhatsApp: As configured in `.env`  
Email: As configured in `.env`
