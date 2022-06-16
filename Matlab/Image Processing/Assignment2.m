co=imread ('rice.png');
co1=im2double(co);
subplot(221);
imshow(co1);
title('Coins');
whos('co1*');
ma=zeros(256,256);
ma1=im2double(ma);
title('Mask Unprocessed');

for i=107:140
j=16:28;
ma1(i,j)=1;
end
subplot(222);
imshow(ma1);
fi=immultiply(co1,ma1);
subplot(223);
imshow(fi);
