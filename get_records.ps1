# $url = 'http://httpbin.org/json'
$url = 'http://www.euclidea.xyz/api/v1/game/numbers/solutions/records'
$r = Invoke-WebRequest $url
$r.content >> ./result.json

$results = Get-Content .\result.json | ConvertFrom-Json
$records = $results.records
$records.Length

$records6 = $records | Where-Object {$_.digits -eq 6}
$records6.Length

$recentRecords6 = $records6 | Where-Object {$_.update_date -gt '2020-03-20T17:11:03.504Z'}

$recentRecords6.Length

$recentRecords6 | Sort-Object -Property update_date > ./recentRecords6.txt

