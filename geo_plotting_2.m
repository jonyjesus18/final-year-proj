% Create a new figure window.
figure('Position',[100 100 500 500])

% Add a map view object to the figure.
figure
p = projcrs(3035);
newmap(p)