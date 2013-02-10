# WebAPI

HomeMatic Addon

API zum Ausführen von Scripten, Prozessen, HTTP-POST-Requests und XML RPC Calls sowie zum Upload von Dateien auf der HomeMatic CCU, speziell auf die Anforderungen von Web-Anwendungen ausgelegt.

Die WebAPI steht in zwei Varianten zur Verfügung, einmal mit Authentifizierung (webapi_auth.tar.gz), einmal ohne (webapi.tar.gz).

Achtung: Eine Installation der WebAPI ohne Authentifizierung eröffnet jedem der Port 80 (http) bzw 443 (https) erreichen kann die Möglichkeit Scripte auf der HomeMatic CCU auszuführen. (Sicherheit ähnlich wie bei der "XML API")


## Dokumentation
Alle Scripte senden den HTTP-Header "Access-Control-Allow-Origin: *" - d.h. die Scripte können ohne Beschränkungen durch die "Same Origin Policy" von jedem Browser per XHR aufgerufen werden.



### hmscript.cgi
Erwartet das Ausgabeformat im Querystring sowie ein Homematic Script als POST Daten
Mögliche Ausgabeformate: xml, json, html, plain
Diese Angabe dient lediglich dazu einen passenden Header und passende Fehlermeldungen zu erzeugen, die Ausgabe selbst muss im TCL Script eigenständig erzeugt werden.
Beispielaufruf:
  hmscript.cgi?content=json

Debug-Modus: ein Aufruf mit
  hmscript.cgi?debug=true
erzeugt eine Ausgabe die alle Variablen beinhaltet

### process.cgi
Erwartet den Prozess und das Ausgabeformat im Querystring sowie STDIN als POST Daten
Mögliche Ausgabeformate: xml, json, html, plain
Diese Angabe dient lediglich dazu einen passenden Header und passende Fehlermeldungen zu erzeugen, die Ausgabe selbst muss im TCL Script eigenständig erzeugt werden.
Beispielaufruf:
  process.cgi?content=plain&process=/bin/sh
Debug-Modus: ein Aufruf mit
  process.cgi?debug=true
erzeugt eine Ausgabe die auch STDERR enthält

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


## Lizenz

Die Nutzung dieser Software erfolgt auf eigenes Risiko. Der Author dieser Software kann für eventuell auftretende Folgeschäden nicht haftbar gemacht werden!

© 2012, 2013 hobbyquaker https://github.com/hobbyquaker

Diese Software ist freie Software. Sie können sie unter den Bedingungen der GNU General Public License, wie von der Free Software Foundation veröffentlicht, weitergeben und/oder modifizieren, gemäß Version 3 der Lizenz. Die Veröffentlichung dieser Software erfolgt in der Hoffnung, daß sie Ihnen von Nutzen sein wird, aber OHNE IRGENDEINE GARANTIE, sogar ohne die implizite Garantie der MARKTREIFE oder der VERWENDBARKEIT FÜR EINEN BESTIMMTEN ZWECK. Details finden Sie in der GNU General Public License.

HomeMatic und das HomeMatic Logo sind eingetragene Warenzeichen der eQ-3 AG




