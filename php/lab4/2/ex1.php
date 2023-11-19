<?php
    $mysql_user = "root";  
    $conn = mysqli_connect("localhost", $mysql_user); 
    if (!$conn ) die("Нет соединени¤ с MySQL");
    
    $database = "sample";
    if (!mysqli_select_db($conn, $database)) {
        print "Нельзя открыть $database";
        mysqli_close($conn);
        exit;
    } 

    $new_table_name = "notebook";
    $query = "DROP TABLE IF EXISTS " . $new_table_name;

    $result = mysqli_query($conn, $query);
    if (!$result) {
        print "Не получилось дропнуть таблицу $new_table_name";
        mysqli_close($conn);
        exit;
    }

    $query = "CREATE TABLE " . $new_table_name . 
    "(id int NOT NULL AUTO_INCREMENT,
      name varchar(50),
      city varchar(50),
      address varchar(50),
      birthday date,
      mail varchar(20),
      PRIMARY KEY(id))";


    $result = mysqli_query($conn, $query);
    if (!$result) {
        print "Не получилось создать таблицу $new_table_name";
        mysqli_close($conn);
        exit;
    }

    mysqli_close($conn);
?>