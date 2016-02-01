% return a symbolic matrix / vector of defined name and size
% example
% a=sym_matrix('a',[3,4])
% b=sym_matrix('b',[3,1])
% c=sym_matrix('c',2)

function m = sym_matrix(name,size) 
  if length(size)==1,
    m=[];
    for i=1:size(1),
      name_mi=[name,int2str(i)];
      mi=sym(name_mi);
      m=[m;mi];
    end
    return
  end
  if length(size)==2,
    m=[];
    for i=1:size(1),
      mi=[];
      for j=1:size(2),
        name_mij=[name,int2str(i),'_',int2str(j)];
        mij=sym(name_mij);
        mi=[mi,mij];
      end
      m=[m;mi];  
    end
    return
  end
end  