NUM_CLASSES=220;
NUM_BASE_CLASSES_GRADES_1_2=100;
NUM_BASE_CLASSES_GRADES_3_4=80;
NUM_BASE_CLASSES=180;
NUM_LANG_CLASSES=20;
NUM_FACT_CLASSES=20;
NUM_SUBJECTS_GRADES_1_2=10;
NUM_SUBJECTS_GRADES_3_4=8;
NUM_TEACHERS=30;
classes = {};
teachers = {};
%�vfolyamonk�nt 5 oszt�ly van, illetve a 9. �s 10. �vfolyam eset�ben 
%10 tant�rgy a nyelvi t�rgyakat nem sz�m�tva (2*5*10=100)
for i = 1 : NUM_BASE_CLASSES_GRADES_1_2
    if (i <= NUM_SUBJECTS_GRADES_1_2) classes{i,1} = "9.A";
    elseif (i > NUM_SUBJECTS_GRADES_1_2 && i <= (NUM_SUBJECTS_GRADES_1_2) * 2) classes{i,1} = "9.B";
    elseif (i > (NUM_SUBJECTS_GRADES_1_2) * 2 && i <= (NUM_SUBJECTS_GRADES_1_2) * 3) classes{i,1} = "9.C";
    elseif (i > (NUM_SUBJECTS_GRADES_1_2) * 3 && i <= (NUM_SUBJECTS_GRADES_1_2) * 4) classes{i,1} = "9.D";
    elseif (i > (NUM_SUBJECTS_GRADES_1_2) * 4 && i <= (NUM_SUBJECTS_GRADES_1_2) * 5) classes{i,1} = "9.E";
    elseif (i > (NUM_SUBJECTS_GRADES_1_2) * 5 && i <= (NUM_SUBJECTS_GRADES_1_2) * 6) classes{i,1} = "10.A";    
    elseif (i > (NUM_SUBJECTS_GRADES_1_2) * 6 && i <= (NUM_SUBJECTS_GRADES_1_2) * 7) classes{i,1} = "10.B";
    elseif (i > (NUM_SUBJECTS_GRADES_1_2) * 7 && i <= (NUM_SUBJECTS_GRADES_1_2) * 8) classes{i,1} = "10.C";
    elseif (i > (NUM_SUBJECTS_GRADES_1_2) * 8 && i <= (NUM_SUBJECTS_GRADES_1_2) * 9) classes{i,1} = "10.D";
    else classes{i,1} = "10.E";
    end
end
%a 11. �s 12. �vfolyam eset�ben 8 tant�rgy van, a nyelvi �r�kat �s a
%fakult�ci�kat nem sz�m�tva
for i = 1 : NUM_BASE_CLASSES_GRADES_3_4
    if (i <= NUM_SUBJECTS_GRADES_3_4) classes{i + NUM_BASE_CLASSES_GRADES_1_2, 1} = "11.A";
    elseif (i > NUM_SUBJECTS_GRADES_3_4 && i <= (NUM_SUBJECTS_GRADES_3_4)*2) classes{i + NUM_BASE_CLASSES_GRADES_1_2, 1} = "11.B";
    elseif (i > (NUM_SUBJECTS_GRADES_3_4) * 2 && i <= (NUM_SUBJECTS_GRADES_3_4) * 3) classes{i + NUM_BASE_CLASSES_GRADES_1_2, 1} = "11.C";
    elseif (i > (NUM_SUBJECTS_GRADES_3_4) * 3 && i <= (NUM_SUBJECTS_GRADES_3_4) * 4) classes{i + NUM_BASE_CLASSES_GRADES_1_2, 1} = "11.D";
    elseif (i > (NUM_SUBJECTS_GRADES_3_4) * 4 && i <= (NUM_SUBJECTS_GRADES_3_4) * 5) classes{i + NUM_BASE_CLASSES_GRADES_1_2, 1} = "11.E";
    elseif (i > (NUM_SUBJECTS_GRADES_3_4) * 5 && i <= (NUM_SUBJECTS_GRADES_3_4) * 6) classes{i + NUM_BASE_CLASSES_GRADES_1_2, 1} = "12.A";    
    elseif (i > (NUM_SUBJECTS_GRADES_3_4) * 6 && i <= (NUM_SUBJECTS_GRADES_3_4) * 7) classes{i + NUM_BASE_CLASSES_GRADES_1_2, 1} = "12.B";
    elseif (i > (NUM_SUBJECTS_GRADES_3_4) * 7 && i <= (NUM_SUBJECTS_GRADES_3_4) * 8) classes{i + NUM_BASE_CLASSES_GRADES_1_2, 1} = "12.C";
    elseif (i > (NUM_SUBJECTS_GRADES_3_4) * 8 && i <= (NUM_SUBJECTS_GRADES_3_4) * 9) classes{i + NUM_BASE_CLASSES_GRADES_1_2, 1} = "12.D";
    else classes{i + NUM_BASE_CLASSES_GRADES_1_2, 1} = "12.E";
    end
