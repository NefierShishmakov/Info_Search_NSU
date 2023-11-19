<!DOCTYPE html>
<html>
<head>
    <title>Листинг 6-2. Использование блоков else и elseif</title>
</head>
<body>
    <?php
        function Ru($color) {
            print "<p style=\"color:$color;\">Здравствуйте!</p>";
        }

        function En ($color) {
            print "<p style=\"color:$color;\">Hello!</p>";
        }

        function Fr($color) {
            print "<p style=\"color:$color;\">Bonjour!</p>";
        }

        function De($color) {
            print "<p style=\"color:$color;\">Guten Tag!</p>";
        }

        $lang = $_GET["lang"];
        $color = $_GET["color"];

        switch ($lang):
            case "Ru":
                Ru($color);
                break;
            case "En":
                En($color);
                break;
            case "De":
                De($color);
                break;
            case "Fr":
                Fr($color);
                break;
            default:
                print "<p style=\"color:$color;\">Unknown language</p>";
        endswitch;
    ?>
</body>
</html>