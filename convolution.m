A = [0,1,2,2,2;
    2,0,0,1,1;
    1,0,0,2,2;
    1,2,0,1,1;
    0,1,2,2,2];
% A = padarray(A,[1,1]);
k1 = rot90([0,1,1;-1,1,0;0,0,0],2);
k2 = rot90([0,0,-1;1,1,1;-1,-1,1],2);
k3 = rot90([1,1,0;0,1,-1;1,-1,-1],2);
conv2(A,k1,'same');
conv2(A,k2,'same');
conv2(A,k3,'same')
%%
x = -4:0.01:4;
relu = max(0,x);
lrelu = max(0,x) + 0.1*min(0,x);
tanhx = tanh(x);

x0 = zeros(size(x));
plot(x, tanhx, 'LineWidth',2)
hold on
plot(x, x0, 'k--')
axis([-4,4,-4,4])
set(gca,'FontSize',18)