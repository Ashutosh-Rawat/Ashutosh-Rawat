i = double(imread('cameraman.tif'));

c1 = 0.1;
c2 = 5;
c3 = 18;

L1 = c1.*(log(1+i));
L2 = c2.*(log(1+i));
L3 = c3.*(log(1+i));

figure(1), subplot(2,2,1), imshow(uint8(i)), title('normal image');
figure(1), subplot(2,2,2), imshow(uint8(L1)), title('log transformation c = 0.1');
figure(1), subplot(2,2,3), imshow(uint8(L2)), title('log transformation c = 5');
figure(1), subplot(2,2,4), imshow(uint8(L3)), title('log transformation c = 18');