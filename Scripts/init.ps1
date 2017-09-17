Set-Location -Path .. -PassThru

$cloneParams = "clone -v https://github.com/Stropek/KattisPythonTemplate.git " +  "Python/" + $args[0]
Start-Process git -ArgumentList $cloneParams -wait -NoNewWindow -PassThru

$expression = ".\Python\projectSetup.ps1 " + $args[0]
Invoke-Expression $expression