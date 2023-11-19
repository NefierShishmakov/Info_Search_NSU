<!DOCTYPE html>
<html>
<head>
    <title>Листинг 6-2. Использование блоков else и elseif</title>
</head>
<body>
    <?php
        $lang = $_GET["lang"];

        if ($lang == "ru") {
            print "The current language is Russian";
        } elseif ($lang == "en") {
            print "The current language is English";
        } elseif ($lang == "de") {
            print "The current language is Deutch";
        } elseif ($lang == "fr") {
            print "The current language is French";
        } else {
            print "Unknown language";
        }

    ?>
</body>
</html>