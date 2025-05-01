import tkinter as tk
from PIL import Image, ImageTk

class NakotnesProfesija:   #tiek definēta klase
    def __init__(self, root):   #tiek definēti galvenie parametri
        self.root = root
        self.root.title("Viktorīna: Tava nākotnes profesija")
        self.root.geometry("600x600")
        self.root.configure(bg="#dbe9f4")
        self.root.resizable(False, False)

        try:   #tiek atvērts attēls
            self.image = Image.open("Profesijas.png")
            self.photo = ImageTk.PhotoImage(self.image)
        except Exception:
            self.photo = None   #ja nevar atrast attēlu, tas netiek ievietots
#jautājumu un atbilžu saraksts
        self.jaut = [
            {"jaut": "Kāds priekšmets tev skolā patīk vislabāk?", "answers": ["Bioloģija", "Matemātika", "Ekonomika", "Māksla"]},
            {"jaut": "Kas tevi visvairāk raksturo?", "answers": ["Palīdzēt citiem", "Risināt problēmas", "Uzņemties vadību", "Izpaust radošumu"]},
            {"jaut": "Kur tu labprātāk strādātu?", "answers": ["Slimnīcā", "Tehnoloģiju uzņēmumā", "Savā uzņēmumā", "Radošā studijā"]},
            {"jaut": "Kuru aktivitāti tu izvēlētos brīvajā laikā?", "answers": ["Pētīt veselības jautājumus", "Būvēt robotus", "Organizēt pasākumus", "Zīmēt vai gleznot"]},
            {"jaut": "Kas tevi visvairāk motivē?", "answers": ["Glābt dzīvības", "Radīt jaunas tehnoloģijas", "Gūt panākumus", "Izpaust emocijas"]},
            {"jaut": "Kā tu parasti risini problēmas?", "answers": ["Meklēju palīdzību un informāciju", "Izstrādāju tehnisku risinājumu", "Plānoju stratēģiju", "Izmantoju radošu pieeju"]},
            {"jaut": "Kāda veida filmas tev patīk?", "answers": ["Medicīnas drāmas", "Zinātniskā fantastika", "Biogrāfijas par uzņēmējiem", "Mākslas filmas"]},
            {"jaut": "Kāds ir tavs sapņu darbs?", "answers": ["Ārsts", "Inženieris", "Uzņēmējs", "Mākslinieks"]},
            {"jaut": "Kas tev padodas vislabāk?", "answers": ["Klausīties cilvēkus", "Domāt loģiski", "Pārliecināt citus", "Radīt ko jaunu"]},
            {"jaut": "Ko tu vēlētos izdarīt pasaules labā?", "answers": ["Uzlabot veselības aprūpi", "Izgudrot ko noderīgu", "Palīdzēt cilvēkiem kļūt veiksmīgākiem", "Iedvesmot ar mākslu"]},
            {"jaut": "Kādā vidē tu jūties vislabāk?", "answers": ["Slimnīcā", "Laboratorijā", "Birojā", "Studijā"]},
            {"jaut": "Kāda ir tava lielākā stiprā puse?", "answers": ["Empātija", "Analītiskā domāšana", "Vadītprasmes", "Radošums"]},
            {"jaut": "Kuru profesiju tu esi ieinteresēts izpētīt?", "answers": ["Mediķis", "Inženieris", "Vadītājs", "Dizaineris"]},
            {"jaut": "Ko tu visbiežāk dari komandā?", "answers": ["Palīdzu un atbalstu", "Radu risinājumus", "Vadu un koordinēju", "Piedāvāju idejas"]},
            {"jaut": "Kāda vērtība tev ir vissvarīgākā?", "answers": ["Palīdzība", "Inovācija", "Brīvība", "Izpausme"]}
        ]
#mērāmie rezultāti
        self.nozares = {
            "Medicīna": 0,
            "Inženierija": 0,
            "Uzņēmējdarbība": 0,
            "Māksla": 0
        }

        self.jaut_index = 0   #sākuma jautājuma indekss

        self.frame = None  #attēlos saturu
        self.create_sakums()    #tiek izsaukts sākuma ekrāns

    def create_sakums(self):   #izveido sākuma logu
        
        if self.frame is not None:
            self.frame.destroy()  #vecais rāmis tiek iznīcināts
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)    #pievienots rāmis logam

        if self.photo:   #parādīts attēls
            img_label = tk.Label(self.frame, image=self.photo, bg="#dbe9f4")
            img_label.pack(pady=10)
