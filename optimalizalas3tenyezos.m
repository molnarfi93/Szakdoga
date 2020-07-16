osztalyok={};
tanarok={};
%�vfolyamonk�nt 5 oszt�ly van, illetve a 9. �s 10. �vfolyam eset�ben 10 tant�rgy a nyelvi t�rgyakat nem sz�m�tva (2*5*10=100)%
for i=1:100
    if (i<=10) osztalyok{i,1}="9.A";
    elseif (i>10 && i<=20) osztalyok{i,1}="9.B";
    elseif (i>20 && i<=30) osztalyok{i,1}="9.C";
    elseif (i>30 && i<=40) osztalyok{i,1}="9.D";
    elseif (i>40 && i<=50) osztalyok{i,1}="9.E";
    elseif (i>50 && i<=60) osztalyok{i,1}="10.A";
    elseif (i>60 && i<=70) osztalyok{i,1}="10.B";
    elseif (i>70 && i<=80) osztalyok{i,1}="10.C";
    elseif (i>80 && i<=90) osztalyok{i,1}="10.D";
    elseif (i>90) osztalyok{i,1}="10.E";
    end
end
%a 11. �s 12. �vfolyam eset�ben 8 tant�rgy van, a nyelvi �r�kat �s a fakult�ci�kat nem sz�m�tva%
for i=101:180
    if (i<=108) osztalyok{i,1}="11.A";
    elseif (i>108 && i<=116) osztalyok{i,1}="11.B";
    elseif (i>116 && i<=124) osztalyok{i,1}="11.C";
    elseif (i>124 && i<=132) osztalyok{i,1}="11.D";
    elseif (i>132 && i<=140) osztalyok{i,1}="11.E";
    elseif (i>140 && i<=148) osztalyok{i,1}="12.A";
    elseif (i>148 && i<=156) osztalyok{i,1}="12.B";
    elseif (i>156 && i<=164) osztalyok{i,1}="12.C";
    elseif (i>164 && i<=172) osztalyok{i,1}="12.D";
    elseif (i>172) osztalyok{i,1}="12.E";
    end
end %egy oszt�ly-tant�rgy kett?s �sszetartozva alkot egy entit�st, itt a 9. �s 10. �vfolyamon megy�nk v�gig%   
for i=1:100
    if (mod(i,10)==1) osztalyok{i,2}="matek";
    elseif (mod(i,10)==2) osztalyok{i,2}="informatika";
    elseif (mod(i,10)==3) osztalyok{i,2}="fizika";
    elseif (mod(i,10)==4) osztalyok{i,2}="k�mia";
    elseif (mod(i,10)==5) osztalyok{i,2}="t�rt�nelem";
    elseif (mod(i,10)==6) osztalyok{i,2}="magyar";
    elseif (mod(i,10)==7) osztalyok{i,2}="f�ldrajz";
    elseif (mod(i,10)==8) osztalyok{i,2}="biol�gia";
    elseif (mod(i,10)==9) osztalyok{i,2}="testnevel�s";
    elseif (mod(i,10)==0) osztalyok{i,2}="zene";
    end
end
%itt pedig a 11. �s 12. �vfolyamon, itt m�r nincs fizika �s k�mia, zene helyett pedig rajz van%
for i=101:180
    if (mod(i-100,8)==1) osztalyok{i,2}="matek";
    elseif (mod(i-100,8)==2) osztalyok{i,2}="informatika";
    elseif (mod(i-100,8)==3) osztalyok{i,2}="t�rt�nelem";
    elseif (mod(i-100,8)==4) osztalyok{i,2}="magyar";
    elseif (mod(i-100,8)==5) osztalyok{i,2}="f�ldrajz";
    elseif (mod(i-100,8)==6) osztalyok{i,2}="biol�gia";
    elseif (mod(i-100,8)==7) osztalyok{i,2}="testnevel�s";
    elseif (mod(i-100,8)==0) osztalyok{i,2}="rajz";
    end
