function T=get_dh(th,a,d,alpha)
%-----------------------------------------------------------------------------
% Denavit Hartenberg
%--------------------------------------------------------------
    
    T = get_rot_z(th) * get_trans(a,0,d) * get_rot_x(alpha);
  end