# GitHub’da APK üretmek

Bu ortam APK derleyecek kadar RAM’e sahip değil. **GitHub Actions** (ücretsiz) senin için derler.

## 1) Yeni repo aç

1. [github.com/new](https://github.com/new)
2. İsim örneği: `veysel-seker-stitch`
3. **Public** veya Private (ikisi de olur)
4. README ekleme, boş oluştur

## 2) Bu klasörü yükle

Bilgisayarında (veya GitHub web “Upload files”):

```bash
cd VEYSEL_SEKER
git init
git add .
git commit -m "Veysel Seker Stitch Studio + Android APK CI"
git branch -M main
git remote add origin https://github.com/KULLANICI/veysel-seker-stitch.git
git push -u origin main
```

GitHub web’den yüklüyorsan **tüm klasörü** at: `android/`, `app/`, `.github/`, `main.py` …

`android/local.properties` gitmesin (zaten `.gitignore`’da).

## 3) APK’yı indir

1. Repo sayfası → **Actions**
2. İlk kez ise yeşil **I understand my workflows** de
3. Solda **APK üret** → **Run workflow** (veya push otomatik başlar)
4. Yeşil tik (~3–6 dk)
5. Alttaki **VeyselSeker-APK** artifact → **Download**
6. Zip içinden `VeyselSeker-StitchStudio.apk`

## 4) Telefona kur

1. APK’yı WhatsApp / Drive / USB ile telefona at
2. Dosyaya bas → **Yükle**
3. “Bilinmeyen uygulamalar” izni isteyebilir — ver
4. Play Store gerekmez

Debug APK’dır; kendi telefonunda çalışır. Mağazaya koymak ayrı imza ister.

## Hata olursa

Actions kırmızıysa log’u aç, “APK derle” adımındaki kırmızı satırı kopyala.
