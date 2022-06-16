i = imread('cameraman.tif');
figure(1), subplot(231), imshow(i), title('original image');

e1 = edge(i,'sobel');
figure(1), subplot(232), imshow(e1), title('sobel edge detection');

e2 = edge(i,'canny');
figure(1), subplot(233), imshow(e2), title('canny edge detection');

e3 = edge(i,'roberts');
figure(1), subplot(234), imshow(e3), title('roberts edge detection');

e4 = edge(i,'prewitt');
figure(1), subplot(235), imshow(e4), title('prewitt edge detection');