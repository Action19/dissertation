# InfoTest - Informatika Fani Bo'yicha Elektron Baholash Platformasi

## TEXNIK SPETSIFIKATSIYA v1.0

**Ishlab chiquvchi:** PhD dissertatsiya loyihasi  
**Maqsad:** 9-10 sinf o'quvchilarining informatika bo'yicha bilimini AKT asosida baholash  
**Til:** O'zbek tili (Lotin alifbosi)  
**Sana:** 2026-06-29

---

## 1. UMUMIY MA'LUMOTLAR

### 1.1. Platformaning maqsadi

InfoTest platformasi - bu informatika fanidan o'quvchilar bilimini zamonaviy axborot texnologiyalari asosida baholash uchun maxsus ishlab chiqilgan elektron tizim. Platforma quyidagi asosiy vazifalarni hal qiladi:

- O'quvchilar bilimini obyektiv va tezkor baholash
- Nazariy bilim va amaliy ko'nikmalarni kompleks baholash
- Dasturlash qobiliyatini avtomatik tekshirish
- Doimiy monitoring va formativ baholash
- Individual ta'lim traektoriyasini yaratish
- O'qituvchilar mehnatini yengillashtirish

### 1.2. Asosiy foydalanuvchilar

| Rol | Tavsif | Soni (pilot loyiha) |
|-----|--------|---------------------|
| **O'qituvchi** | Test yaratadi, natijalarni tahlil qiladi | 47 ta |
| **O'quvchi** | Test topshiradi, natijani ko'radi | 850 ta |
| **Administrator** | Tizimni boshqaradi, hisobotlar oladi | 5 ta |
| **Ota-ona** | Farzandning natijalarini kuzatadi | 850+ |

### 1.3. Funktsional talablar (dissertatsiya asosida)

#### A. Test yaratish va boshqarish
- [x] 8 xil savol turi
- [x] Multimedia qo'llab-quvvatlash (rasm, video, audio)
- [x] Kod yozish savollari
- [x] Savol bazasi (500+ savol)
- [x] Savol tasodifiyligi
- [x] Vaqt cheklovi

#### B. Baholash mexanizmlari
- [x] Avtomatik tekshirish
- [x] Adaptiv test (IRT nazariyasi)
- [x] Kod tekshirish va baholash
- [x] Plagiat aniqlash
- [x] Darhol natija chiqarish

#### C. Monitoring va tahlil
- [x] Elektron portfolio
- [x] Statistik tahlil
- [x] Grafik va diagrammalar
- [x] Individual va guruh tahlili
- [x] Eksport funksiyasi (Excel, PDF)

#### D. Motivatsiya va gamifikatsiya
- [x] Ball tizimi
- [x] Darajalar (Boshlang'ich, O'rta, Yuqori, Expert)
- [x] Badj va mukofotlar
- [x] Liderlik jadvali
- [x] Quest topshiriqlar

#### E. Qayta aloqa va qo'llab-quvvatlash
- [x] Tezkor qayta aloqa
- [x] Tavsiyalar va yo'naltirishlar
- [x] Qo'shimcha materiallar
- [x] Interaktiv yordam

---

## 2. TEXNOLOGIK ARXITEKTURA

### 2.1. Umumiy arxitektura

```
┌─────────────────────────────────────────────────────────┐
│                    FRONTEND                             │
│  React.js + Redux + Material-UI + O'zbek tili          │
└────────────────┬────────────────────────────────────────┘
                 │ HTTPS / WebSocket
┌────────────────▼────────────────────────────────────────┐
│                    BACKEND API                          │
│         Python Django REST Framework                     │
│  - Authentication (JWT)                                 │
│  - Test Management                                      │
│  - Code Execution Engine                                │
│  - Adaptive Algorithm (IRT)                             │
│  - Analytics Engine                                     │
└────────────────┬────────────────────────────────────────┘
                 │
        ┌────────┴────────┐
        │                 │
┌───────▼──────┐  ┌──────▼──────────┐
│  PostgreSQL  │  │   Redis Cache   │
│  (Ma'lumotlar│  │   (Session)     │
│   bazasi)    │  │                 │
└──────────────┘  └─────────────────┘
        │
┌───────▼──────────────────────────────┐
│     File Storage (Media Files)       │
│  - AWS S3 / Mahalliy server          │
│  - Rasm, video, audio fayllar        │
└──────────────────────────────────────┘
```

### 2.2. Texnologik stack

#### Frontend
- **Framework:** React.js 18+ (TypeScript)
- **State Management:** Redux Toolkit
- **UI Library:** Material-UI (MUI) 5+
- **Charting:** Chart.js / Recharts
- **Code Editor:** Monaco Editor (VS Code asosida)
- **Markdown:** React Markdown
- **HTTP Client:** Axios

