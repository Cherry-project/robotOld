%--------------------------------------------------------------
% coordonnees du vecteur V dans le repere i, en fonction de ses coordonnees dans le repere j
%--------------------------------------------------------------
  function vi=get_Vi(Tij,vj)
    vj_0=[vj;0];   % on rajoute un 0 en dessous de vj, pour former vj_0
    vi_0=Tij*vj_0;
    vi=vi_0(1:3,1);
  end