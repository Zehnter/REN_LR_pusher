// We will start by getting the contents out of a json file

<?php
    $sample_json = file_get_contents('sample.json');
    $decoded_json = json_decode($sample_json, true);
    
    //here we specify values to use in php, which we extract from the json
    $match_date = $decoded_json['MATCH_DATE'];
    $total_player = $decoded_json['TOTAL_PLAYER_COUNT'];
    $total_score = $decoded_json['TOTAL_SCORE'];
    $teams = $decoded_json['TEAMS'];

    // below will show the date the match was played, then the current date.
    // It is my intention to show how much time has since passed in the line of code below.
    echo "This match was played on" . $match_date . ". Today is " . date("d-m-y") . ". ";
    ?>