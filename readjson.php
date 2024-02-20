// We will start by getting the contents out of a json file

<?php
    $sample_json = file_get_contents('results.json');
    $decoded_json = json_decode($sample_json, true);
    
    //here we specify values to use in php, which we extract from the json
    $player_name = $decoded_json['Player'];
    $kill_count = $decoded_json['Kills'];
    $death_count = $decoded_json['Deaths'];
    $credit_count = $decoded_json['Credits'];
    $score_count = $decoded_json['Score'];
    $team_side = $decoded_json['Team'];
    
    $advsample_json = file_get_contents('advresults.json');
    $advdecoded_json = json_decode($advsample_json, true);
    
    // here we want to add some extra details, calculations to php
    // like when the match was played, total number of players
    // which team had the highest score or kill count etc.
    $match_date = $advdecoded_json['MATCH_DATE'];
    $total_player = $advdecoded_json['TOTAL_PLAYER_COUNT'];
    $total_score = $advdecoded_json['TOTAL_SCORE'];
    $teams = $advdecoded_json['TEAMS'];
?>
