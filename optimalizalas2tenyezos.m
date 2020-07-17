%25 és 40 közt generált véletlenszámok lesznek az osztályok létszámai, 
%a termek esetében pedig 30 és 45 között generálunk%
letszamok=randi([25 40],1,20); 
kapacitasok=randi([30 45],1,50);
%kiszámítjuk az évfolyamok összesített létszámát%
sum1=0;
sum2=0;
sum3=0;
sum4=0;
for i=1:20
    if (i<=5) sum1=sum1+letszamok(i);
    elseif (i>5 && i<=10) sum2=sum2+letszamok(i);
    elseif (i>10 && i<=15) sum3=sum3+letszamok(i);
    else sum4=sum4+letszamok(i);
    end
end
%ezeket felhasználva kijelöljük a nyelvi, illetve fakultációs csoportok
%látszámát, évfolyamonként%
for i=21:60
    if (i<=25) letszamok(i)=round(sum1/5);
    elseif (i>25 && i<=30) letszamok(i)=round(sum2/5);
    elseif (i>30 && i<=35) letszamok(i)=round(sum3/5);
    elseif (i>35 && i<=40) letszamok(i)=round(sum4/5);
    elseif (i>40 && i<=50) letszamok(i)=round(sum3/10);
    else letszamok(i)=round(sum4/10);
    end
end
disp('Osztálylétszámok: ');
disp(letszamok);
disp('Teremkapacitások: ');
disp(kapacitasok);
parositasok=[];
kihasznalatlansag=[];
%elkészítjük a párosításmátrixot és a kihasználatlanság-mátrixot%
for i=1:60
    for j=1:50
        if (letszamok(i)<=kapacitasok(j)) 
            parositasok(i,j)=1;
            kihasznalatlansag(i,j)=kapacitasok(j)-letszamok(i);
        else
            parositasok(i,j)=0;
            kihasznalatlansag(i,j)=NaN;
        end
    end
end
%7 különböz? hozzárendelésmátrixot is kapni fogunk, amelyek mind egy-egy
%optimális megoldást jelentenek%
megoldasok=[];
megoldasok2=[];
megoldasok3=[];
megoldasok4=[];
megoldasok5=[];
megoldasok6=[];
megoldasok7=[];
foglaltak=[];
%az els? hozzárendelés-mátrix alapesettel dolgozik, vagyis azzal az
%esettel, amikor nyelvi órák és faktok sincsenek%
for i=1:20
    min=40;
    for j=1:50
        boole=0;
        if (parositasok(i,j)==1 && kihasznalatlansag(i,j)<min)
            for k=1:length(foglaltak)
                if (foglaltak(k)==j)
                    boole=1;
                    break;
                end
            end    
            if (boole==0)
                min=kihasznalatlansag(i,j);
                minindex=j;
                megoldasok(i,1)=i;
                megoldasok(i,2)=j;
            end
        end
        if (j==50) foglaltak(i)=minindex;
        end
    end
end
for i=1:length(foglaltak)
    foglaltak(i)=NaN;
end
%a következ? hozzárendelés-mátrixban kicseréljük a 9. évfolyam osztályait
%(1.-5. sorszám) a 9. évfolyamos nyelvi csoportokra (21.-25. sorszám)%
for i=6:25
    min=40;
    for j=1:50
        boole=0;
        if (parositasok(i,j)==1 && kihasznalatlansag(i,j)<min)
            for k=1:length(foglaltak)
                if (foglaltak(k)==j)
                    boole=1;
                    break;
                end
            end    
            if (boole==0)
                min=kihasznalatlansag(i,j);
                minindex=j;
                megoldasok2(i,1)=i;
                megoldasok2(i,2)=j;
            end
        end
        if (j==50) foglaltak(i)=minindex;
        end
    end
end
for i=1:length(foglaltak)
    foglaltak(i)=NaN;
