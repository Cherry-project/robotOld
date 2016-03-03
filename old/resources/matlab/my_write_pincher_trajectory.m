function my_write_pincher_trajectory(t,tab_q,fileName)
    %----------------------------------------------------------------------
    % parametres importants (pour adaptation eventuelle a d'autres robots
    %----------------------------------------------------------------------
    T_STAY_AFTER_SIMU=5; % 5 secondes rajoutees en fin de simulation
    [Nb_instants,Nb_vars]=size(tab_q);
    % dependant du robot% ATTENTION LA CHAINE DE FORMAT NE S'ADAPTE PAS AUTOMATIQUEMENT AU NOMBRE D'OBJETS
  str_format='%12.8f %12.8f %12.8f %12.8f %12.8f %12.8f %12.8f\n';    
  tmax=T_STAY_AFTER_SIMU+max(t);
  tmax_ms=round(1000*tmax);
% FIXER MANUELLEMENT LE NB D'OBJETS ICI
  object=cell(6);
% ATTENTION LA CHAINE DE FORMAT NE S'ADAPTE PAS AUTOMATIQUEMENT AU NOMBRE D'OBJETS
  str_format='%12.8f %12.8f %12.8f %12.8f %12.8f %12.8f %12.8f\n';    
    
    i=1;object{i}=struct();object{i}.name='PhantomXPincher_joint1'; object{i}.type='Axis';object{i}.mode='Position';
    i=2;object{i}=struct();object{i}.name='PhantomXPincher_joint2'; object{i}.type='Axis';object{i}.mode='Position';
    i=3;object{i}=struct();object{i}.name='PhantomXPincher_joint3'; object{i}.type='Axis';object{i}.mode='Position';
    i=4;object{i}=struct();object{i}.name='PhantomXPincher_joint4'; object{i}.type='Axis';object{i}.mode='Position';
    i=5;object{i}=struct();object{i}.name='PhantomXPincher_gripperCenter_joint'; object{i}.type='Axis';object{i}.mode='Position';
    i=6;object{i}=struct();object{i}.name='PhantomXPincher_gripperClose_joint'; object{i}.type='Axis';object{i}.mode='Position';
    NbObject=length(object); % 4 objets a representer
    %----------------------------------------------------------
    % ecriture entete (verifier les premieres parametres )
    %----------------------------------------------------------
    Entete=cell(1);i=0;
    i=i+1; Entete{i}=    '#--------------------------';
    i=i+1; Entete{i}=   '#connection, refresh time  ';
    i=i+1; Entete{i}=   '#--------------------------';
    i=i+1; Entete{i}=   'IpAddr=127.0.0.1';
    i=i+1; Entete{i}=   'PortNB=19997';
    i=i+1; Entete{i}=   'loopTimeMs=5';
    i=i+1; Entete{i}=   sprintf('maxTimeMs=%d',tmax_ms);
    i=i+1; Entete{i}=   'verbose=0';
    i=i+1; Entete{i}=   '#---------------------------------';
    i=i+1; Entete{i}=   '#parameters(unused for instance ) ';
    i=i+1; Entete{i}=   '#---------------------------------';
    i=i+1; Entete{i}=   'NbParam=0';
    i=i+1; Entete{i}=   '##--------------------------------------------------------';
    i=i+1; Entete{i}=   '## Object displacment example                             ';
    i=i+1; Entete{i}=   '##--------------------------------------------------------';
    i=i+1; Entete{i}=   '#----------------------------------------------';
    i=i+1; Entete{i}=   '# Objects';
    i=i+1; Entete{i}=   '# Type :Axis :Mode : Position, or Force  (one coordinate )';
    i=i+1; Entete{i}=   '# Type :Objet3D :Mode : Position, or EulerXYZ (3 coordinates each )';
    i=i+1; Entete{i}=   '#--------------------------------------------';
    i=i+1; Entete{i}=   ['NbObject=',int2str(NbObject)];
    i=i+1; Entete{i}=   '##-------------------------------------------------------';
    i=i+1; Entete{i}=   '## axis (joint) control example (axis angle are in rad )';
    i=i+1; Entete{i}=   '##--------------------------------------------------------';
    for io=1:NbObject,
        oi=object{io};
        i=i+1; Entete{i}=   ['#Object ',int2str(io)];
        i=i+1; Entete{i}=   ['ObjectName=',oi.name];
        i=i+1; Entete{i}=   ['ObjectType=',oi.type];
        i=i+1; Entete{i}=   ['ObjectMode=',oi.mode];
    end
    i=i+1; Entete{i}=   '#---------------------------------------------------------------------';
    i=i+1; Entete{i}=   '#each line represents trajectory coordinates, separated by spaces';
    i=i+1; Entete{i}=   '# t object1_coords  object2Coords ...';
    i=i+1; Entete{i}=   '#---------------------------------------------------------------------';
    i=i+1; Entete{i}=   ['NbPoint=',int2str(Nb_instants)];
    y = [t,tab_q];
% on rajoute 5 secondes a la simulation 
   n=length(t);
   y_n=[t(n)+T_STAY_AFTER_SIMU,tab_q(n,:)];
   y=[y;y_n];  

    fid = fopen(fileName,'w');
    for i=1:length(Entete),
        fprintf(fid,'%s\n',Entete{i});
    end
    fprintf(fid,str_format,y.');
    fclose(fid);
end