<!DOCTYPE html>
<html> 
    <head>
        <title> Листинг 10-1. Простая HTML-форма </title>
        <meta charset="UTF-8">
    </head> 
    <body>
        <?php
            function get_right_answers_num($otv, $answers) {
                $result = 0;
                for ($i = 0; $i < 9; ++$i) {
                    if ($otv[$i] == $answers[$i]) {
                        $result += 1;
                    }
                }

                return $result;
            }

            function get_result_text_based_on_right_answers_num($name, $right_answers_num) {
                switch ($right_answers_num) {
                    case 9:
                        $result_text = " вы великолепно знаете географию";
                        break;
                    case 8:
                        $result_text= " вы отлично знаете географию";
                        break;
                    case 7:
                        $result_text = " вы очень хорошо знаете географию";
                        break;
                    case 6:
                        $result_text = " вы хорошо знаете географию";
                        break;
                    case 5:
                        $result_text = " вы удовлитворительно знаете географию";
                        break;
                    case 4:
                        $result_text = " вы терпимо знаете географию";
                        break;
                    case 3:
                        $result_text = " вы плохо знаете географию";
                        break;
                    case 2:
                        $result_text = " вы очень плохо знаете геогрфию";
                        break;
                    default: 
                        $result_text = " вы вообще не знаете географию";
                }

                return $name . $result_text;
            }


            $otv = array("6","9","4","1","3","2","5","8","7");
            $answers = $_POST["answers"];
            $name = $_POST["user"];

            $right_answers_num = get_right_answers_num($otv, $answers);
            $result_text = get_result_text_based_on_right_answers_num($name, $right_answers_num);

            
            print "<p align='center'>$result_text";
            print "<p align='center'><a href='z4-3a.html'>назад</a>";

        ?>
    </body> 
</html>