a = imread('autumn.tif');
figure(1), subplot(2,2,1), imshow(a), title('rgb image');

b = rgb2hsv(a);
figure(1), subplot(2,2,2), imshow(b), title('hsv image');

c = rgb2ntsc(a);
figure(1), subplot(2,2,3), imshow(c), title('yiq image');


% showing color components of hsv
figure(2),surf(peaks);
colormap('hsv');

e = hsv(100);
f = flipud(e);
colormap(f);