#### Backend
- **Language:** Python 3.10+
- **Framework:** Django 4.2+ / Django REST Framework
- **Authentication:** JWT (Simple JWT)
- **Code Execution:** Docker containers (secure sandboxing)
- **Async Tasks:** Celery + Redis
- **WebSocket:** Django Channels
- **Testing:** pytest

#### Ma'lumotlar bazasi
- **Primary DB:** PostgreSQL 14+
- **Cache:** Redis 7+
- **Search:** PostgreSQL Full-Text Search

#### DevOps
- **Containerization:** Docker + Docker Compose
- **Web Server:** Nginx
- **WSGI:** Gunicorn
- **Monitoring:** Prometheus + Grafana (optional)
- **Logs:** ELK Stack (optional)

### 2.3. Tizim talablari

#### Server (Minimum)
- **CPU:** 4 cores (2.5 GHz+)
- **RAM:** 8 GB
- **Storage:** 100 GB SSD
- **Network:** 100 Mbps
- **OS:** Ubuntu 20.04 LTS / CentOS 8

#### Server (Tavsiya etiladi)
- **CPU:** 8 cores (3.0 GHz+)
- **RAM:** 16 GB
- **Storage:** 250 GB SSD
- **Network:** 1 Gbps
- **OS:** Ubuntu 22.04 LTS

#### Client (Brauzer)
- Chrome 90+ / Firefox 88+ / Safari 14+ / Edge 90+
- JavaScript enabled
- Minimum ekran: 1024x768
- Internet tezligi: 2 Mbps+

---

## 3. MA'LUMOTLAR BAZASI SXEMASI

### 3.1. Asosiy jadvallar

