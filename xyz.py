from datetime import datetime
from datetime import timedelta


def find_date(date_as_string):
    datetime_object = datetime.strptime(date_as_string, '%a %b %d %H:%M:%S %Y')  # trzyma mi date w formacie  pythonowym
    return datetime_object

def zczytaj_wiersze_z_nazwami_kolumn(file): #FIXME zmienia wartość file poza scope funkcji
    columns_names_unprocessed = []
    ## read lines for columns
    for line in file:
        result = line.find(';<<<< 26 Data columns')
        if result == -1:
            columns_names_unprocessed.append(line)
        elif result >= 0:
            break

    return columns_names_unprocessed

def wczytaj_komurki_dla_kolumn(file,tablica_nazw_kolumn):
    komurki = [[] for _ in range(len(tablica_nazw_kolumn))]# robie tablice od tablicy n nazwy kolumn
    print(komurki)
    surowa_linia =file.readline()
    print(str(surowa_linia))

    print(str(surowa_linia))
    linie_w_tablicy = []
    for i in file:
        surowa_linia = i
        linie_w_tablicy.append(surowa_linia.split())
    return linie_w_tablicy

with open(r'E:\Studia\pc_projekty\xyz\xyz.txt', "r+") as file:
    tab = zczytaj_wiersze_z_nazwami_kolumn(file)
    print("xyz")
    print(tab)
    print(tab[0].split(";>>>>>> Start scan at ")[1])
    datetime_object = find_date(tab[0].split(";>>>>>> Start scan at ")[
                                    1].rstrip())  # biore zerowy  element w ktorym jest data  nastepnie pozbywam sie start scan i dziele tablice po tym i biore pierwszy element w praktyce chce sie tego pozbyc
    print(str(datetime_object))

    # new_date_format=datetime_object.strftime("%Y-%m-%d %H:%M:%S.000 %H:%M:%S")
    tab = [i.split() for i in tab]
    # print(new_date_format)

    tab = tab[2:]
    print(tab)
    columns_names = [i[4] for i in tab]
    columns_names.insert(0,"time\trealtime\tProgram\t")

    print(columns_names)
    komurki = wczytaj_komurki_dla_kolumn(file,columns_names)





## zapis nowego pliku
with open(r'E:\Studia\pc_projekty\xyz\plik2.txt','w+') as  nowy_plik:
    nowy_plik.write("\t".join(columns_names))
    nowy_plik.write("\n")
    for i, v in enumerate(komurki):
        nowy_plik.write((datetime_object + timedelta(seconds=i)).strftime("%Y-%m-%d %H:%M:%S.000 %H:%M:%S\t"))
        nowy_plik.write("\t".join(v))
        nowy_plik.write("\n")
 
