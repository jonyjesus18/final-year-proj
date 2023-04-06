% Create a new figure window.
figure('Position',[100 100 500 500])

% Add a map axes object to the figure.
map = newmap('crs','WGS84');

lat = Airs.NH.Lat;
lon = Airs.NH.lon;

% Set the map limits to the extent of the data.
map.limits = [-180 -90 180 90];

% Plot the longitude and latitude vectors on the map axes.
plot(lat,lon,'b-')

data = Airs.NH.Night.k(:,:,1);

% Plot the data vector on the map axes.
plot(lat,lon,data,'r.')

% Add a title and axis labels to the map.
title('My Map')
xlabel('Longitude')
ylabel('Latitude')

% Save the figure.
saveas(figure,'my_map.png')