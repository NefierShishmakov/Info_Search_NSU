<!DOCTYPE html>
<html> 
<head>
    <meta charset="UTF-8">
    <title>Листинг 10-3. HTML-форма с выбором из списка</title> 
</head> 
<body>
    <form action="ls10-5.php" method="post">
        <p>Введите ваше имя
        <p><input type="text" name="user">
        <p>Что вы любите делать в свободное время <br>
        <p><input type="checkbox" name="hobby[]"
            value="слушать музыку">слушать музыку
        <p><input type="checkbox" name="hobby[]"
            value="читать книгу">читать книгу
        <p><input type="checkbox" name="hobby[]"
            value="смотреть телевизор">смотреть телевизор
        <p><input type="checkbox" name="hobby[]"
            value="гулять на улице">гулять на улице
        <p><input type="submit" value="Выбор сделан">
    </form>
</body> 
</html>