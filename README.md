# Prozess & Wirkung

Statische, öffentlich zugängliche Vergleichsseite für eine Praxistransferarbeit. 31 eigenständig formulierte Fragen, 124 literaturbasierte Fallantworten, zwei PDF-Ausgaben und CSV/JSON-Exporte.

## Erzeugen und prüfen

`python content.py` erzeugt den Datensatz und die Exporte.
`python documents.py` erzeugt PDFs (ReportLab, pypdf und DejaVu-Schriften erforderlich).
`node checks.cjs` prüft Datenintegrität und die Bewertungsformel.

`dist/` enthält die vollständige statische Seite. Keine Installation von Frontend-Paketen erforderlich.

## Methodische Abgrenzung

Die Quellenstände der bereitgestellten Bücher werden ausgewertet. Unternehmensmesswerte werden nicht erfunden. Die Fälle sind hinsichtlich Zweck und Bezugsgröße heterogen, daher gibt es keinen gemeinsamen Nachhaltigkeitsindex. Zahlen, qualitative Hinweise, Planungen und fehlende Informationen werden getrennt dargestellt. Reifegradstufen und Gewichtungsregeln sind eigene methodische Vorschläge. Quellenstellen stehen in jedem Datensatz.

Die urheberrechtlich geschützten Bücher sind nicht Bestandteil dieses Repositorys.

Version 1.1 präzisiert Wasser/Trinkwasser/Abwasser (O5) und ergänzt Luftqualität (O7) sowie Flächennutzung (O8). Die Flächenangabe bei Mercedes-Benz ist ein Modellhinweis, keine vollständige Bilanz. Die Ökologie umfasst acht Kriterien; Ökonomie und Soziales je sechs. Die Dimensionen behalten im vorgeschlagenen Gesamtindex je ein Drittel Gewicht.
