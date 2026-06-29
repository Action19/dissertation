# InfoTest Frontend - Dizayn Spetsifikatsiyasi

## 1. DIZAYN TAMOYILLARI

### 1.1. Asosiy tamoyillar (Dissertatsiyaga muvofiq)

- ✅ **O'zbek tili:** Barcha interfeys o'zbek tilida (lotin alifbosi)
- ✅ **Soddalik:** Tushunarli, intuitiv navigatsiya
- ✅ **Zamonaviylik:** Modern, yoqimli dizayn
- ✅ **Motivatsion:** Ranglar, animatsiyalar, gamifikatsiya
- ✅ **Responsiv:** Desktop, planshet, telefon uchun moslashgan
- ✅ **Accessibility:** Barcha foydalanuvchilar uchun qulay

### 1.2. Ranglar palitasi

```css
/* Asosiy ranglar */
--primary: #1976d2;        /* Moviy - asosiy rang */
--primary-dark: #1565c0;   
--primary-light: #42a5f5;  

--secondary: #9c27b0;      /* Binafsha - ikkilamchi rang */
--secondary-dark: #7b1fa2; 
--secondary-light: #ba68c8;

--success: #2e7d32;        /* Yashil - muvaffaqiyat */
--warning: #ed6c02;        /* Sariq - ogohlantirish */
--error: #d32f2f;          /* Qizil - xato */
--info: #0288d1;           /* Ko'k - ma'lumot */

/* Neytral ranglar */
--text-primary: #212121;
--text-secondary: #757575;
--background: #fafafa;
--surface: #ffffff;
--divider: #e0e0e0;

/* Gamifikatsiya ranglari */
--gold: #ffd700;           /* Oltin - yuqori daraja */
--silver: #c0c0c0;         /* Kumush - yaxshi daraja */
--bronze: #cd7f32;         /* Bronza - qoniqarli */
```

### 1.3. Typography (Shriftlar)

```css
/* Asosiy shrift */
font-family: 'Roboto', 'Inter', -apple-system, BlinkMacSystemFont, 
             'Segoe UI', sans-serif;

/* O'lchamlar */
--text-xs: 0.75rem;   /* 12px */
--text-sm: 0.875rem;  /* 14px */
--text-base: 1rem;    /* 16px */
--text-lg: 1.125rem;  /* 18px */
--text-xl: 1.25rem;   /* 20px */
--text-2xl: 1.5rem;   /* 24px */
--text-3xl: 1.875rem; /* 30px */
--text-4xl: 2.25rem;  /* 36px */

/* Vaznlar */
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;
```

### 1.4. Spacing (Bo'shliqlar)

```css
--space-1: 0.25rem;  /* 4px */
--space-2: 0.5rem;   /* 8px */
--space-3: 0.75rem;  /* 12px */
--space-4: 1rem;     /* 16px */
--space-5: 1.25rem;  /* 20px */
--space-6: 1.5rem;   /* 24px */
--space-8: 2rem;     /* 32px */
--space-10: 2.5rem;  /* 40px */
--space-12: 3rem;    /* 48px */
```

---

## 2. SAHIFALAR VA KOMPONENTLAR

### 2.1. Bosh sahifa (Landing Page)

#### Layout:
```
┌──────────────────────────────────────────────────────┐
│  Header: Logo | Haqida | Imkoniyatlar | Kirish      │
├──────────────────────────────────────────────────────┤
│                                                       │
│         Hero Section                                 │
│    "InfoTest - Bilimni baholashning                 │
│     zamonaviy yo'li"                                │
│         [Boshlash] [Video ko'rish]                  │
│                                                       │
├──────────────────────────────────────────────────────┤
│   Imkoniyatlar (4 ta karta)                         │
│   📝 Test yaratish  ⚡ Tez natija                   │
│   📊 Tahlil         🎮 Gamifikatsiya                │
├──────────────────────────────────────────────────────┤
│   Statistika                                         │
│   850+ o'quvchi | 47 o'qituvchi | 500+ savol       │
├──────────────────────────────────────────────────────┤
│   Footer: Kontaktlar | Yordam | © 2024-2026        │
└──────────────────────────────────────────────────────┘
```

### 2.2. Kirish sahifasi (Login)

```
┌────────────────────────────────┐
│                                │
│    🎓 InfoTest                 │
│    Kirish                      │
│                                │
│    [Username yoki Email]       │
│    [Parol] 👁                  │
│    ☐ Eslab qolish              │
│                                │
│    [Kirish]                    │
│                                │
│    Parolni unutdingizmi?       │
│    Ro'yxatdan o'tish           │
│                                │
└────────────────────────────────┘
```

### 2.3. Dashboard (Asosiy panel)

