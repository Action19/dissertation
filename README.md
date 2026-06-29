# Dissertatsiya fayllarini yuklab olish yo'riqnomasi

## 📚 Dissertatsiya haqida

**Mavzu:** INFORMATIKA DARSLARIDA AXBOROT TEXNOLOGIYALARI ASOSIDA O'QUVCHILAR BILIMINI BAHOLASH TEXNOLOGIYASINI TAKOMILLASHTIRISH (9-10 sinf misolida)

**Daraja:** Pedagogika fanlari doktori (PhD)

---

## ✅ Yangilangan versiya (2026-06-29)

### 🎯 **Barcha snoskalar to'g'rilandi!**

- ✅ **60 ta to'liq ilmiy manba** ([^1] dan [^60] gacha)
- ✅ Pandoc konvertatsiyasida **hech qanday noaniq belgi yo'q**
- ✅ Word/PDF formatda barcha snoskalar to'g'ri ko'rinadi
- ✅ 4,495 qator (DISSERTATSIYA.md)
- ✅ 4,723 qator (DISSERTATSIYA_AKADEMIK.md)

---

## 📥 Fayllarni yuklab olish

### **1️⃣ GitHub orqali (tavsiya etiladi)**

Repository: https://github.com/Action19/dissertation/tree/dissertatsiya-akademik

**Fayllar:**
- `DISSERTATSIYA.md` (237 KB) - oddiy Markdown format
- `DISSERTATSIYA_AKADEMIK.md` (253 KB) - Pandoc uchun YAML metadata bilan

### **2️⃣ To'g'ridan-to'g'ri havolalar**

**DISSERTATSIYA.md:**
```
https://raw.githubusercontent.com/Action19/dissertation/dissertatsiya-akademik/DISSERTATSIYA.md
```

**DISSERTATSIYA_AKADEMIK.md:**
```
https://raw.githubusercontent.com/Action19/dissertation/dissertatsiya-akademik/DISSERTATSIYA_AKADEMIK.md
```

### **3️⃣ ZIP arxiv**

Butun repository:
```
https://github.com/Action19/dissertation/archive/refs/heads/dissertatsiya-akademik.zip
```

---

## 📝 Word formatga o'girish (Pandoc)

### **Pandoc o'rnatish:**

**Windows:**
```bash
winget install pandoc
```

**Mac:**
```bash
brew install pandoc
```

**Linux:**
```bash
sudo apt install pandoc
```

### **Konvertatsiya buyruqlari:**

#### **Asosiy konvertatsiya:**
```bash
pandoc DISSERTATSIYA_AKADEMIK.md -o DISSERTATSIYA.docx
```

#### **To'liq formatlangan versiya:**
```bash
pandoc DISSERTATSIYA_AKADEMIK.md -o DISSERTATSIYA.docx \
  --from markdown \
  --to docx \
  --toc \
  --number-sections \
  --reference-doc=reference.docx
```

**Parametrlar:**
- `--toc` - mundarija qo'shish
- `--number-sections` - bo'limlarni raqamlash
- `--reference-doc` - shrift va formatni shablon fayldan olish

#### **PDF ga o'girish:**
```bash
pandoc DISSERTATSIYA_AKADEMIK.md -o DISSERTATSIYA.pdf \
  --from markdown \
  --pdf-engine=xelatex \
  --toc \
  --number-sections
```

---

## 📊 Dissertatsiya tarkibi

### **Asosiy qismlar:**

| Bo'lim | Hajm | Tavsif |
|--------|------|--------|
| **KIRISH** | 14 bet | Mavzuning dolzarbligi, maqsad va vazifalar |
| **I BOB** | 60 bet | Ilmiy-nazariy asoslar |
| **II BOB** | 60 bet | Metodika va texnologiya |
| **III BOB** | 40 bet | Eksperimental natijalar va tahlil |
| **XULOSA** | 5 bet | Asosiy xulosalar va tavsiyalar |
| **ADABIYOTLAR** | 11 bet | 60 ta to'liq ilmiy manba |
| **ILOVALAR** | 10 bet | Jadvallar, grafiklar, testlar |

**JAMI:** ~210 bet, 4,700+ qator

---

## 📚 Ilmiy manbalar (60 ta)

### **Manbalar bo'yicha taqsimot:**

| Turi | Soni | Misollar |
|------|------|----------|
| **O'zbek manbalar** | 15 ta | Azizxo'jaeva, Yuldashev, Begimqulov |
| **Rus manbalar** | 8 ta | Vygotskiy, Tolipov, Xasanboyev |
| **Xorijiy manbalar** | 32 ta | Bloom, Black & Wiliam, Hattie, Dweck |
| **Davlat hujjatlari** | 5 ta | Prezident farmonlari, Davlat standartlari |

### **Mavzular bo'yicha:**
- Pedagogika nazariyasi (12 ta)
- Baholash texnologiyalari (18 ta)
- Informatika ta'limi (10 ta)
- Psixologiya (15 ta)
- Raqamli texnologiyalar (5 ta)

---

## 🔍 Snoska tizimi

### **Format:**
Matnda: `[^1]`, `[^2]`, ..., `[^60]`

Manbalar ro'yxatida:
```markdown
[^1]: Author. (Year). Title. Publisher. Pages.
```

### **Misol:**
```markdown
Matnda: "...baholash muhim ahamiyatga ega[^8]."

Manbalar ro'yxatida:
[^8]: Azizxo'jaeva N.N. (2016). *Pedagogik texnologiya va pedagogik mahorat*. 
      Toshkent: TDPU. 174 b.
```

### **✅ To'g'rilangan muammolar:**
- ❌ Eski versiya: `[^31]` kabi belgilar Wordda ko'rinmasdi
- ✅ Yangi versiya: Barcha 60 ta snoska to'liq manbalar bilan

---

## 💡 Pandoc konvertatsiya natijalari

Pandoc orqali Word/PDF ga o'girgandan keyin:
- ✅ Barcha snoskalar avtomatik sahifa pastiga chiqadi
- ✅ Raqamlash to'g'ri ishlaydi
- ✅ Manbalar to'liq ko'rinadi
- ✅ Formatlar saqlanadi (qalin, kursiv, jadvallar)

---

## 🎓 Foydalanish bo'yicha tavsiyalar

1. **DISSERTATSIYA.md** - oddiy o'qish, GitHub'da ko'rish uchun
2. **DISSERTATSIYA_AKADEMIK.md** - rasmiy hujjat tayyorlash uchun
3. Pandoc konvertatsiyasida `DISSERTATSIYA_AKADEMIK.md` faylidan foydalaning
4. Word'da qo'shimcha formatlashni amalga oshiring (shrift, intervalar)

---

## 📞 Qo'llab-quvvatlash

Savollaringiz bo'lsa, GitHub Issues orqali murojaat qiling:
https://github.com/Action19/dissertation/issues

---

**Oxirgi yangilanish:** 29.06.2026  
**Versiya:** 2.0 (Barcha snoskalar to'g'rilangan)  
**Status:** ✅ Tayyor
