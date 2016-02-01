%--------------------------------------------------------------
% matrice de transformation homogene inverse
% exemple :
% Tji=get_rot_x(pi/2);
% Tji=get_inv_TtTji);
% Tii=Tij*Tji;  %% Tii= Identity44
%--------------------------------------------------------------
  function Tji=get_InvT(Tij)
    Oij=Tij(1:3,4);   % origine repere j exprimee dans repere i= Tij, lignes 1 a 3, colonne 4
    Rij=Tij(1:3,1:3); % Rij=vecteurs [xj,yj,zj] exprimes suivant [xi,yi,zi]=Tij lignes 1 a 3, colonnes 1 a 3
    Rji=Rij.';         % Rji=vecteurs [xi,yi,zi] exprimes suivant [xj,yj,zj] = transposee de Rij
    Oji=-Rji*Oij;     % Oji = origine repere i exprimee dans repere j = Rji . [-Oij]
    Tji=[[ Rji,Oji];[0,0,0,1 ] ];
  end