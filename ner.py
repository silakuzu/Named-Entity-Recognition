import re
import sys

f_name = sys.argv[1]
input_file=open(f_name, encoding="utf8")
input_list = input_file.readlines()


with open('all_organizations.txt',encoding="utf8") as f:
    ORGANIZATIONS = f.read().splitlines()

with open('all_locations.txt',encoding="utf8") as f:
    LOCATIONS = f.read().splitlines()

with open('all_names.txt',encoding="utf8") as f:
    PERSON = f.read().splitlines()


months_days = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık', 
'ocak', 'şubat', 'mart', 'nisan', 'mayıs', 'haziran', 'temmuz', 'ağustos', 'eylül', 'ekim', 'kasım', 'aralık', 
'pazartesi', 'salı', 'çarşamba', 'perşembe', 'cuma', 'cumartesi', 'pazar', 
'Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']

appendixes = ['\'ta', '\'da', '\'ta', '\'nda', 
             '\'te', '\'de', '\'te', '\'nde']                                                   
cnt = 1
for line in input_list:

    line = line.rstrip()

    if '\'' in line:
        x = re.findall(r'(?=[A-ZÇĞİÖŞÜ][a-zçğıöşü]*)\'\w*\s+', line)
        if x:
            for ele in x:
                print("ele:", ele)
                line = line.replace(ele,'')
                print(line)
           

    #-------DATE-------
    #01/01/2000 (Different type of seperators)
    x = re.search(r'(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.]\d?\d?\d?\d?', line)
    if x:    
        print("LINE ", cnt, ": DATE", x.group(0))
        line = line.replace(x.group(0),'')


    #15 kasım 2020
    for month in months_days:
        x = re.search(r'([1-9]|[12][0-9]|3[01])\s' +month+ '\s\d?\d?\d?\d?', line)
        #print(month)
        if x:
            print("LINE ", cnt, ": DATE", x.group(0)) 
            line = line.replace(x.group(0),'')

    #2020 yılı
    if 'yıl' in line:
        x = re.findall(r'\d{4}(?=\s+yıl\w+)',line)
        if x:
            for ele in x:
                print("LINE ", cnt, ": DATE", ele)
                line = line.replace(ele,'')

    #Perşembe günü, Ocak ayı
    day_month = ['ay', 'gün']
    for sample in day_month:
        if sample in line:
            x = re.findall(r'[A-ZÇĞİÖŞÜ]?[a-zçğıöşü]*(?=\s+' +sample+ '\w+)',line)
            if x:
                for ele in x:
                    if ele:
                        print("LINE ", cnt, ": DATE", ele)
                        line = line.replace(ele,'')
               

    #2016'da
    for sample in appendixes:
        if sample in line:
            if re.search(r'\d{4}(?=' +sample+ ')',line):
                x = re.findall(r'\d{4}(?=' +sample+ ')',line)
                for ele in x:
                    print("LINE ", cnt, ": DATE", ele)
                    line = line.replace(ele,'')

            for uppercaseWord in re.finditer(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',line):
                uppercaseWord = line[uppercaseWord.start():uppercaseWord.end()]
        
                if uppercaseWord in LOCATIONS:
                    print("LINE ", cnt, ": LOCATION", uppercaseWord)
                    uppercaseWord = uppercaseWord.replace(ele,'')

            if re.search(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*(?=' +sample+ ')',line):
                x = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*(?=' +sample+ ')',line)
                for ele in x:
                    print("LINE ", cnt, ": LOCATION", ele)
                    line = line.replace(ele,'')
  
    #--------------ORGANIZATION------------------
    org_list = ['Üniversite', 'Holding', 'Vakfı', 'Federasyon', 'Enstitü', 'Kurum','Kurul', 'Banka','Bank', 
                'Lise', 'Ortaokul','İlkokul','Fakülte', 'Ofis', 'Kütüphane', 'Çifliği', 'Kulübü', 'Derneği', 'Bölüm', 'Ocağı',
                'gazete','dergi', 'parti', 'Hotel', 'Hastane', 'Bakanlığı'
                ]
    for sample in org_list:
        if sample in line:
            x = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]* ' + sample + '\w*', line)
            if x:
                for ele in x:
                    print("LINE ", cnt, ": ORGANIZATION", ele)

    if 'spor' in line:
        x = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*spor\w*', line)
        if x:
            for ele in x:
                print("LINE ", cnt, ": ORGANIZATION", ele)

    
    mgmt_list = ['Cumhuriyet', 'Krallığı', 'Devlet', 'Prensliği', 'Federasyon', 'İmparatorluğu']
    for sample in mgmt_list:
        if sample in line:
            x = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]* ' + sample + '\w*\'?', line)
            if x:
                for ele in x:
                    print("LINE ", cnt, ": ORGANIZATION", ele)
                    line = line.replace(ele,'')

    teams = ['Basketbol Takımı', 'Futbol Takımı', 'Tenis Takımı', 'Voleybol Takımı']
    for sample in teams:
        if sample in line: 
            x = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]* ' + sample + '\w*\'?', line)
            if x:
                for ele in x:
                    print("LINE ", cnt, ": ORGANIZATION", ele)
                    line = line.replace(ele,'')  

    comps = ['A.Ş', 'A.Ş', 'Inc.', 'LTD', 'Ltd']
    for sample in comps:
        if sample in line: 
            x = re.findall(r'[A-ZÇĞİÖŞÜ]&?[a-zçğıöşü]* ' + sample + '\w*\'?', line)
            if x:
                for ele in x:
                    print("LINE ", cnt, ": ORGANIZATION", ele)
                    line = line.replace(ele,'')  

    #---------------PERSON---------------
    honor_list = ['Hanım', 'Bey', 'Sayın', 'Bay', 'Bayan', 'Abi', 'Abla', 'Hoca','Öğretmen', 'Sevgili', 'Paşa', 'Ağa']
    for sample in honor_list:
        if sample in line:
            x = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*(?=\s+' +sample+ ')',line)
            if x:
                for ele in x:
                    print("LINE ", cnt, ": PERSON", ele)
                    line = line.replace(ele,'')

    pre_name = ['Prof. Dr.', 'Dr.', 'Prof.', 'Av.', 'Uzm.']
    for sample in pre_name:
        if sample in line:
            x = re.findall(r'(?<=\s' +sample+' )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',line)
            if x:
                for ele in x:
                    print("LINE ", cnt, ": PERSON", ele)
                    line = line.replace(ele,'')

    person_prefixes = ['Vekili','Yardımcısı', 'Başkanı','Cumhurbaşkanı', 'Vali', 'Başkanvekili', 'Milletvekili', 'Lideri']
    for sample in person_prefixes:
        if sample in line:
            x = re.findall(r'(?=' +sample+ '\s*)([A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s*)*',line)            
            if x:
                for ele in x:
                    print("LINE ", cnt, ": PERSON", ele)
                    line = line.replace(ele,'')


    #---------------LOCATION------------
    loc_list = ['ilçe', 'belde', 'köy', 'dağ',
    'Mahalle', 'Sokak', 'Sokağı', 'Bulvar', 'Cadde', 'Saray', 'Köşk', 'Kale', 'Köprü', 'Kule', 'Anıt', 'Camii',
    'Kıta', 'Bölge', 'Deniz', 'Nehir', 'Göl', 'Dağ', 'Boğaz', 'Mezarlığı', 'Irmağı', 'Nehri', 'Geçidi', 'Yaka', 'Meydan']
    for sample in loc_list:
        if sample in line:
            x = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]* ' + sample + '\w*\'?', line)
            if x:
                for ele in x:
                    print("LINE ", cnt, ": LOCATION", ele)
                    line = line.replace(ele,'')

    for sample in appendixes:
        if sample in line:
            x = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*(?=' +sample+ ')',line)
            if x:
                for ele in x:
                    print("LINE ", cnt, ": LOCATION", ele)
                    line = line.replace(ele,'')


    for uppercaseWord in re.finditer(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',line):
        uppercaseWord = line[uppercaseWord.start():uppercaseWord.end()]
        
        if uppercaseWord in LOCATIONS:
            print("LINE ", cnt, ": LOCATION", uppercaseWord)

        elif uppercaseWord in PERSON:
            print("LINE ", cnt, ": PERSON", uppercaseWord)
        elif uppercaseWord in ORGANIZATIONS:
            print("LINE ", cnt, ": ORGANIZATION", uppercaseWord)
  
    cnt += 1