<!DOCTYPE html>
<html>
<head>
    <title>Листинг 6-2. Использование блоков else и elseif</title>
</head>
<body>
    <?php
        function print_array($array) {
            foreach($array as $val) {
                print "$val  ";
            }
        }

        $treug = array();
        for ($n = 1; $n <= 10; ++$n) {
            array_push($treug, $n * ($n + 1) / 2);
        }
        // print_array($treug);

        $kvd = array();
        for ($n = 1; $n <= 10; ++$n) {
            array_push($kvd, $n * $n);
        }
        // print_array($kvd);

        $res = array_merge($treug, $kvd);
        sort($res);
        array_shift($res);
        // print_array($res);
        $res1 = array_unique($res);
        print_array($res1);

    ?>
</body>
</html>