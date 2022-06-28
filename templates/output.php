<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Résultat de la recherche</title>
</head>

<?php
$conf = include('config.php');
$weather_description = file_get_contents('/Applications/MAMP/htdocs/2022-meteo-it/scripts/traitement/weather_description.txt');

$backgroundUrl = null;
// a définir : tableauPluie, tableauSoleil, tableauNuage, tableauNeige
// faire plusieurs if ou un switch pour mettre la bonne valeur dans $backgroundUrl
// if (in_array($weather_description, $tableauPluie)) {
if ($weather_description == "Ensoleillé") {
    $backgroundUrl = $conf['soleil'];
};

echo $backgroundUrl;
?>

<body style="background:url(<?php echo $backgroundUrl; ?>);">
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
</body>
</html>