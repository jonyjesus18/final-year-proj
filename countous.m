load('20220101_AIRS_3DST-1_40km_grid.mat')
[Airs.X,Airs.Y] = ndgrid(Airs.x,Airs.y); 
[Airs.NH.Lat,Airs.NH.Lon] = reckon( 89.999,0,km2deg(sqrt(Airs.X.^2 + Airs.Y.^2)),atan2d(Airs.X,Airs.Y)); 
[Airs.SH.Lat,Airs.SH.Lon] = reckon(-89.999,0,km2deg(sqrt(Airs.X.^2 + Airs.Y.^2)),atan2d(Airs.X,Airs.Y));

altitudes = [24, 30, 36];
levels = [1, 2, 3];

figure;

for i = 1:length(levels)
    subplot(length(levels), 1, i);
    
    m_proj('stereographic','lat',90,'long',60,'radius',50);
    m_contour(Airs.NH.Lon, Airs.NH.Lat, Airs.NH.Night.mfx(:,:,levels(i)));
    
    m_coast('color', 'k');
    m_grid();
    
end
title(['mfx contours at ', num2str(altitudes(i)), ' km altitude']);
colorbar;