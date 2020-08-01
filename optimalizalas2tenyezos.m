NUM_BASE_CLASSES = 20;
NUM_LANG_CLASSES = 20;
NUM_FACT_CLASSES = 20;
NUM_CLASSES = 60;
global NUM_ROOMS;
NUM_ROOMS = 30;
headcounts = [31, 37, 43, 43, 34, 33, 39, 40, 36, 33, 45, 31, 31, 32, 32, 39, 39, 30, 44, 41, 38, 38, 38, 37, 37, 37, 36, 36, 36, 36, 35, 34, 34, 34, 34, 39, 39, 39, 38, 38, 18, 17, 17, 17, 17, 17, 17, 17, 17, 17, 20, 20, 20, 19, 19, 19, 19, 19, 19, 19]; 
capacities = [41, 31, 43, 44, 45, 43, 42, 38, 32, 36, 32, 30, 45, 34, 34, 35, 37, 40, 30, 43, 38, 43, 35, 37, 30, 32, 40, 35, 44, 31];
%elk�sz�tj�k a p�ros�t�sm�trixot �s a kihaszn�latlans�g-m�trixot
global pairings;
pairings = [];
global idles;
idles = [];
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
