<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        $user = "root";  
        $db = "sample";
        $table = "notebook";

        $conn = mysqli_connect("localhost", $user);
        if (!$conn) {
            print "Нет соединения с MySQL сервером";
            exit;
        }

        if (!mysqli_select_db($conn, $db)) {
            mysqli_close($conn);
            exit;
        }
        
        $query = "INSERT INTO $table (name, city, address, birthday, mail) VALUES('Игорь', 'Калыма', 'Улица Пушкина 1', '2021-09-04', 'prikol@mail.ru'), ('Анна', 'Нижний-Новгород', 
        'Улица Калинина', '2002-02-23', 'test1234@gmail.com'), ('Алексей', 'Урюпинск', 'Улица Космонавтом 32', '1980-09-21', 'sobaka@ya.ru')";
        if (!mysqli_query($conn, $query)) {
            $dberror = mysqli_error($conn);
            mysqli_close($conn);
            exit(-1);
        }

        print "Всё прошло успешно";
        mysqli_close($conn);
    ?>
</body>
</html>