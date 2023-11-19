<!DOCTYPE html>
<html> 
<head>
    <meta charset="UTF-8">
    <title>Листинг 10-4. Обработка данных формыиз листинга 10-3</title> 
</head> 
<body>
    <?php
        foreach ($_POST as $key=>$value) {  
            if (gettype($value) == "array") { 
                print "$key = <br>\n";
                foreach ($value as $v ) {
                    print "$v<br>";
                }
            } 
            else {
                print "$key = $value<br>\n";
            }
        }
    ?>
 </body> 
 </html>