NUM_BASE_CLASSES = 20;
NUM_LANG_CLASSES = 20;
NUM_FACT_CLASSES = 20;
NUM_CLASSES = 60;
global NUM_ROOMS;
NUM_ROOMS = 30;
%30 és 45 közt generált véletlenszámok lesznek az osztályok létszámai, 
%illetve a tantermek kapacitásai
headcounts = randi([30 45], 1, NUM_BASE_CLASSES); 
capacities = randi([30 45], 1, NUM_ROOMS);
%kiszámítjuk az évfolyamok összesített létszámát
headcount_grade1 = 0;
headcount_grade2 = 0;
headcount_grade3 = 0;
headcount_grade4 = 0;
for i = 1 : NUM_BASE_CLASSES
    if (i <= 5) headcount_grade1=headcount_grade1+headcounts(i);
    elseif (i > 5 && i <= 10) headcount_grade2=headcount_grade2+headcounts(i);
    elseif (i > 10 && i <= 15) headcount_grade3=headcount_grade3+headcounts(i);
    else headcount_grade4=headcount_grade4+headcounts(i);
    end
end
%ezeket felhasználva kijelöljük a nyelvi, illetve fakultációs csoportok
%létszámát, évfolyamonként
for i = (NUM_BASE_CLASSES) + 1 : NUM_CLASSES
    if (i <= 25) headcounts(i) = round(headcount_grade1/5);
    elseif (i > 25 && i <= 30) headcounts(i) = round(headcount_grade2/5);
    elseif (i > 30 && i <= 35) headcounts(i) = round(headcount_grade3/5);
    elseif (i > 35 && i <= 40) headcounts(i) = round(headcount_grade4/5);
    elseif (i > 40 && i <= 50) headcounts(i) = round(headcount_grade3/10);
    else headcounts(i) = round(headcount_grade4/10);
    end
end
disp('Osztálylétszámok: ');
disp(headcounts);
disp('Teremkapacitások: ');
disp(capacities);
global pairings;
pairings=[];
global idles;
idles=[];
%elkészítjük a párosításmátrixot és a kihasználatlanság-mátrixot
for i = 1 : NUM_CLASSES
    for j = 1 : NUM_ROOMS
        if (headcounts(i) <= capacities(j)) 
            pairings(i,j) = 1;
            idles(i,j) = capacities(j) - headcounts(i);
        else
            pairings(i,j) = 0;
            idles(i,j) = NaN;
        end
    end
end
%az elsö hozzárendelés-mátrix alapesettel dolgozik, vagyis azzal az
%esettel, amikor nyelvi órák és faktok sincsenek
result=assignments(1, 20, 20, 20, 20, 20);
disp('Megoldás: ');
disp(result);
%a következö hozzárendelés-mátrixban kicseréljük a 9. évfolyam osztályait
%(1.-5. sorszám) a 9. évfolyamos nyelvi csoportokra (21.-25. sorszám)
result=assignments(6, 25, 25, 25, 25, 25);
disp('Megoldás a 9. évfolyam nyelvi óráinak idejében: ');
disp(result);
%kicseréljük a 10. évfolyam osztályait a 10. évfolyamos nyelvi csoportokra
result=assignments(1, 5, 11, 20, 26, 30);
disp('Megoldás a 10. évfolyam nyelvi óráinak idejében: ');
disp(result);
%kicseréljük a 11. évfolyam osztályait a 11. évfolyamos nyelvi csoportokra
result=assignments(1, 10, 16, 20, 31, 35);
disp('Megoldás a 11. évfolyam nyelvi óráinak idejében: ');
disp(result);
%kicseréljük a 12. évfolyam osztályait a 12. évfolyamos nyelvi csoportokra
result=assignments(1, 15, 36, 40, 40, 40);
disp('Megoldás a 12. évfolyam nyelvi óráinak idejében: ');
disp(result);
%kicseréljük a 11. évfolyam osztályait a 11. évfolyamos fakt csoportokra
result=assignments(1, 10, 16, 20, 41, 50);
disp('Megoldás a 11. évfolyam fakultációs óráinak idejében: ');
disp(result);
%kicseréljük a 12. évfolyam osztályait a 12. évfolyamos fakt csoportokra
result=assignments(1, 15, 51, 60, 60, 60);
disp('Megoldás a 12. évfolyam fakultációs óráinak idejében: ');
disp(result);
%itt a függvény, amelyet 7 alkalommal meghívtunk, eltérö paraméterezéssel
function result = assignments(i11, i12, i21, i22, i31, i32)
    global NUM_ROOMS;
    global pairings;
    global idles;
    result = [];
    seated_rooms = [];
    for i = [i11 : i12 , i21 : i22 , i31 : i32]
        min = 30;
        minindex = NaN;
        for j = 1 : NUM_ROOMS
            boole = 0;
            if (pairings(i,j) == 1 && idles(i,j) < min)
                for k = 1 : length(seated_rooms)
                    if (seated_rooms(k) == j)
                        boole = 1;
                        break;
                    end
                end    
                if (boole == 0)
                    min = idles(i,j);
                    minindex = j;
                    result(i,1) = i;
                    result(i,2) = j;
                end
            end
            if (j == 30) 
                seated_rooms(i) = minindex;
            end
        end
    end
end
