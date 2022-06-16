a = imread('cameraman.tif');
figure(1),subplot(2,2,1),imshow(a),title('normal image');
% create a diamond structure
struct = strel('diamond', 3);

ao = imopen(a,struct);
figure(1),subplot(2,2,2),imshow(ao),title('opening using diamond structuring element');
ac = imclose(a,struct);
figure(1),subplot(2,2,3),imshow(ac),title('closing using diamond structuring element');