end
%egy oszt�ly-tant�rgy kett�s �sszetartozva alkot egy entit�st, itt a
%9. �s 10. �vfolyamon megy�nk v�gig   
for i = 1 : NUM_BASE_CLASSES_GRADES_1_2
    if (mod(i, NUM_SUBJECTS_GRADES_1_2) == 1) classes{i,2} = "math";
    elseif (mod(i, NUM_SUBJECTS_GRADES_1_2) == 2) classes{i,2} = "informathics";
    elseif (mod(i, NUM_SUBJECTS_GRADES_1_2) == 3) classes{i,2} = "physics";
    elseif (mod(i, NUM_SUBJECTS_GRADES_1_2) == 4) classes{i,2} = "chemistry";
    elseif (mod(i, NUM_SUBJECTS_GRADES_1_2) == 5) classes{i,2} = "history";
    elseif (mod(i, NUM_SUBJECTS_GRADES_1_2) == 6) classes{i,2} = "hungarian";
    elseif (mod(i, NUM_SUBJECTS_GRADES_1_2) == 7) classes{i,2} = "geography";
    elseif (mod(i, NUM_SUBJECTS_GRADES_1_2) == 8) classes{i,2} = "biology";
    elseif (mod(i, NUM_SUBJECTS_GRADES_1_2) == 9) classes{i,2} = "P.E.";
    elseif (mod(i, NUM_SUBJECTS_GRADES_1_2) == 0) classes{i,2} = "music";
    end
end
%itt pedig a 11. �s 12. �vfolyamon, itt m�r nincs fizika �s k�mia, zene 
%helyett pedig rajz van
for i = 1 : NUM_BASE_CLASSES_GRADES_3_4
    if (mod(i, NUM_SUBJECTS_GRADES_3_4) == 1) classes{i + NUM_BASE_CLASSES_GRADES_1_2, 2} = "math";
    elseif (mod(i, NUM_SUBJECTS_GRADES_3_4) == 2) classes{i + NUM_BASE_CLASSES_GRADES_1_2, 2} = "informathics";
    elseif (mod(i, NUM_SUBJECTS_GRADES_3_4) == 3) classes{i + NUM_BASE_CLASSES_GRADES_1_2, 2} = "history";
    elseif (mod(i, NUM_SUBJECTS_GRADES_3_4) == 4) classes{i + NUM_BASE_CLASSES_GRADES_1_2, 2} = "hungarian";
    elseif (mod(i, NUM_SUBJECTS_GRADES_3_4) == 5) classes{i + NUM_BASE_CLASSES_GRADES_1_2, 2} = "geography";
    elseif (mod(i, NUM_SUBJECTS_GRADES_3_4) == 6) classes{i + NUM_BASE_CLASSES_GRADES_1_2, 2} = "biology";
    elseif (mod(i, NUM_SUBJECTS_GRADES_3_4) == 7) classes{i + NUM_BASE_CLASSES_GRADES_1_2, 2} = "P.E.";
    elseif (mod(i, NUM_SUBJECTS_GRADES_3_4) == 0) classes{i + NUM_BASE_CLASSES_GRADES_1_2, 2} = "drawing";
    end
