function [count,sorted]=CountSplitInv(B,C)
if ~isempty(B) && ~isempty(C)
    if B(1,1)< C(1,1)
        [c,d]=CountSplitInv(B(2:end,1),C);
        sorted=[B(1,1);d];
        count=c;
    else
       [c,d]=CountSplitInv(B,C(2:end,1));
       sorted=[C(1,1);d];
       count=c+length(B);
    end
elseif isempty(B)
    count=0;
    sorted=C;
else
    count=0;
    sorted=B;
end