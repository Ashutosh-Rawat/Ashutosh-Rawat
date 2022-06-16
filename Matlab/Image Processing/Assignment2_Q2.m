a=imread('coins.png');
subplot(231);
imshow(a);
title('Coins');
subplot(232);

imhist(a);
title('Histogram');
b1=a>99;
subplot(233);
imshow(b1);
title('Using Threshold Value');

BW=imbinarize(a,0.4667);
subplot(234);
imshow(BW);
title('Using Histogram');
level=graythresh(a);
BW1=imbinarize(b1,level);
subplot(235);
imshow(BW1);
title('Using Greythresh');
display(level);