end
%j�nnek a nyelvi csoportok, �vfolyamonk�nt 3 angol, 1 n�met �s 1 spanyol
i = NUM_BASE_CLASSES;
classes{i+1,1} = "english1base";
classes{i+2,1} = "english1med";
classes{i+3,1} = "english1high";
classes{i+4,1} = "english2base";
classes{i+5,1} = "english2med";
classes{i+6,1} = "english2high";
classes{i+7,1} = "english3base";
classes{i+8,1} = "english3med";
classes{i+9,1} = "english3high";
classes{i+10,1} = "english4base";
classes{i+11,1} = "english4med";
classes{i+12,1} = "english4high";
classes{i+13,1} = "german1";
classes{i+14,1} = "german2";
classes{i+15,1} = "german3";
classes{i+16,1} = "german4";
classes{i+17,1} = "spanish1";
classes{i+18,1} = "spanish2";
classes{i+19,1} = "spanish3";
classes{i+20,1} = "spanish4";
for i = (NUM_BASE_CLASSES) + 1 : (NUM_BASE_CLASSES) + (NUM_LANG_CLASSES)
    if (contains(classes{i,1}, "english"))
        classes{i,2} = "english";
    elseif (contains(classes{i,1}, "german"))
        classes{i,2} = "german";
    else classes{i,2} = "spanish";
    end
end
%meghat�rozzuk a heti �rasz�mokat a k�l�nb�z� tant�rgyak kapcs�n
for i = 1 : (NUM_BASE_CLASSES) + (NUM_LANG_CLASSES) 
    if (classes{i,2} == "math" || classes{i,2} == "hungarian" || classes{i,2} == "english" || classes{i,2} == "german" || classes{i,2} == "spanish") classes{i,3} = 4;
    elseif (classes{i,2} == "informathics" || classes{i,2} == "history" || classes{i,2} == "P.E.") classes{i,3} = 3;
    elseif (classes{i,2} == "geography" || classes{i,2} == "biology" || classes{i,2} == "physics" || classes{i,2} == "chemistry" || classes{i,2} == "drawing") classes{i,3} = 2;
    else classes{i,3} = 1;
    end
end
%v�g�l j�nnek a fakult�ci�s csoportok, a heti �rasz�m egys�gesen 2
i = NUM_BASE_CLASSES + NUM_LANG_CLASSES;
classes{i+1,1} = "mathfact3";
classes{i+2,1} = "mathfact4";
classes{i+3,1} = "infofact3";
classes{i+4,1} = "infofact4";
classes{i+5,1} = "physicsfact3";
classes{i+6,1} = "physicsfact4";
classes{i+7,1} = "chemfact3";
classes{i+8,1} = "chemfact4";
classes{i+9,1} = "hunfact3";
classes{i+10,1} = "hunfact4";
classes{i+11,1} = "historyfact3";
classes{i+12,1} = "historyfact4";
classes{i+13,1} = "geofact3";
classes{i+14,1} = "geofact4";
classes{i+15,1} = "biofact3";
classes{i+16,1} = "biofact4";
classes{i+17,1} = "musicfact3";
classes{i+18,1} = "musicfact4";
classes{i+19,1} = "p.e.fact3";
classes{i+20,1} = "p.e.fact4";
for i = (NUM_BASE_CLASSES) + (NUM_LANG_CLASSES) + 1 : NUM_CLASSES
    if (contains(classes{i,1}, "math")) classes{i,2} = "math";
    elseif (contains(classes{i,1}, "info")) classes{i,2} = "informathics";
    elseif (contains(classes{i,1}, "physics")) classes{i,2} = "physics";
    elseif (contains(classes{i,1}, "chem")) classes{i,2} = "chemistry";
    elseif (contains(classes{i,1}, "hun")) classes{i,2} = "hungarian";
    elseif (contains(classes{i,1}, "history")) classes{i,2} = "history";
    elseif (contains(classes{i,1}, "geo")) classes{i,2} = "geography";
    elseif (contains(classes{i,1}, "bio")) classes{i,2} = "biology";
    elseif (contains(classes{i,1}, "music")) classes{i,2} = "music";
    else classes{i,2} = "P.E.";
    end
