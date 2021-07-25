[CmdletBinding()]
param (

    [Parameter(Mandatory=$true)]
    [Alias("Comp","ComputerName")]
    [String[]]$Computer,

    [int]$MaxCount = -1,

    [int]$MaxHops = 10

)

$count = 0

While ($count -ne $MaxCount) {
    Write-Host "Testing $($Computer.Count) Connections at $(Get-Date)"
    Write-Verbose "Test Count $Count of $MaxCount"

    foreach ($c in $Computer) {
        $result = Test-Connection $c -Quiet -Count 1

        if (!$result) {
            Write-Host $c -ForegroundColor Red
            tracert -d -w 100 -h $MaxHops $c
        } else {
            Write-Verbose "$c Successful"
        }
    }
    $count++
    Write-Host "Sleeping Until Next Run"
    Sleep -Seconds 60
}
