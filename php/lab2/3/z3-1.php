<!DOCTYPE html>
<html>
<head>
    <title>Листинг 6-2. Использование блоков else и elseif</title>
</head>
<body>
    <?php
        $cell_background_color = "blue";
        print "<table border=1 cellpadding=5px>\n";
        $y = 1;
        while ($y <= 10) {
            print "<tr>\n";
            $x = 1;
            while ($x <= 10) {
                if ($x == $y) {
                    print "\t<td bgcolor=\"$cell_background_color\">";
                } else {
                    print "\t<td>";
                }
                print ($x * $y);
                print "</td>\n";
                ++$x;
            }
            print "</tr>\n";
            ++$y;
        }
        print "</table>";
    ?>
</body>
</html>