#spēles nosaukums
        nosaukums = tk.Label(self.frame, text="Kāda ir Tava nākotnes profesija?", font=("Helvetica", 22, "bold"),
                             fg="#12355b", bg="#dbe9f4")
        nosaukums.pack(pady=20)
#poga spēles sākumam
        sakuma = tk.Button(self.frame, text="Sākt", command=self.show_question,
                           font=("Helvetica", 16, "bold"), bg="#1976D2", fg="white", width=20)
        sakuma.pack(pady=20)
#parāda nākamo jautājumu un atbildes
    def show_question(self):
        if self.jaut_index < len(self.jaut):   #pārbauda vai ir jāuzdod vēl jautājumi
            if self.frame is not None:
                self.frame.destroy()  #vecais rāmis iznīcināts
            self.frame = tk.Frame(self.root)   
            self.frame.pack(fill=tk.BOTH, expand=True)   #jauns rāmis

            jaut = self.jaut[self.jaut_index]   #jautājums
#jautājumu nummurs
            jaut_nr = tk.Label(self.frame, text=f"Jautājums {self.jaut_index + 1} no {len(self.jaut)}",
                               font=("Helvetica", 12, "bold"), bg="#dbe9f4", fg="#12355b")
            jaut_nr.pack(pady=(10, 0))
#jautājums
            jaut_label = tk.Label(self.frame, text=jaut["jaut"], font=("Helvetica", 16, "bold"),
                                  bg="#dbe9f4", fg="#12355b", wraplength=550)
            jaut_label.pack(pady=10)
#atbilžu pogas
            for idx, answer in enumerate(jaut["answers"]):
                answer_btn = tk.Button(self.frame, text=answer, font=("Helvetica", 12), bg="#64B5F6", fg="white", width=40,
                                       command=lambda idx=idx: self.answer(idx))
                answer_btn.pack(pady=5)
#parādīts attēls
            if self.photo:
                img_label = tk.Label(self.frame, image=self.photo, bg="#dbe9f4")
                img_label.pack(pady=10)
        else:
            self.show_result()   #ja vairs nav jautājumu rāda rezultātu
#apstrādā atbildi un pāriet tālāk
    def answer(self, idx):
        if idx == 0:
            self.nozares["Medicīna"] += 1
        elif idx == 1:
            self.nozares["Inženierija"] += 1
        elif idx == 2:
            self.nozares["Uzņēmējdarbība"] += 1
        elif idx == 3:
            self.nozares["Māksla"] += 1

        self.jaut_index += 1   #palielina jautājumu skaitu
        self.show_question()   #rāda nākamo jautājumu
#parāda rezultātu
    def show_result(self):
        if self.frame is not None:
            self.frame.destroy()  #iznīcina veco rāmi
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        best_field = max(self.nozares, key=self.nozares.get)   #atrod nozari, pie kuras ir visvairāk punktu
#rezultāta paziņojums
        result_label = tk.Label(self.frame, text=f"Tava nākotnes profesijas joma ir: {best_field}",
                                font=("Helvetica", 18, "bold"), fg="#2e7d32", bg="#dbe9f4")
        result_label.pack(pady=30)

        descriptions = {   #iespējamie komentāri
            "Medicīna": "Tava līdzjūtība un rūpes par citiem liecina, ka būtu lielisks medicīnas speciālists!",
            "Inženierija": "Tava loģiskā domāšana un precizitāte rāda, ka inženierija ir Tavs aicinājums!",
            "Uzņēmējdarbība": "Tava uzņēmība un vadītprasmes palīdzēs Tev gūt panākumus biznesā!",
            "Māksla": "Tava radošā daba un iztēle ved Tevi uz mākslas pasauli!"
        }
#rezultāta apraksts
        result_desc_label = tk.Label(self.frame, text=descriptions[best_field], font=("Helvetica", 14),
                                     bg="#dbe9f4", fg="#333333", wraplength=550)
        result_desc_label.pack(pady=20)
#parāda attēlu
        if self.photo:
            img_label = tk.Label(self.frame, image=self.photo, bg="#dbe9f4")
            img_label.pack(pady=10)

# programmas starts
root = tk.Tk()
app = NakotnesProfesija(root)
root.mainloop()
