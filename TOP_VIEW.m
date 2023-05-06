load('20220101_AIRS_3DST-1_40km_grid.mat')
[Airs.X,Airs.Y] = ndgrid(Airs.x,Airs.y); 
[Airs.NH.Lat,Airs.NH.Lon] = reckon( 89.999,0,km2deg(sqrt(Airs.X.^2 + Airs.Y.^2)),atan2d(Airs.X,Airs.Y)); 
[Airs.SH.Lat,Airs.SH.Lon] = reckon(-89.999,0,km2deg(sqrt(Airs.X.^2 + Airs.Y.^2)),atan2d(Airs.X,Airs.Y)); 
addpath('m_map')
m_proj('stereographic','lat',90,'long',60,'radius',50);

m_pcolor(Airs.NH.Lon,Airs.NH.Lat,Airs.NH.Night.mfx(:,:,2).*1);

m_coast('color','k');

m_grid();

colorbar

clim([-0.08 0.08])
altitudes = [24, 30, 36];
levels = [1, 2, 3];
