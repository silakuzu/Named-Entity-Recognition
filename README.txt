CS445 HW1
*********


PERSON
**The website I took the names from:
https://kerteriz.net/tum-turkce-erkek-ve-kadin-isimleri-cinsiyet-listesi-veritabani/
->At the beginning, the format was like ('Ayşe', 'K')
I removed all the unnecessary characters like (,' 'K') and left with only names line by line
replaced ('      ', 'K')      ', 'E')      ', 'U') with empty ch.

**I took surnames from a github account and pasted them to a txt file:
https://gist.github.com/emrekgn/493304c6445de15657b2

https://www.gercekbilim.com/gecmisten-gunumuze-dunya-yi-sekillendiren-100-buyuk-bilim-adami/

https://ingilizcebankasi.com/ingilizce-kiz-isimleri/






LOCATION
**il ve ilçeler:
https://www.harita.gov.tr/images/urun/il_ilce_alanlari.pdf
->replaced İL / İLÇE ALAN (km²) with empty character and removed all lines
---in order to remove empty lines: replaced [\r\n]+ to \n----NOT USED
->to remove lines like 9 / 14, replaced \w\s/\s\w* with empty ch.
for the last line, I removed the number with hand.
in order to remove empty lines, I used edit->Line operations->remove empty lines
while converting from uppercase to lowercase, 
first replaced I with ı (in order not to lose Is to i)
İ's have not been converted--> replaced all İ with i, the replaced ı's with I/İ if it is at the beginning (\nı/i to \nI/İ)
replaced "_MERKEZ" with " MERKEZ"


World cities, countries and administration names:
https://simplemaps.com/data/world-cities
Removed words after "CUMHURİYET", DEVLETİ and DEVLETİ








ORGANIZATIONS
**universities, yüksekokuls and enstitüs in Turkey(197-many)
https://www.yok.gov.tr/universiteler/universitelerimiz
-> I removed any unnecessary information given in dataset like İNTERNET ADRESİ, E-POSTA, TELEFON, FAKS, ADRES, REKTÖR.
In order to achieve this, I replaced " http.*" and " www.*" with empty ch.. I removed some inconsistent lines with eye.
In some of the lines, ÜNİVERSİTESİ was in the below line. To solve this, I joined all the lines firstly then replaced ÜNİVERSİTESİ. with ÜNİVERSİTESİ\n
I did same operations I did for il & ilçeler to properly convert Is to ı.
 
**Kamu Kurum ve Kuruluşları (54-many)
https://www.tbmm.gov.tr/baglantilar/kamu_kurum_kuruluslar.htm

Foreign companies:
https://en.wikipedia.org/wiki/List_of_company_name_etymologies
replaced " -.*" with " "
replaced \n\w{1}\s with "" in order to remove single characters

https://tr.wikipedia.org/wiki/Gelirlerine_g%C3%B6re_en_b%C3%BCy%C3%BCk_%C5%9Firketler_listesi
replaced Petrol ve doğal gaz.* with empty character
replaced \$.* with empty ch.

https://fortune.com/fortune500/2020/search/
replaced \d with empty ch
[\$,.%-]* with empty ch
replaced \s{5,} with \n

Turkish companies
https://www.fortuneturkey.com/fortune500
replaced "Net Satış" number with \d{1}.*\d{1} to empty line
replaced A.Ş.\s with A.Ş.\n
replaced \d with empty character
replaced A.Ş.\n.*\n\w* with A.Ş
replaced A.Ş.\s\n.* with A.Ş to remove the line below A.Ş.
LTD.\s\n.* with empty ch
ŞTİ.\s\n.* with empty ch
LTD.\s\s\n.* with empty ch.
replaced İSTANBUL, ANKARA with empty ch.
replace all I with ı
replaced \si/ı with " I/İ"

-->replaced Sanayi Ve Ticaret A.Ş. with empty ch.

->in addition, 
removed Sanayi Ve Ticaret A.Ş.

banks:
https://tr.wikipedia.org/wiki/T%C3%BCrkiye%27deki_bankalar_listesi

vakıflar:
http://www.turkcewiki.org/wiki/T%C3%BCrkiye%27deki_vak%C4%B1flar_listesi


After retrieving data from NER_example_data,
replace all I with ı
In notepad++:
convert case to proper case
order them as ascending
remove duplicate line
Then, replaced \si/ı with " I/İ"
replaced \sı with " I"
To remove single letters in one line, replaced \n\w{1}\s\W with empty ch.



