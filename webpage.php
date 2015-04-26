<?php

function weather_readcsv($filename, $header=false) {
$handle = fopen($filename, "r");
$CityState = chop($filename, "analysis.csv");
echo "<caption><u><b>$CityState Prediction Analysis</b></u></caption>";
echo '<table>';
//display header row if true
if ($header) {
    $csvcontents = fgetcsv($handle);
    echo "<tr>\r\n";
    foreach ($csvcontents as $headercolumn) {
        echo "<th>$headercolumn</th>\r\n";
    }
    echo "</tr>\r\n";
}
// displaying contents
while ($csvcontents = fgetcsv($handle)) {
    echo "<tr>\r\n";
    foreach ($csvcontents as $column) {
        echo "<td>$column</td>\r\n";
    }
    echo "</tr>\r\n";
}
echo '</table>';
fclose($handle);
}


weather_readcsv('BoulderCOanalysis.csv', true);

?>