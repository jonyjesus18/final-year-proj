% Create a new figure window.
figure('Name', 'Longitude and Latitude Plot')

% Add a geographic axes to the figure window.

geoshow(lat,lon,data)

% Add a title and labels to the plot.
title('Longitude and Latitude Plot')
