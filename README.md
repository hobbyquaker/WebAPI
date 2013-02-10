# WebAPI

HomeMatic Addon

API zum Ausf�hren von Scripten, Prozessen, HTTP-POST-Requests und XML RPC Calls sowie zum Upload von Dateien auf der HomeMatic CCU, speziell auf die Anforderungen von Web-Anwendungen ausgelegt.

Die WebAPI steht in zwei Varianten zur Verf�gung, einmal mit Authentifizierung (webapi_auth.tar.gz), einmal ohne (webapi.tar.gz).

Achtung: Eine Installation der WebAPI ohne Authentifizierung er�ffnet jedem der Port 80 (http) bzw 443 (https) erreichen kann die M�glichkeit Scripte auf der HomeMatic CCU auszuf�hren. (Sicherheit �hnlich wie bei der "XML API")


## Dokumentation
Alle Scripte senden den HTTP-Header "Access-Control-Allow-Origin: *" - d.h. die Scripte k�nnen ohne Beschr�nkungen durch die "Same Origin Policy" von jedem Browser per XHR aufgerufen werden.



### hmscript.cgi
Dient dazu Homematic-Script auszuführen  

Erwartet das Ausgabeformat im Querystring sowie ein Homematic Script als POST Daten
M�gliche Ausgabeformate: xml, json, html, plain
Diese Angabe dient lediglich dazu einen passenden Header und passende Fehlermeldungen zu erzeugen, die Ausgabe selbst muss im TCL Script eigenst�ndig erzeugt werden.
Beispielaufruf:
  hmscript.cgi?content=json

Debug-Modus: ein Aufruf mit
  hmscript.cgi?debug=true
erzeugt eine Ausgabe die alle Variablen beinhaltet

### process.cgi
Erwartet den Prozess und das Ausgabeformat im Querystring sowie STDIN als POST Daten
M�gliche Ausgabeformate: xml, json, html, plain
Diese Angabe dient lediglich dazu einen passenden Header und passende Fehlermeldungen zu erzeugen, die Ausgabe selbst muss im TCL Script eigenst�ndig erzeugt werden.
Beispielaufruf:
  process.cgi?content=plain&process=/bin/sh
Debug-Modus: ein Aufruf mit
  process.cgi?debug=true
erzeugt eine Ausgabe die auch STDERR enth�lt

### tclscript.cgi

### upload.cgi

### version.cgi
 
### xmlrpc.cgi

### proxy.cgi

### login.cgi
(nur in Variante mit Authentifizierung vorhanden)

### logout.cgi
(nur in Variante mit Authentifizierung vorhanden)

### renew.cgi
(nur in Variante mit Authentifizierung vorhanden)




Die Nutzung dieser Software erfolgt auf eigenes Risiko. Der Author dieser Software kann für eventuell auftretende Folgeschäden nicht haftbar gemacht werden!

(c) 2012, 2013 hobbyquaker https://github.com/hobbyquaker

Diese Software ist freie Software. Sie können sie unter den Bedingungen der GNU General Public License, wie von der Free Software Foundation ver�ffentlicht, weitergeben und/oder modifizieren, gemäß Version 3 der Lizenz. Die Ver�öfentlichung dieser Software erfolgt in der Hoffnung, da� ßie Ihnen von Nutzen sein wird, aber OHNE IRGENDEINE GARANTIE, sogar ohne die implizite Garantie der MARKTREIFE oder der VERWENDBARKEIT F�R ÜINEN BESTIMMTEN ZWECK. Details finden Sie in der GNU General Public License.

HomeMatic und das HomeMatic Logo sind eingetragene Warenzeichen der eQ-3 AG




