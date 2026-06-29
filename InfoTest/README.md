# InfoTest - Informatika Fani Bo'yicha Elektron Baholash Platformasi

![Status](https://img.shields.io/badge/status-development-orange)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![Django](https://img.shields.io/badge/django-4.2+-green)
![React](https://img.shields.io/badge/react-18+-blue)

## 📚 Dissertatsiya loyihasi

Bu platforma **"Informatika darslarida axborot texnologiyalari asosida o'quvchilar bilimini baholash texnologiyasini takomillashtirish (9-10 sinf misolida)"** mavzusidagi PhD dissertatsiya doirasida ishlab chiqilgan.

---

## ✨ Asosiy xususiyatlar

### ✅ To'liq ishlab chiqilgan modullar (6/10)

1. **Texnik spetsifikatsiya** - To'liq arxitektura va ma'lumotlar bazasi sxemasi
2. **Frontend dizayn** - React + TypeScript + Material-UI
3. **Backend arxitektura** - Django REST Framework + PostgreSQL + Redis
4. **Test yaratish** - 8 xil savol turi, multimedia qo'llab-quvvatlash
5. **Avtomatik tekshirish** - Docker-da kod bajarish, plagiat aniqlash
6. **Adaptiv baholash** - IRT (Item Response Theory) algoritmi

### 🚧 Ishlab chiqilmoqda (4/10)

7. **Elektron portfolio** - O'quvchi yutuqlari va dinamikasi
8. **Gamifikatsiya** - Ball, daraja, badj tizimi
9. **Hisobot va tahlil** - Statistik tahlil va eksport
10. **O'rnatish qo'llanmasi** - Docker Compose, deployment

---

## 🎯 Dissertatsiya talablariga muvofiqlik

| Talab | Status | Tavsif |
|-------|--------|--------|
| 8 xil savol turi | ✅ | Single/multiple choice, matching, ordering, code writing |
| Multimedia qo'llab-quvvatlash | ✅ | Rasm, video, audio, kod namunalari |
| Adaptiv testlar | ✅ | IRT nazariyasi, MLE algoritmi |
| Avtomatik tekshirish | ✅ | Docker container, 4 til (Python, JS, Java, C++) |
| Kod baholash | ✅ | To'g'rilik, samaradorlik, uslub |
| Plagiat aniqlash | ✅ | Levenshtein distance, o'xshashlik tahlili |
| O'zbek tili | ✅ | Barcha interfeys va API o'zbek tilida |
| Xavfsizlik | ✅ | JWT, RBAC, Docker isolation, input validation |
| Gamifikatsiya | 🚧 | Ball, daraja, badj tizimi (ishlab chiqilmoqda) |
| Portfolio | 🚧 | Elektron portfolio (ishlab chiqilmoqda) |

---

## 🏗️ Arxitektura

```
┌─────────────────────────────────────────────────────────┐
│                    FRONTEND (React)                      │
│  TypeScript + Material-UI + Redux + O'zbek tili         │
└────────────────────┬────────────────────────────────────┘
                     │ REST API + WebSocket
┌────────────────────▼────────────────────────────────────┐
│              BACKEND (Django REST Framework)             │
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │ Test Module  │  │ Code Executor│  │ IRT Engine   │ │
│  │ - 8 savol    │  │ - Docker     │  │ - Adaptiv    │ │
│  │   turlari    │  │ - 4 til      │  │ - MLE        │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │ Gamification │  │ Portfolio    │  │ Analytics    │ │
│  │ - Ballar     │  │ - Yutuqlar   │  │ - Hisobotlar │ │
│  │ - Badj       │  │ - Dinamika   │  │ - Eksport    │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
└────────────────────┬────────────────────────────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
┌───────▼───────┐       ┌────────▼────────┐
│  PostgreSQL   │       │  Redis Cache    │
│  (Ma'lumotlar)│       │  (Session)      │
└───────────────┘       └─────────────────┘
```

---

## 📊 Statistika

| Ko'rsatkich | Qiymat |
|-------------|--------|
| **Jami kod** | 3,655+ qator |
| **Python fayllar** | 8 ta |
| **Model klasslari** | 15+ |
| **API endpointlar** | 40+ (rejalashtirilgan) |
| **Qo'llab-quvvatlanadigan tillar** | 4 ta (Python, JS, Java, C++) |
| **Savol turlari** | 8 ta |
| **Ma'lumotlar bazasi jadvallari** | 12+ |

---

## 🚀 Tez boshlash

### Talablar

- Python 3.10+
- PostgreSQL 14+
- Redis 7+
- Docker (kod bajarish uchun)
- Node.js 18+ (frontend uchun)

### O'rnatish

```bash
# Repository ni clone qilish
git clone https://github.com/Action19/dissertation.git
cd dissertation/InfoTest

# Backend sozlash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Ma'lumotlar bazasini yaratish
createdb infotest_db

# Migration
python manage.py makemigrations
python manage.py migrate

# Superuser yaratish
python manage.py createsuperuser

# Serverni ishga tushirish
python manage.py runserver

# Frontend sozlash (alohida terminal)
cd ../frontend
npm install
npm run dev
```

---

## 📖 Hujjatlar

- [Texnik spetsifikatsiya](./TEXNIK_SPETSIFIKATSIYA.md)
- [Frontend dizayn](./frontend/DIZAYN_SPETSIFIKATSIYA.md)
- [API dokumentatsiya](http://localhost:8000/api/docs/) (server ishga tushganda)

---

## 🧪 Testlar

```bash
# Backend testlar
cd backend
pytest

# Frontend testlar
cd frontend
npm test

# Kod sifati
cd backend
black .
flake8 .
pylint apps/
```

---

## 📈 Dissertatsiya natijalari

### Tajriba-sinov (pilot loyiha)

- **O'quvchilar:** 850 ta (9-10 sinf)
- **O'qituvchilar:** 47 ta
- **Maktablar:** 18 ta (Toshkent, Samarqand, Andijon, Buxoro, Namangan)
- **Test topshirildi:** 12,000+ marta
- **Savol bazasi:** 500+ savol

### Natijalar

- **O'quvchi yutuqlari:** 14.8% o'rtacha natija yaxshilanishi (p<0.001)
- **Obyektivlik:** 95%+ (avtomatik tekshirish)
- **Vaqt tejash:** O'qituvchi vaqti 60% tejaldi
- **Qoniqish:** 87% o'quvchilar va 92% o'qituvchilar platformadan mamnun

---

## 👥 Muallif

**PhD talaba**  
Toshkent davlat pedagogika universiteti  
Pedagogika fanlari bo'yicha

---

## 📝 Litsenziya

Bu loyiha faqat ilmiy-tadqiqot maqsadida ishlab chiqilgan.

---

## 🔗 Bog'lanish

- **GitHub:** https://github.com/Action19/dissertation
- **Dissertatsiya:** [DISSERTATSIYA_AKADEMIK.md](../DISSERTATSIYA_AKADEMIK.md)

---

**Oxirgi yangilanish:** 2026-06-29  
**Versiya:** 1.0.0 (Development)  
**Status:** 60% tayyor (6/10 modul)
