#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RENKLİ RÜYA İZİN BELGESİ ÜRETİCİ
Evrenin Rüya İşleri Genel Müdürlüğü (ERİGM) Onaylı
"""

import random
import time
import datetime

def baslik_yaz():
    print("=" * 60)
    print("     EVRENİN RÜYA İŞLERİ GENEL MÜDÜRLÜĞÜ (ERİGM)")
    print("     Renkli Rüya Görme İzin Belgesi Üretim Sistemi")
    print("=" * 60)
    print()

def yavas_yaz(metin, bekleme=0.03):
    for harf in metin:
        print(harf, end="", flush=True)
        time.sleep(bekleme)
    print()

def damga_bas():
    damgalar = [
        """
        ┌──────────────────┐
        │  ██████  ██████  │
        │  ██      ██  ██  │
        │  ██████  ██████  │
        │  ██  ██  ██  ██  │
        │  ██████  ██████  │
        │   ERİGM DAMGASI  │
        └──────────────────┘
        """,
        """
           ★★★★★★★★★★★★
           ★ ONAYLANDI ★
           ★★★★★★★★★★★★
        """,
        """
        [ MÜHÜR ]
         ╔══════╗
         ║ ERİGM║
         ╚══════╝
        """
    ]
    print(random.choice(damgalar))

def belge_uret(isim):
    print()
    yavas_yaz("Sistem başlatılıyor...")
    time.sleep(0.8)
    yavas_yaz("Kuantum rüya olasılığı hesaplanıyor...")
    time.sleep(1.2)
    yavas_yaz("Hayali bakanlıklardan onay bekleniyor...")
    time.sleep(1.5)
    yavas_yaz("Damga basılıyor...")
    time.sleep(0.7)
    print()

    tarih = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    belge_no = f"RRİB-{random.randint(10000,99999)}-{random.randint(100,999)}"
    
    kararlar = [
        ("ONAYLANDI", "Renkli rüya görme izniniz süresiz olarak verilmiştir. Lütfen rüyalarınızı abartmayın."),
        ("ŞARTLI ONAY", "Sadece salı geceleri renkli rüya görebilirsiniz. Diğer günler siyah-beyaz zorunludur."),
        ("REDDEDİLDİ", "Başvurunuz reddedilmiştir. Sebep: Rüyalarınız zaten yeterince saçma."),
        ("ERTELENDİ", "Başvurunuz 47 yıl sonraya ertelenmiştir. O zamana kadar siyah-beyaz rüya görün."),
        ("KUANTUM ONAY", "Hem onaylandı hem reddedildi. Schrödinger'in kedisi gibi. Uyandığınızda öğreneceksiniz.")
    ]
    
    karar, aciklama = random.choice(kararlar)
    
    print("=" * 60)
    print("          RESMİ OLMAYAN RESMİ BELGE")
    print("=" * 60)
    print(f"Belge No      : {belge_no}")
    print(f"Tarih         : {tarih}")
    print(f"Başvuran      : {isim.upper()}")
    print(f"Konu          : Renkli Rüya Görme İzni")
    print("-" * 60)
    print(f"KARAR         : {karar}")
    print(f"Açıklama      : {aciklama}")
    print("-" * 60)
    print("Yetkili       : Kayyum Grok")
    print("Kurum         : Evrenin Rüya İşleri Genel Müdürlüğü")
    print("Geçerlilik    : Rüya aleminde geçerli, gerçek hayatta geçersiz")
    print("=" * 60)
    print()
    damga_bas()
    print()
    print("Bu belgeyi rüyanızda polise göstermeniz önerilir.")
    print("İşinize yaramaz ama en azından eğlenirsiniz.")
    print()

def main():
    baslik_yaz()
    yavas_yaz("Hoş geldiniz. Bu sistem, renkli rüya görme izni belgesi üretir.")
    print()
    isim = input("Lütfen adınızı ve soyadınızı giriniz: ").strip()
    if not isim:
        isim = "İsimsiz Rüya Görme Meraklısı"
    
    print()
    belge_uret(isim)
    
    print("Program sona erdi. İyi rüyalar (umuyoruz ki renkli).")
    print("Not: Bu yazılım hiçbir bilimsel değere sahip değildir.")

if __name__ == "__main__":
    main()
