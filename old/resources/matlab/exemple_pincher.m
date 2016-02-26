%---------------------------------------------------------------------------
% entete standard, on efface tout (et on charge les fonctions de calcul symbolique
%---------------------------------------------------------------------------
  clear all;close all;
  use_octave=0;
  if (use_octave==1),
  % specifique octave
    more off;
    pkg load all;
  end
  t=[0;5;10;15;20];
  th_1234= [0   ,0,0,0;
            pi/4,0,0,0;
            pi/4,pi/4,0,0;
            pi/4,pi/4,pi/4,0;
            pi/4,pi/4,pi/4,pi/4];
  nb_points=length(t);
  pince_12=zeros(nb_points,2);  
  tab_q=[th_1234,pince_12];         
%---------------------------------------------------------------------------------
% 6- ecriture des donnees sous forme d'un fichier exploitable par v_rep
%---------------------------------------------------------------------------------
  my_write_pincher_trajectory(t,tab_q,'pincher_trajectory.txt');  