#### O'quvchi Dashboard:
```
┌─────────────────────────────────────────────────────────┐
│ 🎓 InfoTest     Testlar | Portfolio | Profil    [🔔] 👤│
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Salom, Abdulloh! 👋                                    │
│  Sizning reytingingiz: 🏆 245-o'rin (850 dan)          │
│                                                          │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐          │
│  │ Darajangiz│  │ Ballaringiz│  │ Badj soni │          │
│  │  ⭐ O'rta │  │  1,234     │  │    12     │          │
│  └───────────┘  └───────────┘  └───────────┘          │
│                                                          │
│  📝 Faol testlar (3 ta)                                │
│  ┌────────────────────────────────────────────┐        │
│  │ Algoritmlar asoslari                       │        │
│  │ ⏱ 2 kun qoldi | 25 savol | 60 daqiqa      │        │
│  │ [Boshlash]                           85%   │        │
│  └────────────────────────────────────────────┘        │
│                                                          │
│  📊 So'ngi natijalar                                    │
│  • Python dasturlash - 87% ✅                          │
│  • Ma'lumotlar bazasi - 72% ⚠️                         │
│                                                          │
│  🎯 Tavsiyalar                                          │
│  • SQL so'rovlarini takrorlang                         │
│  • Tsikl mavzusini mustahkamlang                       │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

#### O'qituvchi Dashboard:
```
┌─────────────────────────────────────────────────────────┐
│ 🎓 InfoTest  Testlar | Savollar | Statistika  [🔔] 👤  │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Salom, Nodira Akramovna! 👋                            │
│  9-A va 10-B sinflar                                    │
│                                                          │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐          │
│  │ O'quvchilar│  │ Testlar  │  │ O'rtacha  │          │
│  │     42    │  │    18    │  │   78%     │          │
│  └───────────┘  └───────────┘  └───────────┘          │
│                                                          │
│  ⚡ Tezkor harakatlar                                   │
│  [➕ Yangi test] [📝 Savol qo'shish] [📊 Hisobot]     │
│                                                          │
│  📋 Faol testlar (5 ta)                                │
│  • Algoritmlar - 28/42 o'quvchi topshirdi             │
│  • Python asoslari - 15/42 topshirdi                   │
│                                                          │
│  📊 Oxirgi natijalar grafigi                           │
│  [Bar chart: sinf bo'yicha o'rtacha natijalar]        │
│                                                          │
│  ⚠️ E'tiborga olish kerak                              │
│  • 5 ta o'quvchi past natija - yordam zarur           │
│  • 2 ta test muddati tugayapti                         │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### 2.4. Test topshirish sahifasi

```
┌─────────────────────────────────────────────────────────┐
│ ◀ Chiqish    Algoritmlar testi        ⏱ 45:23   [💾]  │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Progress: ▓▓▓▓▓▓▓▓░░░░░░░░  12/25 savol              │
│                                                          │
│  Savol 12:                                    [🔖 Flag] │
│                                                          │
│  Quyidagi kod qanday natija beradi?                    │
│                                                          │
│  ┌──────────────────────────────────┐                  │
│  │ for i in range(5):               │                  │
│  │     print(i * 2)                 │                  │
│  └──────────────────────────────────┘                  │
│                                                          │
│  Javobni tanlang:                                       │
│  ⃝ A) 0, 2, 4, 6, 8                                    │
│  ⃝ B) 1, 2, 3, 4, 5                                    │
│  ⃝ C) 2, 4, 6, 8, 10                                   │
│  ⃝ D) 0, 1, 2, 3, 4                                    │
│                                                          │
│  💡 Maslahat kerakmi?                                   │
│                                                          │
│  [◀ Avvalgi]              [Keyingi ▶]                  │
│                                                          │
│  Savollar paneli:                                       │
│  [1✓][2✓][3✓][4✓][5✓][6✓][7✓][8✓][9✓][10✓][11✓][12] │
│  [13][14][15][16][17][18][19][20][21][22][23][24][25] │
│                                                          │
│                         [Topshirish]                     │
└─────────────────────────────────────────────────────────┘
```

### 2.5. Natijalar sahifasi

```
┌─────────────────────────────────────────────────────────┐
│                   🎉 Ajoyib natija!                     │
│                                                          │
│              Sizning natijangiz: 87%                    │
│                  22/25 to'g'ri                          │
│                                                          │
│  ┌─────────────────────────────────────────┐           │
│  │       [Progress ring: 87%]              │           │
│  │                                          │           │
│  │    ⭐⭐⭐⭐⭐                              │           │
│  │    A'lo baho!                           │           │
│  └─────────────────────────────────────────┘           │
│                                                          │
│  📊 Batafsil tahlil:                                    │
│  ┌──────────────────────────────────────┐              │
│  │ Nazariy bilim      ████████░  90%    │              │
│  │ Amaliy ko'nikma    ███████░░  85%    │              │
│  │ Algoritmik fikr    ███████░░  83%    │              │
│  └──────────────────────────────────────┘              │
│                                                          │
│  ✅ Kuchli tomonlar:                                    │
│  • Tsikllar mavzusi - mukammal!                        │
│  • Ma'lumot tuzilmalari - a'lo                         │
│                                                          │
│  ⚠️ Yaxshilash kerak:                                   │
│  • Rekursiya mavzusini takrorlang                      │
│  • Qidiruv algoritmlari - 2 ta xato                    │
│                                                          │
│  📚 Tavsiya etilgan materiallar:                        │
│  • Video: Rekursiya tushunarli tushuntirish            │
│  • Mashq: Qidiruv algoritmlari amaliyoti              │
│                                                          │
│  🏆 +50 ball | 🎖 "Algoritmlar ustasi" badji olindi!  │
│                                                          │
│  [Batafsil ko'rish] [Portfolio ga qo'shish] [Qayta]   │
└─────────────────────────────────────────────────────────┘
```

### 2.6. Portfolio sahifasi

```
┌─────────────────────────────────────────────────────────┐
│  📁 Mening Portfolio'm                                   │
│  [Barcha] [Testlar] [Loyihalar] [Yutuqlar]             │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  📈 Umumiy statistika                                   │
│  [Line chart: vaqt bo'yicha rivojlanish]               │
│                                                          │
│  🏆 Yutuqlar (12 ta)                                    │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐                          │
│  │ 🥇 │ │ 🎯 │ │ 🔥 │ │ ⭐ │                          │
│  │1-o │ │Top │ │Seri│ │Usta│                          │
│  │rin │ │ 10 │ │ya  │ │d   │                          │
│  └────┘ └────┘ └────┘ └────┘                          │
│                                                          │
│  📝 So'ngi testlar (10 ta)                             │
│  ┌────────────────────────────────────────┐            │
│  │ Algoritmlar testi          87% ⭐⭐⭐⭐⭐│            │
│  │ 2024-06-25 | 25 savol | 45 daqiqa     │            │
│  │ [Batafsil ko'rish]                     │            │
│  └────────────────────────────────────────┘            │
│                                                          │
│  💼 Loyihalar (5 ta)                                    │
│  • Kalkulyator dasturi - Python           │            │
│  • Savol-javob o'yini - Scratch          │            │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## 3. KOMPONENTLAR KUTUBXONASI

### 3.1. Button (Tugma)

```tsx
// Variantlar
<Button variant="contained">Primary</Button>
<Button variant="outlined">Secondary</Button>
<Button variant="text">Text</Button>

// Ranglar
<Button color="primary">Asosiy</Button>
<Button color="success">Muvaffaqiyat</Button>
<Button color="error">Xato</Button>

// O'lchamlar
<Button size="small">Kichik</Button>
<Button size="medium">O'rtacha</Button>
<Button size="large">Katta</Button>
```

### 3.2. Card (Karta)

```tsx
<Card elevation={2}>
  <CardHeader 
    title="Test nomi"
    subheader="25 savol | 60 daqiqa"
    avatar={<Avatar>A</Avatar>}
  />
  <CardContent>
    Kontent matni
  </CardContent>
  <CardActions>
    <Button>Boshlash</Button>
  </CardActions>
</Card>
```

### 3.3. Progress Bar (Progress)

```tsx
// Linear
<LinearProgress variant="determinate" value={75} />

// Circular
<CircularProgress variant="determinate" value={75} />

// Customized
<CircularProgress 
  variant="determinate" 
  value={75}
  size={120}
  thickness={8}
  sx={{ color: 'primary.main' }}
/>
```

### 3.4. Badge (Badj)

```tsx
<Badge badgeContent={12} color="error">
  <NotificationsIcon />
</Badge>

<Badge badgeContent="NEW" color="primary">
  <MailIcon />
</Badge>
```

### 3.5. Chip (Yorliq)

```tsx
<Chip label="Python" color="primary" />
<Chip label="Algoritmlar" variant="outlined" />
<Chip 
  label="O'rta daraja" 
  icon={<StarIcon />}
  onDelete={handleDelete}
/>
```

### 3.6. Alert (Ogohlantirish)

```tsx
<Alert severity="success">Muvaffaqiyatli!</Alert>
<Alert severity="info">Ma'lumot</Alert>
<Alert severity="warning">Ogohlantirish</Alert>
<Alert severity="error">Xato yuz berdi</Alert>
```

### 3.7. Dialog (Modal oyna)

```tsx
<Dialog open={open} onClose={handleClose}>
  <DialogTitle>Tasdiqlash</DialogTitle>
  <DialogContent>
    <DialogContentText>
      Rostdan ham chiqmoqchimisiz?
    </DialogContentText>
  </DialogContent>
  <DialogActions>
    <Button onClick={handleClose}>Yo'q</Button>
    <Button onClick={handleConfirm} color="primary">
      Ha
    </Button>
  </DialogActions>
</Dialog>
```

---

## 4. ANIMATSIYALAR VA O'TISHLAR

### 4.1. Sahifa o'tishlari

```tsx
// Framer Motion bilan
<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  exit={{ opacity: 0, y: -20 }}
  transition={{ duration: 0.3 }}
>
  Sahifa kontenti
</motion.div>
```

### 4.2. Hover effektlari

```css
.card {
  transition: all 0.3s ease;
}

.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 24px rgba(0,0,0,0.15);
}
```

### 4.3. Loading animatsiyalari

```tsx
// Skeleton loader
<Skeleton variant="rectangular" width={210} height={118} />
<Skeleton variant="text" />
<Skeleton variant="circular" width={40} height={40} />

