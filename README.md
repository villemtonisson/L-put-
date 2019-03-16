# Log File Editor
### Töörežiimid
**One logfile** - Loodud ühest logifailist ülesannete eraldamiseks. Selle kasutamiseks peab olema sisse lülitatud "Separate by .py files". Eraldatud ülesannete logid tekivad samasse kohta, kui algse logi asukoht. Kui logi nimi on "logi.txt", siis tulemusfailide nimed on formaadis logi_111111.txt.

**One archive** - Loodud ühe arhiivifaili lahtipakkimiseks. Kasutada saab mõlemat lisavalikut. Kui kasutada kuupäevi lahtipakkimiseks, jäävad alles vaid failid, mille esimene kirje oli etteantud ajavahemikus. Kaust lahtipakitud failidega tekib samasse kausta, kus on arhiivifail ja selle nimeks saab arhiivifaili nimi. Näiteks, kui on fail "näidis.zip", siis logid jäävad kausta näidis.  

**Multiple logfiles** - Loodud mitmest logifailist ülesannete eraldamiseks. Käitub sama moodi, kui ühe logifailiga, kuid faili valides saab võtta mitu faili. 

**Multiple archives** - Loodud mitme arhiivi lahtipakkimiseks. Käitub sama moodi, kui ühe arhiivifailiga, luues kausta iga arhiivifaili jaoks. Samuti saab valida mitu faili. 

### Lisavalikud 
**Separate by .py files** - Teeb igast logifailist mitu logifaili, kus igas on kaasas informatsioon ühe .py failiga töötamise kohta. Samuti on kaasas kõik käsureal toimuv tegevus. Eraldatud logifailid jäävad samasse kausta, kui algne. Kui logi nimi on "logi.txt", siis tulemusfailide nimed on formaadis logi_111111.txt, kus 111111 asemel võib olla mistahes arv.

**"Unpack using dates** - Kehtib vaid arhiivifailide puhul. Pakib lahti, kõik logifailid ja seejärel eemaldab need, mille esimese kirje aeg pole etteantud ajavahemikus.

Lisavalikuid on võimalik kasutada ka koos.
### Aja sisestamine
Kuupäeva sisestamine käib klõpsates väljale Date. Seejärel avaneb kalender, kus saab valida soovitud päeva.  
Võib isestada ka kirjutades **YYYY-MM-DD** formaadis

Minutite ja tundide sisestamise jaoks võib klõpsata noolekest ja valida sobiv arv menüüst või sisestada see arv käsitsi.

Programmi normaalse töö jaoks tuleb sisestada nii algusaeg, kui ka lõpp. Kui tahta eraldada logisid kellaaegada järgi tuleb sisse lülitada ka "Unpack using dates".

	
### settings.json 
Selle programmi kasutamise jaoks on vajalik **7-Zip** olemasolu. Settings.json faili tuleb panna **loc-7z** alla jutumärkides oma **7z.exe** asukoht. Enne programmi kasutamist on vaja see kindlasti seadistada.

### Töö käik
1. Valida töörežiim Select mode alt
2. Soovi korral lülitada sisse lisavalikud
3. Kui on valitud aegade järgi eraldamine, tuleb sisestada kuupäevad ja kellaaeg
4. Valida fail(id) klõpsates nuppu "Pick File"
5. Klõpsata "Unpack nuppu"  
Kui valitud on mitme logifaili või arhiivi töörežiim, saab valida mitu faili hoides all **CTRL** või **SHIFT** nuppe.

### Programmi käivitamine
Programm on loodud kasutades Pythoni versiooni 3.6. Programmi tööks on vajalik, et ühes kaustas oleksid failid: settings.json, splitter.py, unpacker.py, datepicker.py ja GUI.py. Samuti tuleb settings.json faili lisada enda 7-Zipi asukoht Käivitada tuleb GUI.py. 
