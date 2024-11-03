![Anka](.github/docs/img/logo.png)
<!-- Bu dosya, İngilizce olan README.md dosyasının Türkçe halidir.-->
# Anka

Anka Tarayıcısı v1.8

## Anka Browser nedir?

Anka Python'da PyQt6 ve QWebEngine ile geliştirilmiş açık kaynak bir tarayıcıdır.

Anka Browser'ı Python yüklü her cihazda indirip, kullanabilirsin.

---

## Anka v1.8:

- ### Diller:
   Artık, Anka Browser iki dili destekliyor. Türkçe ve İngilizce. İngilizce versiyonunu şuradan bulabilirsiniz
  ``/src/en-En/`` ve Türkçe versiyonunu ``/src/tr-TR/`` adresinden bulabilirsiniz.

- ### Geçmiş güncellemesi:
  Arama geçmişiniz /public/browser/history.txt dosyasına kaydedilir. Geçmişi silmek isterseniz, Ayarlar'dan “Geçmişi Sil” butonundan silebilirsiniz.
 
- ### PNG butonlar:
  Artık, ikonlar ``.png`` uzantısına sahip, ``.svg`` uzantısına sahip değil.

- ### Açık&Koyu Tema:
  Linux kullanıyorsanız ve sistem temanız açıksa, Anka Browser teması açık veya sistem temanız koyu ise, Anka Browser teması koyu olur.

- ### Tarayıcı Dosyaları Kontrolü:
  Eğer ``config/config.conf`` dosyası veya ``public/browser/history.txt`` dosyası bulunmaz veya silinirse, Anka Browser bunları varsayılan değişkenlerle oluşturur.

- ### Varsayılan Pencere Rengi:
  Artık, varsayılan sekme rengi HEX ile #2aa1b3'tür.

- ### Görünüm Düzen Güncellemesi:
  Artık, ana düzenin kenar boşlukları 0.

---

## Sonraki güncelleme ne?
***Sonraki güncelleme şunları içerir:***

- İndirilenler
- Yer imleri
- Çeviri(Belki)
- Ve daha fazla ekleneceği şuan kesin olarak belli olmayan şeyler

## Anka Browser'dan ekran görüntüleri:
![Screenshot](./.github/docs/img/image1.png)
![Screenshot2](./.github/docs/img/image2.png)
![Screenshot3](./.github/docs/img/image3.png)

## Bu projeye dahil edilmiş Python kütüphaneleri:

- PyQt6
- sys
- configparser

## Kodu nasıl derleyebilirim?
  ### İngilizce versiyon:
   Kaynak kodu indirin (isterseniz /src/tr-TR klasörünü indirmeyin). Ve dizini kaynak kodu indirdiğiniz klasöre değiştirin ve bu komutları terminale yazın:
    
  1. ``cd Anka``

  2. ``cd src``

  3. ``cd en-EN``

  4. ``python3 anka-browser.py``

  ### Türkçe Versiyon:
  Kaynak kodunu indirin, isterseniz ingilizce kaynak kodu indirmeyebilirsiniz. Kaynak kodunu
  indirdiğiniz klasöre geçin ve şu kodları terminale yazın:

  1. ``cd Anka``

  2. ``cd src``

  3. ``cd tr-TR``

  4. ``python3 anka-browser.py``


## Uyarılar:
> Bu proje "GNU GENERAL PUBLIC LICENSE" kullanır.