// Shimmer effect
<Box className="shimmer">
  Loading content...
</Box>
```

### 4.4. Confetti (muvaffaqiyat bayramida)

```tsx
import Confetti from 'react-confetti';

// Test muvaffaqiyatli topshirilganda
{showConfetti && (
  <Confetti
    width={width}
    height={height}
    recycle={false}
    numberOfPieces={200}
  />
)}
```

---

## 5. RESPONSIV DIZAYN

### 5.1. Breakpoints

```tsx
const theme = createTheme({
  breakpoints: {
    values: {
      xs: 0,      // Telefon
      sm: 600,    // Kichik planshet
      md: 960,    // Planshet
      lg: 1280,   // Desktop
      xl: 1920,   // Katta ekran
    },
  },
});
```

### 5.2. Grid tizimi

```tsx
<Grid container spacing={3}>
  <Grid item xs={12} sm={6} md={4} lg={3}>
    {/* Kontent */}
  </Grid>
</Grid>
```

### 5.3. Media queries

```css
/* Telefon */
@media (max-width: 600px) {
  .dashboard { grid-template-columns: 1fr; }
}

/* Planshet */
@media (min-width: 600px) and (max-width: 960px) {
  .dashboard { grid-template-columns: repeat(2, 1fr); }
}

/* Desktop */
@media (min-width: 960px) {
  .dashboard { grid-template-columns: repeat(3, 1fr); }
}
```

---

## 6. ACCESSIBILITY (Kirish imkoniyati)

### 6.1. ARIA attributes

```tsx
<button 
  aria-label="Testni boshlash"
  aria-describedby="test-description"
