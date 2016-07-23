function [count,sorted]= sort_and_count(A)
l=length(A);
if l>1
    [X,B]=sort_and_count(A(1:floor(l/2),1));
    [Y,C]=sort_and_count(A(floor(l/2)+1:end,1));
    [Z,sorted]=CountSplitInv(B,C);
    count=X+Y+Z;
else
    count=0;
    sorted=A;
end
end
    