end
for i = (NUM_BASE_CLASSES) + (NUM_LANG_CLASSES) + 1 : NUM_CLASSES
    classes{i,3} = 2;
end
%a tan�rok sorsz�mot kapnak 1-30-ig
for i = 1 : NUM_TEACHERS
    teachers{i,1} = i;
end
%be�ll�tunk minden tan�rhoz k�t tant�rgyat, amelyet tud tan�tani
for i = 1 : 3
    teachers{i,2} = "math";
    teachers{i,3} = "informathics";    
end
for i = 4 : 6
    teachers{i,2} = "math";
    teachers{i,3} = "physics";
end
for i = 7 : 8
    teachers{i,2} = "math";
    teachers{i,3} = "chemistry";
end
for i = 9 : 11
    teachers{i,2} = "hungarian";
    teachers{i,3} = "history";
end
for i = 12 : 14
    teachers{i,2} = "hungarian";
    teachers{i,3} = "english";
end
for i = 15 : 16
    teachers{i,2} = "hungarian";
    teachers{i,3} = "german";
end
for i = 17 : 19
    teachers{i,2} = "history";
    teachers{i,3} = "geography";
end
for i = 20 : 21
    teachers{i,2} = "history";
    teachers{i,3} = "english";
end
i = 22;
teachers{i,2} = "english";
teachers{i,3} = "biology";
for i = 23 : 24
    teachers{i,2} = "biology";
    teachers{i,3} = "drawing";
end
for i = 25 : 26
    teachers{i,2} = "music";
    teachers{i,3} = "spanish";
end
for i = 27 : 30
    teachers{i,2} = "P.E.";
    teachers{i,3} = "none";
end
%0-val inicializ�ljuk az egyes tan�rok heti �rasz�m�t
for i = 1 : NUM_TEACHERS
    teachers{i,4} = 0;
end
pairings = [];
%az oszt�ly-tant�rgy entit�sok 2. oszlopa �s a tan�r entit�sok 2. �s 3.
%oszlopa tartalmazza a t�rgyneveket, ezekre v�gz�nk �sszehasonl�t�st, ha
%egyez�s�g van, akkor az adott tan�r tan�thatja az adott tant�rgyat az
%adott oszt�lynak, de m�g nem tudjuk, hogy fogja-e
for i = 1 : NUM_CLASSES
    for j = 1 : NUM_TEACHERS
        if (classes{i,2} == teachers{j,2} || classes{i,2} == teachers{j,3}) pairings{i,j} = 1;
        else pairings{i,j} = 0;
        end
    end
end
result = {};
%ebben a ciklusban m�r hozz�rendel�nk
for i = 1 : NUM_CLASSES
    for j = 1 : NUM_TEACHERS
        boole = 0;
        if (pairings{i,j} == 1)
            %j�n m�g egy be�gyazott ciklus annak �rdek�ben, hogy ha van
            %m�sik olyan tan�r is, aki tudja tan�tani az adott t�rgyat �s a
            %heti �rasz�m�nak aktu�lis �rt�ke kisebb, akkor � r� essen a
            %v�laszt�s az egyenl�tlen terhel�s elker�l�se v�gett
            for k = j : NUM_TEACHERS
                if (teachers{k,4} < teachers{j,4} && pairings{i,k} == 1) boole = 1;
                end
            end
            if (boole == 0)
                result{i,1} = classes{i,1};
                result{i,2} = classes{i,2};
                result{i,3} = teachers{j,1};
                teachers{j,4} = teachers{j,4} + classes{i,3};
                result{i,4} = teachers{j,4};
                break;
            end
        end
    end
end
for i = 1 : length(result)
    fprintf('%s %s %g %g\n', result{i,1}, result{i,2}, result{i,3}, result{i,4});
end

