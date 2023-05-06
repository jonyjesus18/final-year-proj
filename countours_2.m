altitudes = [24, 30, 36];
levels = [1, 2, 3];

% Calculate the average mfx values over latitudes
mfx_avg_lat = squeeze(mean(Airs.NH.Night.mfx, 1));

% Create a 2D matrix for altitude with the same dimensions as Airs.NH.Lon
Alt2D = repmat(reshape(altitudes(levels), [1, 1, length(levels)]), [size(Airs.NH.Lon, 1), size(Airs.NH.Lon, 2), 1]);

figure;
pcolor(Airs.NH.Lon, Alt2D(:,:,1), mfx_avg_lat(levels, :));
shading interp;

xlabel('Longitude');
ylabel('Altitude (km)');
title('mfx values averaged over latitudes');
colorbar;