end
%j�nnek a nyelvi csoportok, �vfolyamonk�nt 3 angol, 1 n�met �s 1 spanyol%
osztalyok{181,1}="angol1gyenge";
osztalyok{182,1}="angol1k�zepes";
osztalyok{183,1}="angol1er�s";
osztalyok{184,1}="n�met1";
osztalyok{185,1}="spanyol1";
osztalyok{186,1}="angol2gyenge";
osztalyok{187,1}="angol2k�zepes";
osztalyok{188,1}="angol2er�s";
osztalyok{189,1}="n�met2";
osztalyok{190,1}="spanyol2";
osztalyok{191,1}="angol3gyenge";
osztalyok{192,1}="angol3k�zepes";
osztalyok{193,1}="angol3er�s";
osztalyok{194,1}="n�met3";
osztalyok{195,1}="spanyol3";
osztalyok{196,1}="angol4gyenge";
osztalyok{197,1}="angol4k�zepes";
osztalyok{198,1}="angol4er�s";
osztalyok{199,1}="n�met4";
osztalyok{200,1}="spanyol4";
for i=181:200
    if (i==184 || i==189 || i==194 || i==199) osztalyok{i,2}="n�met";
    elseif (i==185 || i==190 || i==195 || i==200) osztalyok{i,2}="spanyol";
    else osztalyok{i,2}="angol";
    end
end
%meghat�rozzuk a heti �rasz�mokat a k�l�nb�z? tant�rgyak kapcs�n%
for i=1:200 
    if (osztalyok{i,2}=="matek" || osztalyok{i,2}=="magyar" || osztalyok{i,2}=="angol" || osztalyok{i,2}=="n�met" || osztalyok{i,2}=="spanyol") osztalyok{i,3}=4;
    elseif (osztalyok{i,2}=="informatika" || osztalyok{i,2}=="t�rt�nelem" || osztalyok{i,2}=="testnevel�s") osztalyok{i,3}=3;
    elseif (osztalyok{i,2}=="f�ldrajz" || osztalyok{i,2}=="biol�gia" || osztalyok{i,2}=="fizika" || osztalyok{i,2}=="k�mia" || osztalyok{i,2}=="rajz") osztalyok{i,3}=2;
    else osztalyok{i,3}=1;
    end
end
%v�g�l j�nnek a fakult�ci�s csoportok, a heti �rasz�m egys�gesen 2%
osztalyok{201,1}="matekfakt3";
osztalyok{202,1}="inf�fakt3";
osztalyok{203,1}="fizikafakt3";
osztalyok{204,1}="k�miafakt3";
osztalyok{205,1}="t�rifakt3";
osztalyok{206,1}="magyarfakt3";
osztalyok{207,1}="f�ldrajzfakt3";
osztalyok{208,1}="bioszfakt3";
osztalyok{209,1}="tesifakt3";
osztalyok{210,1}="zenefakt3";
osztalyok{211,1}="matekfakt4";
osztalyok{212,1}="inf�fakt4";
osztalyok{213,1}="fizikafakt4";
osztalyok{214,1}="k�miafakt4";
osztalyok{215,1}="t�rifakt4";
osztalyok{216,1}="magyarfakt4";
osztalyok{217,1}="f�ldrajzfakt4";
osztalyok{218,1}="bioszfakt4";
osztalyok{219,1}="tesifakt4";
osztalyok{220,1}="zenefakt4";
for i=201:220
    if (i==201 || i==211) osztalyok{i,2}="matek";
    elseif (i==202 || i==212) osztalyok{i,2}="informatika";
    elseif (i==203 || i==213) osztalyok{i,2}="fizika";
    elseif (i==204 || i==214) osztalyok{i,2}="k�mia";
    elseif (i==205 || i==215) osztalyok{i,2}="t�rt�nelem";
    elseif (i==206 || i==216) osztalyok{i,2}="magyar";
    elseif (i==207 || i==217) osztalyok{i,2}="f�ldrajz";
    elseif (i==208 || i==218) osztalyok{i,2}="biol�gia";
    elseif (i==209 || i==219) osztalyok{i,2}="testnevel�s";
    else osztalyok{i,2}="zene";
    end
