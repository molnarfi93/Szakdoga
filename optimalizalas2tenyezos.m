%25 �s 40 k�zt gener�lt v�letlensz�mok lesznek az oszt�lyok l�tsz�mai, 
%a termek eset�ben pedig 30 �s 45 k�z�tt gener�lunk%
letszamok=randi([25 40],1,20); 
kapacitasok=randi([30 45],1,50);
%kisz�m�tjuk az �vfolyamok �sszes�tett l�tsz�m�t%
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
%ezeket felhaszn�lva kijel�lj�k a nyelvi, illetve fakult�ci�s csoportok
%l�tsz�m�t, �vfolyamonk�nt%
for i=21:60
    if (i<=25) letszamok(i)=round(sum1/5);
    elseif (i>25 && i<=30) letszamok(i)=round(sum2/5);
    elseif (i>30 && i<=35) letszamok(i)=round(sum3/5);
    elseif (i>35 && i<=40) letszamok(i)=round(sum4/5);
    elseif (i>40 && i<=50) letszamok(i)=round(sum3/10);
    else letszamok(i)=round(sum4/10);
    end
end
disp('Oszt�lyl�tsz�mok: ');
disp(letszamok);
disp('Teremkapacit�sok: ');
disp(kapacitasok);
parositasok=[];
kihasznalatlansag=[];
%elk�sz�tj�k a p�ros�t�sm�trixot �s a kihaszn�latlans�g-m�trixot%
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
%7 k�l�nb�z? hozz�rendel�sm�trixot is kapni fogunk, amelyek mind egy-egy
%optim�lis megold�st jelentenek%
megoldasok=[];
megoldasok2=[];
megoldasok3=[];
megoldasok4=[];
megoldasok5=[];
megoldasok6=[];
megoldasok7=[];
foglaltak=[];
%az els? hozz�rendel�s-m�trix alapesettel dolgozik, vagyis azzal az
%esettel, amikor nyelvi �r�k �s faktok sincsenek%
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
%a k�vetkez? hozz�rendel�s-m�trixban kicser�lj�k a 9. �vfolyam oszt�lyait
%(1.-5. sorsz�m) a 9. �vfolyamos nyelvi csoportokra (21.-25. sorsz�m)%
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
%kicser�lj�k a 10. �vfolyam oszt�lyait a 10. �vfolyamos nyelvi csoportokra%
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
%kicser�lj�k a 11. �vfolyam oszt�lyait a 11. �vfolyamos nyelvi csoportokra%
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
%kicser�lj�k a 12. �vfolyam oszt�lyait a 12. �vfolyamos nyelvi csoportokra%
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
%kicser�lj�k a 11. �vfolyam oszt�lyait a 11. �vfolyamos fakt csoportokra%
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
%kicser�lj�k a 12. �vfolyam oszt�lyait a 12. �vfolyamos fakt csoportokra%
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
disp('Megold�sok: ');
disp(megoldasok);
disp('Megold�sok a 9. �vfolyam nyelvi �r�inak idej�ben: ');
disp(megoldasok2);
disp('Megold�sok a 10. �vfolyam nyelvi �r�inak idej�ben: ');
disp(megoldasok3);
disp('Megold�sok a 11. �vfolyam nyelvi �r�inak idej�ben: ');
disp(megoldasok4);
disp('Megold�sok a 12. �vfolyam nyelvi �r�inak idej�ben: ');
disp(megoldasok5);
disp('Megold�sok a 11. �vfolyam fakult�ci�s �r�inak idej�ben: ');
disp(megoldasok6);
disp('Megold�sok a 12. �vfolyam fakult�ci�s �r�inak idej�ben: ');
disp(megoldasok7);