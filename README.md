# meinkitaplatz-leipzig to csv

Trotz der Vergabe der Kitaplätze über die Website, muss man oft alle Einrichtungen abtelefonieren. Es gibt jedoch keine eingebaute Möglichkeit des Datenexports.
Mit diesen einfachen Python Skript können die Informationen über Kindertageststätten im Leipziger Kivan-Tool https://www.meinkitaplatz-leipzig.de/ extrahiert und in eine CSV exportiert werden.

Beispiel: 

|einrichtungsname                                             |adresse                                    |ansprechpartner                      |telefonnummer       |traeger                                                     |
|-------------------------------------------------------------|-------------------------------------------|-------------------------------------|--------------------|------------------------------------------------------------|
|"Schöne Zwerge"                                                 |Schönestraße 10 04178 Leipzig                |Frau Jana Mustermann                       |0341/12345        |DRK Kreisverband Leipzig Land e.V.                          |
|"Schönes Kinderland"                                       |Schönestraße  65 04178 Leipzig          |Frau Yvonne Mustermann                |0341/12345       |Volkssolidarität Kreisverband Leipziger Land/Muldental e. V.|
|"Schöne Sternchen"                                           |Schönestraße 7-8 04158 Leipzig    |Frau Katrin Mustermann                     |0341/12345        |Volkssolidarität Kreisverband Leipziger Land/Muldental e. V.|


## Schritte

### 1. Fork des Repls auf Replit

https://replit.com/@KatharinaNi/meinkitaplatz-leipzig-to-csv

### 2. Download der HTML Dateien

Zuerst muss ich mich unter https://www.meinkitaplatz-leipzig.de/app/de/nutzerkonto einloggen und dann den Menüpunkt `Bedarfsanmeldung erstellen` auswählen. Dann ist es empfehlenswert Filter hinzuzufügen, wie z.B. Entfernung zum Wohnort, um die Zahl der Einrichtungen einzugrenzen. Das ist aber nicht notwendig.

Die HTML-Dateien der einzelnen Unter-Seiten (unten rechts 1, 2, 3, 4, 5 usw) müssen bei der aktuellen Programmversion manuell heruntergelanden werden. Dazu nutze ich die Chrome Extension `Save Page WE` : https://chrome.google.com/webstore/detail/save-page-we/dhhpefjklgkmgeafimnjhojgjamoafof

### Upload der HTML Dateien auf Replit in den Ordner `download`

![alt text](/examples/download_folder_example.png)

### Anpassung der Variable `local_file_list` in `main.py` an die Anzahl und Bezeichnung der html-dateien im Ordner `download`

```
local_file_list = [
        "download/Kivan - Elternportal.html",
        "download/Kivan - Elternportal (1).html",
				"download/Kivan - Elternportal (2).html"]
```

### Ausführen des Programms

In Replit wird das Programm mit `Run` ausgeführt und anschließend kann die Datei `kita_daten_uebersicht.csv` heruntergeladen werden.

## Author

[k4th4]([https://github.com/k4th4])



## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details