end
for i=201:220
    osztalyok{i,3}=2;
end
for i=1:220
    fprintf('%s %s %g\n', osztalyok{i,1}, osztalyok{i,2}, osztalyok{i,3});
end
%a tan�rok sorsz�mot kapnak 1-30-ig%
for i=1:30
    tanarok{i,1}=i;
end
%be�ll�tunk minden tan�rhoz k�t tant�rgyat, amelyet tud tan�tani%
for i=1:8
    tanarok{i,2}="matek";
    if (i<=3) tanarok{i,3}="fizika";
    elseif (i>3 && i<=6) tanarok{i,3}="informatika";
    else tanarok{i,3}="k�mia";
    end    
end
for i=9:17
    tanarok{i,2}="t�rt�nelem";
    if (i<=12) tanarok{i,3}="f�ldrajz";
    elseif (i>12 && i<=15) tanarok{i,3}="magyar";
    else tanarok{i,3}="angol";
    end
end
for i=18:20
    tanarok{i,2}="magyar";
    tanarok{i,3}="angol";
end
i=21;
tanarok{i,2}="magyar";
tanarok{i,3}="n�met";
i=22;
tanarok{i,2}="biol�gia";
tanarok{i,3}="angol";
for i=23:24
    tanarok{i,2}="biol�gia";
    tanarok{i,3}="rajz";
end
for i=25:26
    tanarok{i,2}="zene";
    tanarok{i,3}="spanyol";
end
%a tesitan�rok r�szmunkaid?s�k, ez�rt ?k nem tan�tanak m�st%
for i=27:30
    tanarok{i,2}="testnevel�s";
    tanarok{i,3}="nincs";
end
%0-val inicializ�ljuk az egyes tan�rok heti �rasz�m�t% 
for i=1:30
    tanarok{i,4}=0;
end
for i=1:30
    fprintf('%g %s %s\n', tanarok{i,1}, tanarok{i,2}, tanarok{i,3});
end
parositasok=[];
%az oszt�ly-tant�rgy entit�sok 2. oszlopa �s a tan�r entit�sok 2. �s 3.
%oszlopa tartalmazza a t�rgyneveket, ezekre v�gz�nk �sszehasonl�t�st, ha
%egyez?s�g van, akkor az adott tan�r tan�thatja az adott tant�rgyat az
%adott oszt�lynak, de hogy fogja-e az k�s?bb der�l ki%
for i=1:220
    for j=1:30
        if (osztalyok{i,2}==tanarok{j,2} || osztalyok{i,2}==tanarok{j,3}) parositasok{i,j}=1;
        else parositasok{i,j}=0;
        end
    end
end
megoldasok={};
%ebben a ciklusban m�r hozz�rendel�nk%
for i=1:220
    for j=1:30
        boole=0;
        if (parositasok{i,j}==1)
            %j�n m�g egy be�gyazott ciklus annak �rdek�ben, hogy ha van
            %m�sik olyan tan�r is, aki tudja tan�tani az adott t�rgyat �s a
            %heti �rasz�m�nak aktu�lis �rt�ke kisebb, akkor ? r� essen a
            %v�laszt�s az egyenl?tlen terhel�s elker�l�se v�gett%
            for k=j:30
                if (tanarok{k,4}<tanarok{j,4} && parositasok{i,k}==1) boole=1;
                end
            end
            if (boole==0)
            megoldasok{i,1}=osztalyok{i,1};
            megoldasok{i,2}=osztalyok{i,2};
            megoldasok{i,3}=tanarok{j,1};
            tanarok{j,4}=tanarok{j,4}+osztalyok{i,3};
            megoldasok{i,4}=tanarok{j,4};
            break;
            end
        end
    end
end
for i=1:length(megoldasok)
    fprintf('%s %s %g %g\n', megoldasok{i,1}, megoldasok{i,2}, megoldasok{i,3}, megoldasok{i,4});
end
