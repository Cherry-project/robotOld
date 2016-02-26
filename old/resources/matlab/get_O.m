%---------------------------------------------
% origine repere j exprimee dans le repere i, exemple
% Tij=get_trans(2,2,3)*get_rot_u([-1;0;0],pi);
%  oij=get_O(Tij);
%---------------------------------------------
  function oij=get_O(Tij)
    oij=Tij(1:3,4);
  end
  