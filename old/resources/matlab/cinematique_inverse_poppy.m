% clear all;close all;
% use_octave=0;
% if (use_octave==1),
%     % specifique octave
%     more off;
%     pkg load all;
% end
% 
% syms q1 q2 q3 q4 ;
% q = [q1 q2 q3 q4];
% syms Pxi Pyi Pzi;
% 
% NQ = 4;
% NB_FRAME = 5;
% 
% T_imoins1_i=cell(NB_FRAME);
%       %T_imoins1_i{1} = get_trans(  0,  0, 10) * get_rot_z(q1); %  passage du repere 0 au repere 1  
%       T_imoins1_i{1} = get_trans(  7.74,  -0.43, 12.92) * get_rot_x(q1); %  passage du repere 1 au repere 2
%       T_imoins1_i{2} = get_trans(  2.59,  -1.92,  0.07) * get_rot_y(-q2); %  passage du repere 2 au repere 3
%       T_imoins1_i{3} = get_trans(  -0.02,  1.88, -3.61) * get_rot_z(q3); %  passage du repere 3 au repere 4
%       T_imoins1_i{4} = get_trans(  -0.09,  0.96, -14.79)* get_rot_x(q4);
%       T_imoins1_i{5} = get_trans(  0,  -26, 0); %  passage du repere 4 au repere 5
% 
%       
%  T0i=cell(NB_FRAME,1);
%   for i_frame=1:NB_FRAME,
%     if (i_frame==1) ,
%       T0i{i_frame}=T_imoins1_i{i_frame};
%     else
%       T0i{i_frame}=T0i{i_frame-1} *T_imoins1_i{i_frame};
%     end  
%   end
%   
%       
% Verif =  subs(T0i{5},{'q1','q2','q3','q4'},{pi/4,pi/4,pi/4,pi/4})
% 
% iPi=[Pxi;Pyi;Pzi];
%   J0Pi=cell(NQ,1);
%   J0Ri=cell(NQ,1);
%   for i_frame=1:NB_FRAME,
%     % extraction des quantites 
%      T_0i=T0i{i_frame};
%      R_0i=T_0i(1:3,1:3); % repere i exprime dans repere 0
%      R_i0=R_0i.';        % => repere 0 exprime dans repere i
%      O_0i=T_0i(1:3,4)  ; % origine du repere i exprimee dans repere 0
%      J_0Pi=[];J_0Ri=[]; % init des jacobiennes en position et en orientation du repere i/ repere 0, exprimee dans le repere 0
%      for j=1:NQ, % on pourrait s'arreter a i_frame au lieu de NQ
%        qj=q(j);
%        JR0ij=diff(R_0i,qj);
%        JO0ij=diff(O_0i,qj);
%       %calcul de partial J0Pij = D0Pi/ Dqj, et concatenation a J_0Pi = D0Pi/ Dqk={1..j-1} 
%        J0Pij=JR0ij * iPi + JO0ij; 
%        J_0Pi=[J_0Pi,J0Pij];
%       %calcul de partial J0Rij = D0wi/ Dvqj, et concatenation a J_0Ri = D0wi/ Dqk={1..j-1} 
%        JS_0wij=JR0ij * R_i0; % derivee partielle de S(0wRi/R0) par rapport a qj 
%        J0wij=[JS_0wij(3,2); JS_0wij(1,3); JS_0wij(2,1)]; % extraction des coefs de la derivee partielle de 0wRi/R0 par rapport a qj
%        J_0Ri=[J_0Ri,J0wij]; % concatenation
%     end
%     % jacobienne   
%      J0Pi{i_frame}=simplify(J_0Pi);
%      J0Ri{i_frame}=simplify(J_0Ri);
%   end
% 
% matlabFunction(J0Pi{5},'File','computejacobpoppy.m')
% matlabFunction(T0i{5},'File','computegeometricpoppy.m')
  
fQi = [10.22;-25.51;-5.41];
Q1 = [0; 0; 0;0];

fQi_plus_1 = [0;-25.51;-5.41];
iter = 0;

while  and(iter < 200, norm(fQi_plus_1 - fQi) > 0.001)
    
    Jac = computejacobpoppy(0,0,0,Q1(1),Q1(2),Q1(3),Q1(4));
    Jinv = pinv(Jac);

    diff_fQi = fQi_plus_1 - fQi;
    delta_qi = Jinv *0.6 * diff_fQi;
    qi_plus_1 = Q1 + delta_qi;

    fqinew = computegeometricpoppy(qi_plus_1(1),qi_plus_1(2),qi_plus_1(3),qi_plus_1(4));
    fQi = double(fqinew(1:3,4));
    Q1 = qi_plus_1;
    
    iter = iter +1;
end


