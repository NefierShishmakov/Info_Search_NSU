<!DOCTYPE html>
<html>
<head>
    <title>Листинг 1-2. Документ, содержащий PHP-команды и HTML-текст</title>
</head>
<body>
    <p><i>Checking</i></p>
    <?php
        $color = "blue";
        $size = 20;
        print "<p style=\"color:$color;font-size:${size}px;\">PHP is working</p>";
    ?>
</body>
</html>