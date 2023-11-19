<!DOCTYPE html>
<html>
<head>
    <title>Листинг 6-2. Использование блоков else и elseif</title>
    <style>
        .blue {
            color: blue;
        }
        .red {
            color: red;
        }
    </style>
</head>
<body>
    <?php
        $cell_background_color = "blue";
        print "<table border=1 cellpadding=5px>\n";
        for ($y = 1; $y <= 10; $y++) {
            print "<tr>\n";
            for ($x = 1; $x <= 10; $x++) {
                if ($y == 1 && $x == 1) {
                    print "\t<td class=\"red\">";
                } else if ($y == 1 || $x == 1) {
                    print "\t<td class=\"blue\">";  
                } else {
                    print "\t<td>";
                }

                if ($y == 1 && $x == 1) {
                    print "+";
                } else if ($x == 1 || $y == 1) {
                    print ($x + $y - 1);
                } else {
                    print ($x + $y);
                }
                print "</td>\n";
            }
            print "</tr>\n";
        }
        print "</table>";
    ?>
</body>
</html>