import tkinter as tk
from PIL import Image, ImageTk

class NakotnesProfesija:
    def __init__(self, root):   #galveno logu
        self.root = root
        self.root.title("Viktorīna: Tava nākotnes profesija")   #loga virsraksts
        self.root.geometry("600x600")   #loga izmērs
        self.root.configure(bg="#dbe9f4")   #loga krāsa
        self.root.resizable(False, False)   #nosaka, ka loga izmēru nevarēs mainīt

        try:
            self.image = Image.open("Profesijas.png")   #atver attēlu
            self.photo = ImageTk.PhotoImage(self.image)   #pārveido attēlu
        except Exception:
            self.photo = None   #ja nevar ielādēt attēlu, tas neparādās

        self.jaut = [   #saraksts ar visiem jautājumiem un atbildēm
            {"jaut": "Kāds priekšmets tev skolā patīk vislabāk?", "atbildes": ["Bioloģija", "Matemātika", "Ekonomika", "Māksla"]},
            {"jaut": "Kas tevi visvairāk raksturo?", "atbildes": ["Palīdzēt citiem", "Risināt problēmas", "Uzņemties vadību", "Izpaust radošumu"]},
            {"jaut": "Kur tu labprātāk strādātu?", "atbildes": ["Slimnīcā", "Tehnoloģiju uzņēmumā", "Savā uzņēmumā", "Radošā studijā"]},
            {"jaut": "Kuru aktivitāti tu izvēlētos brīvajā laikā?", "atbildes": ["Pētīt veselības jautājumus", "Būvēt robotus", "Organizēt pasākumus", "Zīmēt vai gleznot"]},
            {"jaut": "Kas tevi visvairāk motivē?", "atbildes": ["Glābt dzīvības", "Radīt jaunas tehnoloģijas", "Gūt panākumus", "Izpaust emocijas"]},
            {"jaut": "Kā tu parasti risini problēmas?", "atbildes": ["Meklēju palīdzību un informāciju", "Izstrādāju tehnisku risinājumu", "Plānoju stratēģiju", "Izmantoju radošu pieeju"]},
            {"jaut": "Kāda veida filmas tev patīk?", "atbildes": ["Medicīnas drāmas", "Zinātniskā fantastika", "Biogrāfijas par uzņēmējiem", "Mākslas filmas"]},
            {"jaut": "Kāds ir tavs sapņu darbs?", "atbildes": ["Ārsts", "Inženieris", "Uzņēmējs", "Mākslinieks"]},
            {"jaut": "Kas tev padodas vislabāk?", "atbildes": ["Klausīties cilvēkus", "Domāt loģiski", "Pārliecināt citus", "Radīt ko jaunu"]},
            {"jaut": "Ko tu vēlētos izdarīt pasaules labā?", "atbildes": ["Uzlabot veselības aprūpi", "Izgudrot ko noderīgu", "Palīdzēt cilvēkiem kļūt veiksmīgākiem", "Iedvesmot ar mākslu"]},
            {"jaut": "Kādā vidē tu jūties vislabāk?", "atbildes": ["Slimnīcā", "Laboratorijā", "Birojā", "Studijā"]},
            {"jaut": "Kāda ir tava lielākā stiprā puse?", "atbildes": ["Empātija", "Analītiskā domāšana", "Vadītprasmes", "Radošums"]},
            {"jaut": "Kuru profesiju tu esi ieinteresēts izpētīt?", "atbildes": ["Mediķis", "Inženieris", "Vadītājs", "Dizaineris"]},
            {"jaut": "Ko tu visbiežāk dari komandā?", "atbildes": ["Palīdzu un atbalstu", "Radu risinājumus", "Vadu un koordinēju", "Piedāvāju idejas"]},
            {"jaut": "Kāda vērtība tev ir vissvarīgākā?", "atbildes": ["Palīdzība", "Inovācija", "Brīvība", "Izpausme"]}
        ]

        self.nozares = {
            "Medicīna": 0,
            "Inženierija": 0,
            "Uzņēmējdarbība": 0,
            "Māksla": 0
        }   #saglabā puktus katrai kategorijai

        self.jaut_index = 0   #saglabā jautājuma indeksu

        self.frame = tk.Frame(self.root)   #izveido saturu
        self.frame.pack_forget()  #sākotnēji to nerāda

        self.create_sakums()   #parāda sākuma ekrānu

    def reset_frame(self):
        self.frame.destroy()   #noņem iepriekšējo saturu
        self.frame = tk.Frame(self.root, bg="#dbe9f4")   #izveido jaunu saturu
        self.frame.pack(fill=tk.BOTH, expand=True)   #aizpilda logu

    def create_sakums(self):
        self.reset_frame()   #attīra logu

        if self.photo:   #ja ir attēls - to parāda
            img_label = tk.Label(self.frame, image=self.photo, bg="#dbe9f4")
            img_label.pack(pady=10)

        nosaukums = tk.Label(self.frame, text="Kāda ir Tava nākotnes profesija?", font=("Arial", 22, "bold"),   #virsraksts
                             fg="#12355b", bg="orange")
        nosaukums.pack(pady=20)

        sakuma = tk.Button(self.frame, text="Sākt", command=self.show_question,   #sākma poga
                           font=("Arial", 16, "bold"), bg="#1976D2", fg="white", width=20)
        sakuma.pack(pady=20)

    def show_question(self):
        if self.jaut_index < len(self.jaut):   #ja ir atlikuši vēl jautājumi
            self.reset_frame()   #notīra ekrānu
            jaut = self.jaut[self.jaut_index]  #parāda nākamo jautājumu

            jaut_nr = tk.Label(self.frame, text=f"{self.jaut_index + 1}. no {len(self.jaut)} jautājumiem",   #rāda jautājuma numuru
                               font=("Arial", 12, "bold"), bg="#dbe9f4", fg="#12355b")
            jaut_nr.pack(pady=(10, 0))

            jaut_label = tk.Label(self.frame, text=jaut["jaut"], font=("Arial", 16, "bold"),   #jautājuma teksts
                                  bg="orange", fg="#12355b", wraplength=550)
            jaut_label.pack(pady=10)

            for idx in range(len(jaut["atbildes"])):   #pogas katrai atbildei
                answer = jaut["atbildes"][idx]
                answer_btn = tk.Button(self.frame, text=answer, font=("Arial", 12), bg="#64B5F6", fg="white", width=40,
                                       command=lambda idx=idx: self.answer(idx))
                answer_btn.pack(pady=5)

            if self.photo:   #attēls pie katra jautājuma
                img_label = tk.Label(self.frame, image=self.photo, bg="#dbe9f4")
                img_label.pack(pady=10)
        else:
            self.show_result()   #ja vairs jautājumu nav, rāda rezultātu

    def answer(self, idx):
        if idx == 0:
            self.nozares["Medicīna"] += 1
        elif idx == 1:
            self.nozares["Inženierija"] += 1
        elif idx == 2:
            self.nozares["Uzņēmējdarbība"] += 1
        elif idx == 3:
            self.nozares["Māksla"] += 1

        self.jaut_index += 1   #pāriet uz nākamo jautājumu
        self.show_question()   #rāda nākamo jautājumu

    def show_result(self):
        self.reset_frame()   #notīra ekrānu

        max_punkti = max(self.nozares.values())   #nosaka augstāko punktu skaitu
        piemerotakie = [nozare for nozare, punkti in self.nozares.items() if punkti == max_punkti]

        komentari = {   #komentāri katrai profesijai
            "Medicīna": "Tava līdzjūtība un rūpes par citiem liecina, ka būtu lielisks medicīnas speciālists!",
            "Inženierija": "Tava loģiskā domāšana un precizitāte rāda, ka inženierija ir Tavs aicinājums!",
            "Uzņēmējdarbība": "Tava uzņēmība un vadītprasmes palīdzēs Tev gūt panākumus biznesā!",
            "Māksla": "Tava radošā daba un iztēle ved Tevi uz mākslas pasauli!"
        }

        if len(piemerotakie) == 1:
            nozare = piemerotakie[0]
            result_text = f"Tava nākotnes profesijas joma ir: {nozare}"
            kom_teksts = komentari[nozare]
        else:   #ja ir vairākas profesijas ar augstāko punktu skaitu
            result_text = "Tavas nākotnes profesijas jomas ir: " + " un ".join(piemerotakie)   #rezultāta virsraksts
            kom_teksts = "Tu esi daudzpusīgs! Tavā priekšā ir daudz iespēju – izvēlies sev sirdij tuvāko!"   #komentārs

        result_label = tk.Label(self.frame, text=result_text, font=("Arial", 18, "bold"),   #rezultāta virsraksts
                                fg="#12355b", bg="orange", wraplength=550)
        result_label.pack(pady=30)

        result_kom_label = tk.Label(self.frame, text=kom_teksts,   #komentārs
                                    font=("Arial", 14), bg="#dbe9f4", fg="#333333", wraplength=550)
        result_kom_label.pack(pady=20)

        if self.photo:   #parāda attēlu
            img_label = tk.Label(self.frame, image=self.photo, bg="#dbe9f4")
            img_label.image = self.photo  #saglabā attēlu, lai tas netiktu izdzēsts
            img_label.pack(pady=10)

#startē programmu
root = tk.Tk()
app = NakotnesProfesija(root)
root.mainloop()
