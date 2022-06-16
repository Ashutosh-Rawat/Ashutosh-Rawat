i = imread('cameraman.tif');
figure(1),subplot(2,2,1),imshow(i),title('normal image');
gauss = imgaussfilt(i,2); 
figure(1),subplot(2,2,2),imshow(gauss),title('gaussian filter');
median = medfilt2(i);
figure(1),subplot(2,2,3),imshow(median),title('median filter');

a = 0.5;
b = 0.2;
laplace = locallapfilt(i,a,b);
figure(1),subplot(2,2,4), imshow(laplace),title('laplacian filter');

PSF = fspecial('motion',21,11);
Idouble = im2double(i);
blurred = imfilter(Idouble,PSF,'conv','circular');
figure(2),subplot(1,2,1),imshow(blurred),title('blurred image');
weiner = deconvwnr(blurred, PSF);
figure(2),subplot(1,2,2),imshow(weiner),title('blur removal using weiner filter');
