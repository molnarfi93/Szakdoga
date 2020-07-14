letszamok=randi([25 40],1,30);
kapacitasok=randi([30 45],1,50);
disp('Osztálylétszámok: ');
for i=1:30
    disp(letszamok(i));
end
disp('Teremkapacitások: ');
for i=1:50
    disp(kapacitasok(i));
end
parositasok=[];
kihasznalatlansag=[];
for i=1:30
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
disp('Párosításmátrix');
disp(parositasok);
foglaltak=[];
megoldasok=[];
for i=1:30
    min=21;
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
disp(megoldasok);


