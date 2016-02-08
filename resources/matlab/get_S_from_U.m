%-----------------------------------------------------------------------------
% renvoie la matrice anti symetrique liée au produit vectoriel a gauche par u
%-----------------------------------------------------------------------------
  function S=get_S_from_U(u)
    ux=u(1);uy=u(2);uz=u(3);
    S=[ [0  ,-uz,uy ]
        [uz ,0  ,-ux]
        [-uy,ux ,0  ]        
      ];        
  end