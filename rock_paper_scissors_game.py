import tkinter as tk
import random
from tkinter import messagebox

# Global değişkenler
oyuncu_galibiyetleri = 0
bilgisayar_galibiyetleri = 0
dil = "tr"  # Varsayılan dil Türkçe

# Oyun kuralları
kurallar_en = (
    "1. Rock beats scissors.\n"
    "2. Scissors beat paper.\n"
    "3. Paper beats rock.\n"
    "4. The first to win two rounds wins the game.\n"
    "5. Select rock, paper, or scissors to start the game.\n"
    "6. To exit the game, use the 'Exit' button."
)

kurallar_tr = (
    "1. Taş, makası yener.\n"
    "2. Makas, kağıdı yener.\n"
    "3. Kağıt, taşı yener.\n"
    "4. İlk iki turu kazanan oyunun galibi olur.\n"
    "5. Oyunu başlatmak için taş, kağıt veya makas seçin.\n"
    "6. Oyundan çıkmak için 'Çıkış' butonunu kullanın."
)

# Oyun mantığını işleyen fonksiyon
def tas_kagit_makas_RECEP_KIZIL(oyuncu_secimi):
    global oyuncu_galibiyetleri, bilgisayar_galibiyetleri

    secenekler = ["rock", "paper", "scissors"]
    bilgisayar_secimi = random.choice(secenekler)

    secim_metni = {
        "rock": {"en": "rock", "tr": "taş"},
        "paper": {"en": "paper", "tr": "kağıt"},
        "scissors": {"en": "scissors", "tr": "makas"}
    }

    bilgisayar_secimi_text = secim_metni[bilgisayar_secimi][dil]

    if oyuncu_secimi == bilgisayar_secimi:
        mesaj = f"Draw! Computer also chose {bilgisayar_secimi_text}." if dil == "en" else f"Beraberlik! Bilgisayar da {bilgisayar_secimi_text} seçti."
    elif (oyuncu_secimi == "rock" and bilgisayar_secimi == "scissors") or \
         (oyuncu_secimi == "scissors" and bilgisayar_secimi == "paper") or \
         (oyuncu_secimi == "paper" and bilgisayar_secimi == "rock"):
        mesaj = f"You won this round! Computer chose {bilgisayar_secimi_text}." if dil == "en" else f"Bu turu kazandınız! Bilgisayar {bilgisayar_secimi_text} seçti."
        oyuncu_galibiyetleri += 1
    else:
        mesaj = f"Computer won this round! Computer chose {bilgisayar_secimi_text}." if dil == "en" else f"Bu turu bilgisayar kazandı! Bilgisayar {bilgisayar_secimi_text} seçti."
        bilgisayar_galibiyetleri += 1
    
    # Skorları güncelle
    skor_label.config(text=get_skor_text())

    # Seçimlerin ekranda gösterilmesi
    sonuc_label.config(text=mesaj)

    # Galibiyet durumunu kontrol et
    if oyuncu_galibiyetleri == 2 or bilgisayar_galibiyetleri == 2:
        oyun_sonu()

# Oyun bittikten sonra sonucu kontrol eden fonksiyon
def oyun_sonu():
    if oyuncu_galibiyetleri == 2:
        if dil == "en":
            kazanma_mesaji = "Congratulations, you won the game!"
        else:
            kazanma_mesaji = "Tebrikler, oyunu kazandınız!"
        messagebox.showinfo("Game Over", kazanma_mesaji)
    elif bilgisayar_galibiyetleri == 2:
        if dil == "en":
            kaybetme_mesaji = "Unfortunately, the computer won the game."
        else:
            kaybetme_mesaji = "Maalesef, oyunu bilgisayar kazandı."
        messagebox.showinfo("Game Over", kaybetme_mesaji)

    oyuna_devam_etmek_iste_mesaj()

# Oyuna devam etmek isteyip istemediğini soran fonksiyon
def oyuna_devam_etmek_iste_mesaj():
    global oyuncu_galibiyetleri, bilgisayar_galibiyetleri

    # Bilgisayarın kararı
    bilgisayar_karari = random.choice(["yes", "no"])

    if dil == "en":
        devam_mesaji = "Do you want to continue playing?"
    else:
        devam_mesaji = "Oynamaya devam etmek istiyor musunuz?"

    response = messagebox.askquestion("Continue Playing", devam_mesaji)

    if response == 'yes' and bilgisayar_karari == 'yes':
        oyuncu_galibiyetleri = 0
        bilgisayar_galibiyetleri = 0
        sonuc_label.config(text=hosgeldin_mesaji)
        skor_label.config(text=get_skor_text())
    else:
        if bilgisayar_karari == 'no':
            bilgisayar_mesaj = "Computer decided not to continue." if dil == "en" else "Bilgisayar devam etmek istemedi."
        else:
            bilgisayar_mesaj = "You decided not to continue." if dil == "en" else "Siz devam etmek istemediniz."
        messagebox.showinfo("Game Over", bilgisayar_mesaj)
        pencere.quit()

