
clear;close all
len = 1000;C = 500-6;
t = linspace(0,10,len);
v = 12.*(1-exp(1-(0.5)*t));
figure(1); clf;
plot(t,v);
xlabel Time(s); ylabel Voltage(volts)
title('Voltage');
for i = 1:len-1
    dt = t(i+1) - t(i);
    dv = v(i+1) - v(i);
    dvdt(i) = dv/dt;
end
current = C*dvdt;
figure(2); clf;
plot(t(1:length(dvdt)),current);
title('Current')
xlabel Time(s); ylabel Current(amps)
