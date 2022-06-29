<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../static/main.css">

    <title>Résultat de la recherche</title>
    
</head>
<body>
        <h1 id="location">{{ location }}</h1>

        <img src="../assets/soleil.png" alt="soleil">
        
        <h2 id="day_average_temperature">{{ day_average_temperature }}</h2>

        <div id="rain">{{ rain }}</div>

        <div id="weather_description">{{ weather_description }}</div>

        <div class="container">

            <div id="day_min_temperature">{{ day_min_temperature }}</div>

            <div id="day_max_temperature">{{ day_max_temperature }}</div>

        <div>

        <div id="humidity">{{ humidity }}</div>

        <div id="wind">{{ wind }}</div>
    
</body>
</html>