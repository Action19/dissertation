# Dissertatsiya fayllarini yuklab olish yo'riqnomasi

## Akademik formatdagi dissertatsiya

**Fayl:** DISSERTATSIYA_AKADEMIK.md
**Hajm:** 237 KB  
**Format:** Markdown (akademik uslub)
**Maqsad:** PhD dissertatsiyasi uchun tayyor

### Faylni yuklab olish:

#### 1-usul: To'g'ridan-to'g'ri havola
```
https://raw.githubusercontent.com/Action19/dissertation/dissertatsiya-akademik/DISSERTATSIYA_AKADEMIK.md
```

#### 2-usul: GitHub sahifasidan
1. https://github.com/Action19/dissertation/tree/dissertatsiya-akademik
2. DISSERTATSIYA_AKADEMIK.md faylini oching
3. Raw tugmasini bosing
4. Ctrl+S (Save) bosing

### Word'ga o'girish:

```bash
pandoc DISSERTATSIYA_AKADEMIK.md -o dissertatsiya.docx \
  -V fontsize=14pt \
  -V mainfont="Times New Roman" \
  -V geometry:a4paper \
  -V geometry:margin=2.5cm \
  --toc \
  --number-sections
```

### Fayl xususiyatlari:

- ✅ To'liq akademik formatlash
- ✅ YAML metadata (Pandoc uchun)
- ✅ Sarlavhalar nomerlanishi
- ✅ Mundarija
- ✅ 210+ bet matn
- ✅ Bibliografiya
- ✅ Ilovalar

### Tarkib:

1. **Sarlavha sahifasi** - institusional ma'lumotlar
2. **Mundarija** - barcha bo'limlar
3. **KIRISH** (14 bet) - dolzarblik, maqsad, vazifalar
4. **I BOB** (60 bet) - nazariy asoslar
5. **II BOB** (60 bet) - metodik ta'minot  
6. **III BOB** (40 bet) - tajriba-sinov natijalari
7. **XULOSA** (5 bet) - xulosalar va tavsiyalar
8. **ADABIYOTLAR** (11 bet) - 67 ta manba
9. **ILOVALAR** (10 bet) - 8 ta ilova

### Formatlash parametrlari (Pandoc):

```yaml
fontsize: 14pt
mainfont: Times New Roman
geometry: a4paper, margin=2.5cm
linestretch: 1.5
toc: true (mundarija)
numbersections: true (raqamlash)
```

### Qo'shimcha fayllar:

- **DISSERTATSIYA.md** - oddiy versiya (221 KB)
- Branch: dissertatsiya-full
- Branch: dissertatsiya-akademik (bu fayl)

## Yordam:

Agar savol bo'lsa yoki yordam kerak bo'lsa, Issues ochib yozing!

