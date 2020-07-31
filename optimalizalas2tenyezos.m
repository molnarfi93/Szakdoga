NUM_BASE_CLASSES = 20;
NUM_LANG_CLASSES = 20;
NUM_FACT_CLASSES = 20;
NUM_CLASSES = 60;
global NUM_ROOMS;
NUM_ROOMS = 30;
%30 �s 45 k�zt gener�lt v�letlensz�mok lesznek az oszt�lyok l�tsz�mai, 
%illetve a tantermek kapacit�sai
headcounts = randi([30 45], 1, NUM_BASE_CLASSES); 
capacities = randi([30 45], 1, NUM_ROOMS);
%kisz�m�tjuk az �vfolyamok �sszes�tett l�tsz�m�t
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
%ezeket felhaszn�lva kijel�lj�k a nyelvi, illetve fakult�ci�s csoportok
%l�tsz�m�t, �vfolyamonk�nt
for i = (NUM_BASE_CLASSES) + 1 : NUM_CLASSES
    if (i <= 25) headcounts(i) = round(headcount_grade1/5);
    elseif (i > 25 && i <= 30) headcounts(i) = round(headcount_grade2/5);
    elseif (i > 30 && i <= 35) headcounts(i) = round(headcount_grade3/5);
    elseif (i > 35 && i <= 40) headcounts(i) = round(headcount_grade4/5);
    elseif (i > 40 && i <= 50) headcounts(i) = round(headcount_grade3/10);
    else headcounts(i) = round(headcount_grade4/10);
    end
end
disp('Oszt�lyl�tsz�mok: ');
disp(headcounts);
disp('Teremkapacit�sok: ');
disp(capacities);
global pairings;
pairings=[];
global idles;
idles=[];
%elk�sz�tj�k a p�ros�t�sm�trixot �s a kihaszn�latlans�g-m�trixot
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
%az els� hozz�rendel�s-m�trix alapesettel dolgozik, vagyis azzal az
%esettel, amikor nyelvi �r�k �s faktok sincsenek
result=assignments(1, 20, 20, 20, 20, 20);
disp('Megold�s: ');
disp(result);
%a k�vetkez� hozz�rendel�s-m�trixban kicser�lj�k a 9. �vfolyam oszt�lyait
%(1.-5. sorsz�m) a 9. �vfolyamos nyelvi csoportokra (21.-25. sorsz�m)
result=assignments(6, 25, 25, 25, 25, 25);
disp('Megold�s a 9. �vfolyam nyelvi �r�inak idej�ben: ');
disp(result);
%kicser�lj�k a 10. �vfolyam oszt�lyait a 10. �vfolyamos nyelvi csoportokra
result=assignments(1, 5, 11, 20, 26, 30);
disp('Megold�s a 10. �vfolyam nyelvi �r�inak idej�ben: ');
disp(result);
%kicser�lj�k a 11. �vfolyam oszt�lyait a 11. �vfolyamos nyelvi csoportokra
result=assignments(1, 10, 16, 20, 31, 35);
disp('Megold�s a 11. �vfolyam nyelvi �r�inak idej�ben: ');
disp(result);
%kicser�lj�k a 12. �vfolyam oszt�lyait a 12. �vfolyamos nyelvi csoportokra
result=assignments(1, 15, 36, 40, 40, 40);
disp('Megold�s a 12. �vfolyam nyelvi �r�inak idej�ben: ');
disp(result);
%kicser�lj�k a 11. �vfolyam oszt�lyait a 11. �vfolyamos fakt csoportokra
result=assignments(1, 10, 16, 20, 41, 50);
disp('Megold�s a 11. �vfolyam fakult�ci�s �r�inak idej�ben: ');
disp(result);
%kicser�lj�k a 12. �vfolyam oszt�lyait a 12. �vfolyamos fakt csoportokra
result=assignments(1, 15, 51, 60, 60, 60);
disp('Megold�s a 12. �vfolyam fakult�ci�s �r�inak idej�ben: ');
disp(result);
%itt a f�ggv�ny, amelyet 7 alkalommal megh�vtunk, elt�r� param�terez�ssel
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
