%
% Calculate the grade of the student from an index.
%
% param i: index of the class, non-negative integer
%
% return: grade
%
function grade = calc_grade(i)
    grade = floor((i - 1) / 5) + 1
end

