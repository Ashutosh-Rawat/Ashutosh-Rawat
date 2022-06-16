i = imread('cameraman.tif');
figure(1), subplot(221), imshow(i), title('normal image');

i1 = histeq(i);
figure(1), subplot(222), imshow(i1), title('contrast enhancement using histeq');

i2 = imadjust(i);
figure(1), subplot(223), imshow(i2), title('imadjust');

i3 = adapthisteq(i);
figure(1), subplot(224), imshow(i3), title(' adapthisteq');
