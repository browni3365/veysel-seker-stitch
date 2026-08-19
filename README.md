# VEYSEL ŞEKER — Cross Stitch Pattern Studio

Yerel Python uygulaması. Görsel yükle → DMC pattern + PDF + mockup + Etsy listing + ZIP.

Lisans / aktivasyon **yoktur**. Çıktıları sen dağıtırsın.

## Kurulum

```bash
pip install pillow reportlab numpy
```

GUI için sistem `tkinter` yeterlidir (PyQt gerekmez).

## Test (V3+ tam pipeline)

```bash
cd /home/user/VEYSEL_SEKER
python3 run_v3plus_complete.py
```

Çıktı: `output/midnight-owl/` + `*_SHOP.zip` + `*_BUYER.zip`

## GUI

```bash
python3 main.py
```

## Motorlar (`app/`)

| Modül | İş |
|---|---|
| `pattern_engine` | Izgara + DMC kuantizasyon |
| `dmc_engine` | 450+ DMC renk |
| `pdf_engine` | Kapak, çok sayfa, 10’lu grid, 3 satır overlap, 5 sütun key, TR font |
| `mockup_engine` | Hoop / kare / dikdörtgen / close-up / lifestyle / Etsy hero |
| `etsy_engine` | Başlık, etiket, açıklama |
| `package_engine` | Shop + buyer ZIP |
| `qa_engine` | Boyut / renk uyarıları |

## Android APK (GitHub Actions)

Hazır APK bu klasörde yok. GitHub’a yükleyince Actions üretir.

Adımlar: [GITHUB_APK.md](GITHUB_APK.md)

## Notlar

V3’te “stok fotoğraf” yok — mockup’lar prosedürel (Aida dokusu + ahşap grain).
Premium fotoğraf eklemek istersen `mockup_engine` içine kendi JPG’lerini bağlayabilirsin.
