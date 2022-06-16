i = imread('coloredchips.jpg');

gray = rgb2gray(i);
[centers,radii] = imfindcircles(gray,[20 25],'ObjectPolarity','dark', ... 
    'Sensitivity', 0.975, 'Method', 'twostage');

%[centersBright,radiiBright,metricBright] = imfindcircles(gray,[20 25], ...
%    'ObjectPolarity','bright','Sensitivity',0.92,'EdgeThreshold',0.1);

%hBright = viscircles(centersBright, radiiBright,'Color','b');

imshow(i);
h = viscircles(centers,radii);
length(centers)
