$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$uri = "https://website.com"
$corsSource = "https://someothersite.com"
$session.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"

Invoke-WebRequest -UseBasicParsing -Uri $uri `
-Method "POST" `
-WebSession $session `
-Headers @{
  "Referer"=$corsSource  #not strictly Necessary
  "Origin"=$corsSource #This is the important bit
} 