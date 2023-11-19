<?php
    $username = "p07";
    $password = "ibivfrjd753159!#";
    $database = "databasez4";
    $hostname = "localhost";
    $conn = mysqli_connect($hostname, $username, $password, $database);

    if (!$conn) {
        die("Нет соединения с БД.");
    }
?>