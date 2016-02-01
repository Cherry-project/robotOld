%-----------------------------------------------------------------------------
% coordonnees du point P dans le repere i, en fonction de ses coordonnees dans le repere j
%--------------------------------------------------------------
  function Pi=get_Pi(Tij,pj)
    pj_1=[pj;1];   % on rajoute un 1 en dessous de Pj, pour former pj_1
    pi_1=Tij*pj_1;
    Pi=pi_1(1:3,1);
  end
