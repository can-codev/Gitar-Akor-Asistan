# Gitar Akor Asistanı

PyQt5 ile geliştirilmiş, modern arayüze sahip bir **Gitar Akor Asistanı** uygulamasıdır.

Bu uygulama ile:

- Akorları listeleyebilir
- Akor şemalarını görebilir
- Parmak numaralarını inceleyebilir
- Akor pratiği yapabilir
- Mikrofon ile temel nota/akor tahmini alabilir
- Sanal piyano kullanabilirsiniz

---

## Özellikler

### Akor Sözlüğü
- Majör, minör, 7'li ve maj7 akorları görüntüleme
- Arama kutusu ile akor filtreleme
- Akor tipi seçme
- Akor diyagramı üzerinde parmak numaralarını gösterme

### Akor Pratiği
- Rastgele akor gösterimi
- Doğru / yanlış işaretleme
- Skor takibi
- Başarı oranı hesaplama
- Süreli pratik modu

### Akor Tanıma (Test Edilmedi)
- Mikrofon üzerinden temel frekans analizi
- Nota ve akor tahmini
- Tanınan akor geçmişi

### Sanal Piyano
- Fare ile nota çalma
- Klavye ile nota çalma
- Oktav değiştirme
- Sustain desteği
- Ses seviyesi ayarı

---

## Gereksinimler

Bu proje **Python 3** ile çalışır.

Gerekli Python paketleri:

- PyQt5
- numpy
- pyaudio

## Kurulum

- git clone https://github.com/can-codev/Gitar-Akor-Asistan.git
- cd Gitar-Akor-Asistan
- pip3 install -r requirements.txt
- python gitar_akor_asistani.py

---

## Proje Yapısı

```bash
Gitar-Akor-Asistan/
├── gitar_akor_asistani.py
├── requirements.txt
└── README.md
