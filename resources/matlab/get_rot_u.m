%--------------------------------------------------------------
% rotation de theta autour de l'axe u ( formule de Rodrigues )
%--------------------------------------------------------------
  function T=get_rot_u(U,theta)
    c=cos(theta);
    s=sin(theta);
    R=U*U.'*(1-c) +eye(3,3)*c+get_S_from_U(U)*s
    T=[R,[0;0;0]];
    T=[T;[0,0,0,1]];
  end