# Skorları metin formatında döndüren fonksiyon
def get_skor_text():
    if dil == "en":
        return f"Player: {oyuncu_galibiyetleri} | Computer: {bilgisayar_galibiyetleri}"
    else:
        return f"Oyuncu: {oyuncu_galibiyetleri} | Bilgisayar: {bilgisayar_galibiyetleri}"

# Oyun kurallarını ekranda göstermek için fonksiyon
def kurallar_goster():
    if dil == "en":
        kurallar_label.config(text=kurallar_en)
    else:
        kurallar_label.config(text=kurallar_tr)

    # Kuralları oyunun başlığının hemen altına taşı
    kurallar_label.pack(before=sonuc_label, pady=10)

# Dil seçimi fonksiyonu
def dil_secimi(secim):
    global dil, hosgeldin_mesaji
    dil = secim
    if dil == "en":
        hosgeldin_mesaji = "Rock Paper Scissors! Make a choice to start."
        tas_text = "Rock"
        kagit_text = "Paper"
        makas_text = "Scissors"
        geri_button_text = "Back"
        cikis_button_text = "Exit"
    else:
        hosgeldin_mesaji = "Taş, Kağıt, Makas! Başlamak için bir seçim yapın."
        tas_text = "Taş"
        kagit_text = "Kağıt"
        makas_text = "Makas"
        geri_button_text = "Geri"
        cikis_button_text = "Çıkış"

    sonuc_label.config(text=hosgeldin_mesaji)

    # Dil seçimi yapıldıktan sonra mesajları gizle
    dil_seçim_mesajı.pack_forget()
    karşılama_mesajı.pack_forget()

    # Dil seçimi yapıldıktan sonra butonları göster ve dilini ayarla
    tas_button.config(text=tas_text)
    kagit_button.config(text=kagit_text)
    makas_button.config(text=makas_text)
    
    tr_button.pack_forget()
    en_button.pack_forget()
    
    tas_button.pack(pady=10)
    kagit_button.pack(pady=10)
    makas_button.pack(pady=10)

    # Geri ve Çıkış butonlarını ekle
    geri_button.config(text=geri_button_text)
    cikis_button.config(text=cikis_button_text)
    geri_button.pack(side="left", padx=20, pady=10)
    cikis_button.pack(side="right", padx=20, pady=10)

    # Skoru sadece oyun başladığında göster
    skor_label.pack(pady=10)

    # Oyun kurallarını göster
    kurallar_goster()

# Geri butonu fonksiyonu
def geri_don():
    # Oyun ekranını temizle ve dil seçim ekranına dön
    tas_button.pack_forget()
    kagit_button.pack_forget()
    makas_button.pack_forget()
    geri_button.pack_forget()
    cikis_button.pack_forget()
    skor_label.pack_forget()
    kurallar_label.pack_forget()
    sonuc_label.config(text="")

    dil_seçim_mesajı.pack(pady=10)
    karşılama_mesajı.pack(pady=10)
    tr_button.pack(pady=10)
    en_button.pack(pady=10)

# Çıkış butonu fonksiyonu
def cikis_oyunu_kapat():
    messagebox.showinfo("Exit", "Exiting the game. Goodbye!")
    pencere.quit()

# Tkinter ana pencere oluşturulması
pencere = tk.Tk()
pencere.title("Rock Paper Scissors / Taş Kağıt Makas")
pencere.state('zoomed')

# Karşılama mesajı
dil_seçim_mesajı = tk.Label(pencere, text="Select a language / Dil seçin", font=("Arial", 18))
dil_seçim_mesajı.pack(pady=10)

karşılama_mesajı = tk.Label(pencere, text="Welcome to Rock Paper Scissors / Taş Kağıt Makas", font=("Arial", 14))
karşılama_mesajı.pack(pady=10)

# Dil seçenekleri butonları
tr_button = tk.Button(pencere, text="Türkçe", font=("Arial", 14), command=lambda: dil_secimi("tr"))
tr_button.pack(pady=10)

en_button = tk.Button(pencere, text="English", font=("Arial", 14), command=lambda: dil_secimi("en"))
en_button.pack(pady=10)

# Oyuncu seçimi butonları
tas_button = tk.Button(pencere, text="", font=("Arial", 14), command=lambda: tas_kagit_makas_RECEP_KIZIL("rock"))
kagit_button = tk.Button(pencere, text="", font=("Arial", 14), command=lambda: tas_kagit_makas_RECEP_KIZIL("paper"))
makas_button = tk.Button(pencere, text="", font=("Arial", 14), command=lambda: tas_kagit_makas_RECEP_KIZIL("scissors"))

# Geri ve Çıkış butonları
geri_button = tk.Button(pencere, text="", font=("Arial", 14), command=geri_don)
cikis_button = tk.Button(pencere, text="", font=("Arial", 14), command=cikis_oyunu_kapat)

# Sonuç ve skor etiketi
sonuc_label = tk.Label(pencere, text="", font=("Arial", 14))
sonuc_label.pack(pady=10)

skor_label = tk.Label(pencere, text="", font=("Arial", 14))

# Kurallar etiketi
kurallar_label = tk.Label(pencere, text="", font=("Arial", 12))

# Pencereyi çalıştırma
pencere.mainloop()