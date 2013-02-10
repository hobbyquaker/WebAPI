# HomeMatic WebAPI Addon

API zum Ausführen von Scripten, Prozessen, HTTP-POST-Requests und XML RPC Calls sowie zum Upload von Dateien auf der HomeMatic CCU, speziell auf die Anforderungen von Web-Anwendungen ausgelegt.

Die WebAPI steht in zwei Varianten zur Verfügung, einmal mit Authentifizierung (webapi_auth.tar.gz), einmal ohne (webapi.tar.gz).

Achtung: Eine Installation der WebAPI ohne Authentifizierung eröffnet jedem der Port 80 (http) bzw 443 (https) erreichen kann die Möglichkeit Scripte auf der HomeMatic CCU auszuführen. (Sicherheit ähnlich wie bei der "XML API")


## Dokumentation
Alle Scripte senden den HTTP-Header "Access-Control-Allow-Origin: *" - d.h. die Scripte können ohne Beschränkungen durch die "Same Origin Policy" von jedem Browser per XHR aufgerufen werden.



### hmscript.cgi
Erwartet das Homematic Script als POST Daten und gibt die Script-Ausgabe zurück

#### Paramter (Querystring)
* content - das Ausgabeformat (xml/json/html/plain) - Diese Angabe dient lediglich dazu einen passenden Header und passende Fehlermeldungen zu erzeugen, die Ausgabe selbst muss im TCL Script eigenständig erzeugt werden.
* debug - true/false - erzeugt eine Ausgabe die alle Variablen enthält (ähnlich Remote Script via Port 8181)
* session (nur in Variante mit Authentifizierung)


### process.cgi
Startet beliebige Prozesse auf der CCU, übergibt die POST-Daten als STDIN und gibt STDOUT zurück.  
Durch Umleiten der Ausgabe/Eingabe lassen sich hiermit auch Dateien auf der CCU lesen oder schreiben.

#### Paramter
* content - das Ausgabeformat (xml/json/html/plain) - Diese Angabe dient lediglich dazu einen passenden Header und passende Fehlermeldungen zu erzeugen, die Ausgabe selbst muss im TCL Script eigenständig erzeugt werden.
* debug - true/false - erzeugt eine Ausgabe die auch STDERR enthält
* session (nur in Variante mit Authentifizierung)


### tclscript.cgi
Erwartet das TCL Script als POST Daten und gibt die Script-Ausgabe zurück

#### Paramter (Querystring)
* content - das Ausgabeformat (xml/json/html/plain) - Diese Angabe dient lediglich dazu einen passenden Header und passende Fehlermeldungen zu erzeugen, die Ausgabe selbst muss im TCL Script eigenständig erzeugt werden.
* session (nur in Variante mit Authentifizierung)

### upload.cgi
Dient dazu Dateien per HTTP POST auf die CCU hochzuladen. 
Siehe auch upload-test.html

#### Paramater (Querystring)
* path - der Pfad wo die Datei abgelegt werden soll (mit abschließendem Slash!)
* overwrite - true/false - Wenn Du true werden evtl. vorhandene Dateien überschrieben
* session (nur in Variante mit Authentifizierung)
#### Parameter (POST)
* file - der Dateiupload 


### version.cgi
Gibt die Version und die Variante (mit oder ohne Authentifizierung) im JSON Format zurück

### xmlrpc.cgi
Dient als Proxy um XML RPC via Port 80 bzw 443 ausführen zu können. 
#### Paramater (Querystring)
* port - der Zielport (2000/2001/2002)
* session (nur in Variante mit Authentifizierung)


### proxy.cgi
Dient dazu unter Umgehung der "Same Origin Policy" (ein Sicherheitsmerkmal moderner Browser) XHR POST Requests an beliebige URLs zu stellen.  
Querystring und POST-Daten werden unverändert durchgereicht.

#### Paramter (Querystring)
* hmwa_url - die Aufzurufende URL
* hmwa_session (nur in Variante mit Authentifizierung)

### login.cgi
(nur in Variante mit Authentifizierung vorhanden)

Eine Session eröffnen. Gibt die Session-ID zurück

#### Paramter (POST)
* username 
* password

### logout.cgi
(nur in Variante mit Authentifizierung vorhanden)

Beendet eine Session

#### Parameter (Querystring)
* session

### renew.cgi
(nur in Variante mit Authentifizierung vorhanden)

Erneuert eine Session. Sollte in Intervallen kürzer als der in der CCU konfigurierte Session-Timeout aufgerufen werden
#### Parameter (Querystring)
* session


## Lizenz

Die Nutzung dieser Software erfolgt auf eigenes Risiko. Der Author dieser Software kann für eventuell auftretende Folgeschäden nicht haftbar gemacht werden!

© 2012, 2013 hobbyquaker https://github.com/hobbyquaker

Diese Software ist freie Software. Sie können sie unter den Bedingungen der GNU General Public License, wie von der Free Software Foundation veröffentlicht, weitergeben und/oder modifizieren, gemäß Version 3 der Lizenz. Die Veröffentlichung dieser Software erfolgt in der Hoffnung, daß sie Ihnen von Nutzen sein wird, aber OHNE IRGENDEINE GARANTIE, sogar ohne die implizite Garantie der MARKTREIFE oder der VERWENDBARKEIT FÜR EINEN BESTIMMTEN ZWECK. Details finden Sie in der GNU General Public License.

HomeMatic und das HomeMatic Logo sind eingetragene Warenzeichen der eQ-3 AG