#### Users (Foydalanuvchilar)
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    first_name VARCHAR(150),
    last_name VARCHAR(150),
    role VARCHAR(20) NOT NULL, -- 'student', 'teacher', 'admin', 'parent'
    school_id INTEGER REFERENCES schools(id),
    grade INTEGER, -- 9, 10
    avatar_url TEXT,
    language VARCHAR(10) DEFAULT 'uz',
    is_active BOOLEAN DEFAULT true,
    date_joined TIMESTAMP DEFAULT NOW(),
    last_login TIMESTAMP
);
```

#### Schools (Maktablar)
```sql
CREATE TABLE schools (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    region VARCHAR(100),
    district VARCHAR(100),
    address TEXT,
    phone VARCHAR(20),
    email VARCHAR(254),
    director_name VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### Questions (Savol bazasi)
```sql
CREATE TABLE questions (
    id UUID PRIMARY KEY,
    author_id UUID REFERENCES users(id),
    question_type VARCHAR(50) NOT NULL, 
    -- 'single_choice', 'multiple_choice', 'true_false', 
    -- 'matching', 'ordering', 'fill_blank', 'short_answer', 'code_writing'
    topic VARCHAR(100) NOT NULL,
    subtopic VARCHAR(100),
    difficulty INTEGER CHECK (difficulty >= 1 AND difficulty <= 5),
    bloom_level VARCHAR(50), -- 'knowledge', 'comprehension', 'application', etc.
    
    question_text TEXT NOT NULL,
    question_media_url TEXT, -- rasm, video, audio
    code_snippet TEXT, -- agar dasturlash savoli bo'lsa
    
    options JSONB, -- javob variantlari
    correct_answer JSONB NOT NULL,
    explanation TEXT, -- tushuntirish
    hints TEXT, -- maslahat
    
    tags TEXT[], -- ['algoritmlar', 'tsikl', 'python']
    estimated_time INTEGER, -- kutilgan vaqt (soniyalarda)
    
    usage_count INTEGER DEFAULT 0,
    success_rate FLOAT, -- to'g'ri javob foizi
    irt_difficulty FLOAT, -- IRT parametri
    irt_discrimination FLOAT, -- IRT parametri
    
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

#### Tests (Testlar)
```sql
CREATE TABLE tests (
    id UUID PRIMARY KEY,
    teacher_id UUID REFERENCES users(id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    subject VARCHAR(100) DEFAULT 'Informatika',
    grade INTEGER CHECK (grade IN (9, 10)),
    
    test_type VARCHAR(50), -- 'diagnostic', 'formative', 'summative', 'practice'
    is_adaptive BOOLEAN DEFAULT false,
    
    total_questions INTEGER,
    time_limit INTEGER, -- daqiqalarda
    passing_score INTEGER, -- minimal ball
    
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    
    shuffle_questions BOOLEAN DEFAULT true,
    shuffle_options BOOLEAN DEFAULT true,
    show_results_immediately BOOLEAN DEFAULT true,
    allow_retake BOOLEAN DEFAULT false,
    max_attempts INTEGER DEFAULT 1,
    
    status VARCHAR(20) DEFAULT 'draft', -- 'draft', 'published', 'archived'
    
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

#### Test_Questions (Test-Savol bog'lanishi)
```sql
CREATE TABLE test_questions (
    id UUID PRIMARY KEY,
    test_id UUID REFERENCES tests(id) ON DELETE CASCADE,
    question_id UUID REFERENCES questions(id),
    order_number INTEGER,
    points INTEGER DEFAULT 1,
    
    UNIQUE(test_id, question_id)
);
```

#### Test_Attempts (Urinishlar)
```sql
CREATE TABLE test_attempts (
    id UUID PRIMARY KEY,
    test_id UUID REFERENCES tests(id),
    student_id UUID REFERENCES users(id),
    
    attempt_number INTEGER,
    start_time TIMESTAMP DEFAULT NOW(),
    end_time TIMESTAMP,
    time_taken INTEGER, -- soniyalarda
    
    total_questions INTEGER,
    answered_questions INTEGER,
    correct_answers INTEGER,
    
    score INTEGER, -- olingan ball
    percentage FLOAT,
    grade VARCHAR(10), -- 'A', 'B', 'C', 'D', 'F'
    passed BOOLEAN,
    
    adaptive_theta FLOAT, -- adaptiv test uchun bilim darajasi
    
    ip_address INET,
    user_agent TEXT,
    
    status VARCHAR(20) DEFAULT 'in_progress', -- 'in_progress', 'completed', 'abandoned'
    
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### Answers (Javoblar)
```sql
CREATE TABLE answers (
    id UUID PRIMARY KEY,
    attempt_id UUID REFERENCES test_attempts(id) ON DELETE CASCADE,
    question_id UUID REFERENCES questions(id),
    
    student_answer JSONB,
    is_correct BOOLEAN,
    points_earned INTEGER,
    time_spent INTEGER, -- soniyalarda
    
    code_submission TEXT, -- agar kod yozish savoli bo'lsa
    code_output TEXT,
    code_errors TEXT,
    plagiarism_score FLOAT, -- 0.0 - 1.0
    
    feedback TEXT, -- avtomatik qayta aloqa
    
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### Portfolio (Elektron portfolio)
```sql
CREATE TABLE portfolio (
    id UUID PRIMARY KEY,
    student_id UUID REFERENCES users(id),
    
    item_type VARCHAR(50), -- 'test_result', 'project', 'assignment', 'achievement'
    title VARCHAR(255),
    description TEXT,
    
    test_attempt_id UUID REFERENCES test_attempts(id),
    file_url TEXT,
    
    score INTEGER,
    grade VARCHAR(10),
    teacher_comment TEXT,
    
    is_showcased BOOLEAN DEFAULT false, -- o'quvchi ko'rsatmoqchi bo'lgan ishlar
    
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### Achievements (Yutuqlar - Gamifikatsiya)
```sql
CREATE TABLE achievements (
    id UUID PRIMARY KEY,
    student_id UUID REFERENCES users(id),
    
    achievement_type VARCHAR(50), -- 'badge', 'level', 'quest'
    name VARCHAR(100),
    description TEXT,
    icon_url TEXT,
    
    points_earned INTEGER,
    level INTEGER, -- 1=Boshlang'ich, 2=O'rta, 3=Yuqori, 4=Expert
    
    earned_at TIMESTAMP DEFAULT NOW()
);
```

#### Analytics (Tahlil ma'lumotlari)
```sql
CREATE TABLE analytics (
    id UUID PRIMARY KEY,
    
    entity_type VARCHAR(50), -- 'student', 'class', 'school', 'question', 'test'
    entity_id UUID,
    
    metric_name VARCHAR(100),
    metric_value JSONB,
    
    period VARCHAR(20), -- 'daily', 'weekly', 'monthly', 'yearly'
    date DATE,
    
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 4. API ENDPOINTLAR

### 4.1. Authentication

```
POST   /api/auth/register/          - Ro'yxatdan o'tish
POST   /api/auth/login/             - Kirish
POST   /api/auth/logout/            - Chiqish
POST   /api/auth/refresh-token/     - Token yangilash
POST   /api/auth/password-reset/    - Parolni tiklash
GET    /api/auth/profile/           - Profil ma'lumotlari
PUT    /api/auth/profile/           - Profilni yangilash
```

### 4.2. Tests (Testlar)

```
GET    /api/tests/                  - Barcha testlar ro'yxati
POST   /api/tests/                  - Yangi test yaratish
GET    /api/tests/{id}/             - Test tafsilotlari
PUT    /api/tests/{id}/             - Testni tahrirlash
DELETE /api/tests/{id}/             - Testni o'chirish
POST   /api/tests/{id}/publish/     - Testni nashr qilish
POST   /api/tests/{id}/start/       - Testni boshlash
POST   /api/tests/{id}/submit/      - Testni topshirish
GET    /api/tests/{id}/results/     - Test natijalari
```

### 4.3. Questions (Savollar)

```
GET    /api/questions/              - Savol bazasi
POST   /api/questions/              - Yangi savol yaratish
GET    /api/questions/{id}/         - Savol tafsilotlari
PUT    /api/questions/{id}/         - Savolni tahrirlash
DELETE /api/questions/{id}/         - Savolni o'chirish
GET    /api/questions/topics/       - Mavzular ro'yxati
GET    /api/questions/search/       - Savol qidirish
POST   /api/questions/import/       - Savollarni import qilish
GET    /api/questions/export/       - Savollarni export qilish
```

### 4.4. Attempts (Urinishlar)

```
GET    /api/attempts/               - Urinishlar tarixi
GET    /api/attempts/{id}/          - Urinish tafsilotlari
POST   /api/attempts/{id}/answer/   - Javob yuborish
GET    /api/attempts/{id}/feedback/ - Qayta aloqa olish
```

### 4.5. Portfolio

```
GET    /api/portfolio/              - Portfolio ro'yxati
POST   /api/portfolio/              - Element qo'shish
GET    /api/portfolio/{id}/         - Element tafsilotlari
PUT    /api/portfolio/{id}/         - Elementni yangilash
DELETE /api/portfolio/{id}/         - Elementni o'chirish
GET    /api/portfolio/showcase/     - Namoyish uchun portfolio
```

### 4.6. Analytics (Tahlil)

```
GET    /api/analytics/student/{id}/     - O'quvchi statistikasi
GET    /api/analytics/class/{id}/       - Sinf statistikasi
GET    /api/analytics/school/{id}/      - Maktab statistikasi
GET    /api/analytics/question/{id}/    - Savol statistikasi
GET    /api/analytics/test/{id}/        - Test statistikasi
GET    /api/analytics/reports/          - Hisobotlar
POST   /api/analytics/export/           - Ma'lumotlarni eksport
```

### 4.7. Gamification

```
GET    /api/achievements/           - Yutuqlar ro'yxati
GET    /api/achievements/badges/    - Badj ro'yxati
GET    /api/achievements/levels/    - Darajalar
GET    /api/leaderboard/            - Liderlik jadvali
POST   /api/achievements/earn/      - Yutuq olish
```

---

## 5. XAVFSIZLIK VA HIMOYA

### 5.1. Authentication & Authorization
- JWT (JSON Web Token) asosida autentifikatsiya
- Role-based access control (RBAC)
- Token muddati: 1 soat (refresh token: 7 kun)
- 2FA (Two-Factor Authentication) - optional

### 5.2. Ma'lumotlar xavfsizligi
- HTTPS (TLS 1.3)
- Parollar bcrypt bilan shifrlangan
- SQL Injection himoyasi (Django ORM)
- XSS va CSRF himoyasi
- Rate limiting (DDoS himoyasi)
- Input validation va sanitization

### 5.3. Kod ijrosi xavfsizligi
- Docker container izolyatsiyasi
- Cheklangan resurslar (CPU, RAM, vaqt)
- Network access yo'q
- File system read-only
- Xavfli amallar taqiqlankan (exec, eval, import)

### 5.4. Ma'lumotlar maxfiyligi
- GDPR va O'zbekiston qonunchiligigaiga muvofiq
- Shaxsiy ma'lumotlar shifrlangan
- Ma'lumotlar zaxirasi har kuni
- Audit log (kim, qachon, nima qilgan)

---

## 6. ISHLASH PARAMETRLARI (SLA)

### 6.1. Performance
- Response time: < 200ms (avg)
- Page load time: < 2 sekund
- API latency: < 100ms
- Concurrent users: 1000+
- Tests per second: 50+

### 6.2. Availability
- Uptime: 99.5% (yiliga ~43 soat downtime)
- Backup: har kuni
- Disaster recovery: < 4 soat

### 6.3. Scalability
- Horizontal scaling (cloud)
- Load balancing
- Caching strategiyasi
- CDN for media files

---

**SPETSIFIKATSIYA TAMOMLANDI**

Keyingi bosqichlar:
- [x] Texnik spetsifikatsiya ✅
- [ ] Frontend dizayn
- [ ] Backend arxitektura
- [ ] Database migration
- [ ] API development
- [ ] Frontend development
- [ ] Testing
- [ ] Deployment

