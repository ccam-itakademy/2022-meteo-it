<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Résultats de la recherche météo</title>
</head>
<body>
    <ul>
        {% for key, value in weather_report: %}
            <li id="{{ key }}">{{ value['value'] }} {{ value['unit'] if value['unit'] }}</li>
        {% endfor %}
    </ul>
</body>
</html>
