% Paramètres du circuit
R = 1000;
C = 1e-6;

% Générer 100 fréquences de 1 Hz à 100 kHz
f = logspace(0, 5, 100);

% Calculer l'impédance pour chaque fréquence
Z_R = R * ones(size(f));
Z_C = 1 ./ (1i * 2 * pi * f * C);
Z_eq = Z_R + Z_C;

% Module et phase
module = abs(Z_eq);
phase = angle(Z_eq) * 180 / pi;

% Tracer
subplot(2,1,1);
semilogx(f, module);
ylabel('Module (Ohm)');
title('Réponse en fréquence - RC série (Octave)');
grid on;

subplot(2,1,2);
semilogx(f, phase);
xlabel('Fréquence (Hz)');
ylabel('Phase (deg)');
grid on;
print -dpng reponse_RC_octave.png

