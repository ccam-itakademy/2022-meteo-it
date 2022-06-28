<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Résultat de la recherche</title>
</head>
<body>
    <ul>
        <li id="location">{{ location }}</li>
        <li id="day_average_temperature">{{ day_average_temperature }}</li>
        <li id="day_min_temperature">{{ day_min_temperature }}</li>
        <li id="day_max_temperature">{{ day_max_temperature }}</li>
        <li id="weather_description">{{ weather_description }}</li>
        <li id="humidity">{{ humidity }}</li>
        <li id="wind">{{ wind }}</li>
        <li id="rain">{{ rain }}</li>
    </ul>
    
    <a href="/welcome">GO back</a>
</body>
</html>
