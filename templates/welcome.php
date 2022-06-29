<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to 2022 Météo IT</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>
<body>
    <p>Welcome page</p>
    <p>Liste déroulante ou micro</p>
    <h1 > {{ message }}</h1>
    
    <a href="/weather-report">Test</a>
    
    <label for="city-select">Choose a city:</label>

<select name="cities" id="city-select" autofocus>
    <option value="paris">paris</option>
    <option value="lyon">lyon</option>
    <option value="marseille">marseille</option>
    <option value="nice">nice</option>
    <option value="dijon">dijon</option>
</select>

</body>
</html>