>
  Boshlash
</button>

<div id="test-description" className="sr-only">
  Bu test 25 ta savoldan iborat va 60 daqiqa davom etadi
</div>
```

### 6.2. Klaviatura navigatsiyasi

- Tab - keyingi element
- Shift + Tab - oldingi element
- Enter/Space - tugmani bosish
- Esc - modal oynani yopish
- Arrow keys - ro'yxatda harakat

### 6.3. Contrast ratios

- Normal matn: 4.5:1 (AA standart)
- Katta matn: 3:1 (AA standart)
- Interaktiv elementlar: 3:1

---

## 7. GAMIFIKATSIYA ELEMENTLARI

### 7.1. Darajalar

```
🌱 Boshlang'ich (0-500 ball)
⭐ O'rta (501-1000 ball)
🏆 Yuqori (1001-2000 ball)
👑 Expert (2001+ ball)
```

### 7.2. Badjlar

```
🥇 1-o'rin - Lider
🎯 Top 10 - Eng yaxshilar qatorida
🔥 Seriya - 7 kun ketma-ket
⭐ Ustadlik - Barcha mavzular 90%+
💎 Mukammallik - 5 ta test 100%
🚀 Tezkor - 10 ta test 1 haftada
```

### 7.3. Progress animatsiyalari

```tsx
// XP bar animation
<motion.div
  className="xp-bar"
  initial={{ width: 0 }}
  animate={{ width: `${percentage}%` }}
  transition={{ duration: 1, ease: "easeOut" }}
/>

// Level up celebration
{levelUp && (
  <motion.div
    initial={{ scale: 0, opacity: 0 }}
    animate={{ scale: 1, opacity: 1 }}
    className="level-up-badge"
  >
    🎉 Level Up! ⭐
  </motion.div>
)}
```

---

**DIZAYN SPETSIFIKATSIYA YAKUNLANDI**

Keyingi: Backend arxitekturasi va API development

