<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title> Листинг 10-2. Чтение данных формы из листинга 10-1 </title>
        <style>
            /* body {
                background-color: silver;
                color: black;
            }
            a:link {
                color: white;
            }
            a:active {
                color: maroon;
            } */
        </style>
    </head>
    <body>
        <?php
            $align = $_GET["align"];
            $valign = $_GET["valign"];

            print "<table border=\"1px\" width=\"100px\" height=\"100px\" text-align=\"$align\" align=\"center\">\n";
            print "<tr><td align=\"$align\" valign=\"$valign\">Текст</td></tr></table>\n";
            print "<p style='text-align: center'><a href='z4-1a.html'>назад</a>";
        ?>
    </body>
</html>