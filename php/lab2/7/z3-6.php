<!DOCTYPE html>
<html>
<head>
    <title>Листинг 6-2. Использование блоков else и elseif</title>
</head>
<body>
    <?php
        function print_associative_array($array) {
            foreach($array as $key => $val) {
                print "$key: $val<br>";
            }
        }

        $cust = array(
            'cnum' => 2001,
            'cname' => "Hoffman",
            'city' => "London",
            'snum' => 1001,
            'rating' => 100
        );  
        // print_associative_array($cust);
        // asort($cust);
        // print_associative_array($cust);
        // ksort($cust);
        // print_associative_array($cust);
        sort($cust);
        print_associative_array($cust);
    ?>
</body>
</html>