end
%kicseréljük a 10. évfolyam osztályait a 10. évfolyamos nyelvi csoportokra%
for i=[1:5,11:20,26:30]
    min=40;
    for j=1:50
        boole=0;
        if (parositasok(i,j)==1 && kihasznalatlansag(i,j)<min)
            for k=1:length(foglaltak)
                if (foglaltak(k)==j)
                    boole=1;
                    break;
                end
            end    
            if (boole==0)
                min=kihasznalatlansag(i,j);
                minindex=j;
                megoldasok3(i,1)=i;
                megoldasok3(i,2)=j;
            end
        end
        if (j==50) foglaltak(i)=minindex;
        end
    end
end
for i=1:length(foglaltak)
    foglaltak(i)=NaN;
end
%kicseréljük a 11. évfolyam osztályait a 11. évfolyamos nyelvi csoportokra%
for i=[1:10,16:20,31:35]
    min=40;
    for j=1:50
        boole=0;
        if (parositasok(i,j)==1 && kihasznalatlansag(i,j)<min)
            for k=1:length(foglaltak)
                if (foglaltak(k)==j)
                    boole=1;
                    break;
                end
            end    
            if (boole==0)
                min=kihasznalatlansag(i,j);
                minindex=j;
                megoldasok4(i,1)=i;
                megoldasok4(i,2)=j;
            end
        end
        if (j==50) foglaltak(i)=minindex;
        end
    end
end
for i=1:length(foglaltak)
    foglaltak(i)=NaN;
end
%kicseréljük a 12. évfolyam osztályait a 12. évfolyamos nyelvi csoportokra%
for i=[1:15,36:40]
    min=40;
    for j=1:50
        boole=0;
        if (parositasok(i,j)==1 && kihasznalatlansag(i,j)<min)
            for k=1:length(foglaltak)
                if (foglaltak(k)==j)
                    boole=1;
                    break;
                end
            end    
            if (boole==0)
                min=kihasznalatlansag(i,j);
                minindex=j;
                megoldasok5(i,1)=i;
                megoldasok5(i,2)=j;
            end
        end
        if (j==50) foglaltak(i)=minindex;
        end
    end
end
for i=1:length(foglaltak)
    foglaltak(i)=NaN;
end
%kicseréljük a 11. évfolyam osztályait a 11. évfolyamos fakt csoportokra%
for i=[1:10,16:20,41:50]
    min=40;
    for j=1:50
        boole=0;
        if (parositasok(i,j)==1 && kihasznalatlansag(i,j)<min)
            for k=1:length(foglaltak)
                if (foglaltak(k)==j)
                    boole=1;
                    break;
                end
            end    
            if (boole==0)
                min=kihasznalatlansag(i,j);
                minindex=j;
                megoldasok6(i,1)=i;
                megoldasok6(i,2)=j;
            end
        end
        if (j==50) foglaltak(i)=minindex;
        end
    end
end
for i=1:length(foglaltak)
    foglaltak(i)=NaN;
end
%kicseréljük a 12. évfolyam osztályait a 12. évfolyamos fakt csoportokra%
for i=[1:15,51:60]
    min=40;
    for j=1:50
        boole=0;
        if (parositasok(i,j)==1 && kihasznalatlansag(i,j)<min)
            for k=1:length(foglaltak)
                if (foglaltak(k)==j)
                    boole=1;
                    break;
                end
            end    
            if (boole==0)
                min=kihasznalatlansag(i,j);
                minindex=j;
                megoldasok7(i,1)=i;
                megoldasok7(i,2)=j;
            end
        end
        if (j==50) foglaltak(i)=minindex;
        end
    end
end
disp('Megoldások: ');
disp(megoldasok);
disp('Megoldások a 9. évfolyam nyelvi óráinak idejében: ');
disp(megoldasok2);
disp('Megoldások a 10. évfolyam nyelvi óráinak idejében: ');
disp(megoldasok3);
disp('Megoldások a 11. évfolyam nyelvi óráinak idejében: ');
disp(megoldasok4);
disp('Megoldások a 12. évfolyam nyelvi óráinak idejében: ');
disp(megoldasok5);
disp('Megoldások a 11. évfolyam fakultációs óráinak idejében: ');
disp(megoldasok6);
disp('Megoldások a 12. évfolyam fakultációs óráinak idejében: ');
disp(megoldasok7);