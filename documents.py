import json
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak,KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4,landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader
R=Path(__file__).parent;O=R/'dist/downloads';D=json.loads((R/'dist/data.json').read_text())
for n,f in [('Body','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf'),('Display','DejaVuSerif.ttf')]:pdfmetrics.registerFont(TTFont(n,'/usr/share/fonts/truetype/dejavu/'+f))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Body',boldItalic='Bold')
INK=colors.HexColor('#173d31');MUTED=colors.HexColor('#667260');LINE=colors.HexColor('#dbe2d3');PALE=colors.HexColor('#edf2e7')
S={k:ParagraphStyle(k,fontName=f,fontSize=z,leading=l,textColor=c,spaceAfter=a,spaceBefore=b) for k,f,z,l,c,a,b in [('title','Display',25,31,INK,12,0),('h1','Display',20,26,INK,12,0),('h2','Bold',12,17,INK,8,12),('body','Body',9,13,INK,7,0),('small','Body',7.5,10.5,MUTED,4,0),('cell','Body',8.2,11.7,INK,4,0),('head','Bold',9,12,INK,3,0),('eyebrow','Bold',8,11,MUTED,9,0)]}
S['h1'].keepWithNext=True
S['h2'].keepWithNext=True
def clean(t):return str(t).replace('–','-').replace('—','-').replace('−','-').replace('\u00ad','')
def tx(t):return escape(clean(t))
def p(t,s='body'):return Paragraph(clean(t),S[s])
def footer(c,d):
 w,h=d.pagesize;c.saveState();c.setStrokeColor(LINE);c.line(32,29,w-32,29);c.setFont('Body',7);c.setFillColor(MUTED);c.drawString(32,17,'PROZESS & WIRKUNG  |  Praxistransfer Nachhaltigkeit  |  Version 1.1 · 16.11.2026');c.drawRightString(w-32,17,str(d.page));c.restoreState()
def document(name,size=A4):return SimpleDocTemplate(str(O/name),pagesize=size,leftMargin=33,rightMargin=33,topMargin=30,bottomMargin=39,title='Nachhaltigkeit im Prozessvergleich',author='Praxistransfer Wirtschaftsingenieurwesen')
def table(rows,widths,compact=False):
 pad=5 if compact else 8
 t=Table(rows,colWidths=widths,repeatRows=1,hAlign='LEFT');t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),pad),('BOTTOMPADDING',(0,0),(-1,-1),pad),('LINEBELOW',(0,0),(-1,-1),.4,LINE),('BACKGROUND',(0,0),(-1,0),PALE)]));return t
F=[p('VERGLEICHSBLATT / VIER LITERATURBEISPIELE','eyebrow'),p('Vier Fälle. Ein Fragenkatalog.','title'),p('31 Fragen: 5 Kontext + 20 Wirkung + 6 Management. Alle 124 Antworten stehen im Gesamtdokument. Die Fälle unterscheiden sich in Zweck und Bezugsgröße; dies ist kein Nachhaltigkeitsranking.')]
rows=[[p('Kriterium','head')]+[p(c['name'],'head') for c in D['cases']]]
lines=[('Falltyp',['Digitale Produktion und Verwaltung','Brennstoffzellen-Pilot + Modell','Berichte von vier Hörgeräteherstellern','Konzept für Softwareprojekte']),('Ökologisch',['Keine Umweltmesswerte; Trink-/Abwasser, Luftschadstoffe und Flächennutzung offen.','CO₂ modellabhängig; Wärme/Lärm qualitativ verbessert. Pumpenfläche < 1 m² im Modell; Gesamtfläche, Trink-/Abwasser und Luftschadstoffe offen.','Keine Umweltbilanz; Trink-/Abwasser, Luftschadstoffe und Flächennutzung offen.','Keine Umweltmesswerte; Trink-/Abwasser, Luftschadstoffe und Flächennutzung offen.']),('Ökonomisch',['QCD, Engpässe und Wartung werden gesteuert; Vor-/Nachher-Werte fehlen.','Betankung 8 min; Ziel 3-5 min. Ausfälle und getrennte Wartung beschrieben.','Keine vergleichbaren Prozesskosten im ausgewerteten Abschnitt.','Keine Kosten-/Nutzenmessung; zusätzlicher Rollen-/Reviewaufwand offen.']),('Sozial',['Schulung und Beteiligung beschrieben; Belastungswirkung nicht gemessen.','Fahrer beteiligt; Wärme/Lärm reduziert, Belastungswerte fehlen.','Sonova: 270 geschult, Ziel 250. Output und Wirkung werden unterschieden.','Gemeinsame Zielvereinbarung vorgesehen; Teamwirkung noch zu prüfen.']),('Management',['PDCA und externes ADEX-Assessment; Umwelt-/Sozialziele offen.','Pilotmessung und Anpassungen; Modellvorteile weiter zu bestätigen.','Berichte, Ziele und Wirkmodelle; Datenqualität herstellerweise prüfen.','Controller, Backlog und Review vorgeschlagen; logische Evaluation.']),('Nächster Nachweis',['Einen Prozess mit Ist-/Soll-Messung abgrenzen.','Gleiche Transportleistung, Vorketten, Kosten und Verfügbarkeit messen.','Hersteller trennen; Nutzerwirkung empirisch prüfen.','Pilot durchführen; Aufwand und Wirkung messen.']),('Quelle / PDF',['L, Kap. 6.7, 119-127','E, Kap. 6.4, 89-91','C, Kap. 9.4, 144-149','C, Kap. 10, 164-171'])]
for title,v in lines:rows.append([p(title,'head')]+[p(tx(x),'cell') for x in v])
F+=[table(rows,[87]+[172.2]*4,compact=True),Spacer(1,8),p('<b>Berechenbare Einzelbefunde:</b> Mercedes: (8 - 5) / 5 = <b>60 % über der oberen Zeit-Zielgrenze</b>. Sonova: (270 - 250) / 250 = <b>8 % über dem Schulungsziel</b>. Unterschiedliche Kennzahlen; kein gemeinsamer Index.'),p('<b>Quellen:</b> L = Reichert, Lean & Green: Best Practice, DOI 10.1007/978-3-658-47806-3. E = Krauss/Plugmann (Hrsg.), Nachhaltigkeit ermöglichen, DOI 10.1007/978-3-658-44832-5. C = Weber/Hastenteufel (Hrsg.), Nachhaltigkeit im Controlling, DOI 10.1007/978-3-658-45769-3. Buchstände, keine aktuellen Unternehmensauskünfte.','small')]
document('vergleich.pdf',landscape(A4)).build(F,onFirstPage=footer,onLaterPages=footer)
F=[p('FRAGENKATALOG / FALLANWENDUNGEN / BEWERTUNG','eyebrow'),p('Nachhaltigkeit im<br/>Prozessvergleich','title'),p('Arbeitsinstrument für die Praxistransferarbeit','h2'),p('31 eigenständig formulierte Fragen, 124 dokumentierte Fallantworten und ein transparenter Bewertungsrahmen. Grundlage sind sechs bereitgestellte Fachbücher. Alle Seitenangaben beziehen sich auf die PDF-Zählung.'),p('Zweck und Ergebnis','h2'),p(tx(D['method']['scope'])),p(tx(D['method']['limits'])),p('Bei jeder Frage stehen Antwortformat, Bewertungsregel und Quelle. Jede Fallanwendung dokumentiert auch fehlende Informationen. Qualitative Hinweise können eine Frage teilweise betreffen, ohne sie vollständig zu beantworten. Fehlende Unternehmensmesswerte wurden nicht erfunden.'),p('Zwei konkrete Ergebnisse','h2'),p('<b>Mercedes-Benz:</b> Betankung 8 Minuten, Ziel 3-5 Minuten. Gegenüber der oberen Zielgrenze: +3 Minuten bzw. +60 %. Für den Vergleich mit Batteriefahrzeugen fehlt deren Wechselzeit.'),p('<b>Sonova:</b> 270 ausgebildete Akustiker bei Ziel 250 in zwei berichteten Geschäftsjahren: +20 Personen bzw. +8 %. Das ist ein Schulungsoutput; eine verbesserte Versorgung benötigt einen gesonderten Nachweis.'),p('Aufbau','h2'),p('1. Bewertungsregeln<br/>2. Katalog: Kontext, Ökologie, Ökonomie, Soziales, Management<br/>3. Vier vollständige Fallanwendungen<br/>4. Literatur und Grenzen'),PageBreak()]
F+=[p('1. Bewertungsregeln','h1'),p('Erweiterung in Version 1.1','h2'),p(tx(D['method']['revision'])),p('Antworten und Belegstand','h2'),p(tx(D['method']['coverage']))]
meanings={'num':'Konkrete Zahl berichtet; nicht automatisch umfassende Wirkung.','qual':'Vorgehen oder Beobachtung beschrieben; quantitative oder kausale Antwort teilweise offen.','plan':'Ziel, Erwartung, Modell oder Konzept; kein erreichtes Ergebnis.','gap':'Im ausgewerteten Abschnitt nicht ausreichend angegeben.','context':'Rahmenbedingungen; eigene Vorschläge ausdrücklich gekennzeichnet.'}
for k,v in D['method']['status'].items():F.append(p('<b>'+tx(v)+':</b> '+tx(meanings[k])))
for title,key in [('Skalierung künftiger Messdaten','scoring'),('Aggregation und Freigabe','aggregation'),('Fehlende Werte','missing'),('Managementreife separat','grade')]:F.extend([p(title,'h2'),p(tx(D['method'][key]))])
F+=[p('Vor praktischem Einsatz: fachliche Prüfung der Kriterien, Verständlichkeitstest mit Nutzern, operationalisierte Messgrößen und Pilot an einem realen Prozess. 80-%-Schwelle und Gleichgewichtung sind eigene Arbeitsfestlegungen, keine wissenschaftlich validierten Schwellen.'),PageBreak()]
for dim in ['Kontext','Ökologisch','Ökonomisch','Sozial','Management']:
 F.append(p('2. Fragenkatalog / '+dim,'h1'));rows=[[p('Frage','head'),p('Antwortformat, Bewertung und Quelle','head')]]
 for q in D['questions']:
  if q['dimension']==dim:rows.append([p('<b>'+q['id']+' · '+tx(q['topic'])+'</b><br/>'+tx(q['text']),'cell'),[p('<b>Antwort:</b> '+tx(q['format']),'cell'),p('<b>Bewertung:</b> '+tx(q['rule']),'cell'),p('Ableitung: '+tx(q['source'])+' | Eigene Formulierung.','small')]])
 F+=[table(rows,[185,344.28]),PageBreak()]
for c in D['cases']:
 F.extend([p('3. Anwendung / '+c['name'],'h1'),p(tx(c['kind']+' · '+c['subtitle']),'eyebrow'),p(tx(c['summary'])),p('<b>Ergebnis:</b> '+tx(c['takeaway'])),p('<b>Nächster Nachweis:</b> '+tx(c['next'])),p('Ausgewertet: '+tx(c['source']),'small')])
 for dim in ['Kontext','Ökologisch','Ökonomisch','Sozial','Management']:
  F.append(p(dim,'h2'));rows=[[p('Frage','head'),p('Anwendung und fehlender Nachweis','head')]]
  for q in D['questions']:
   if q['dimension']!=dim:continue
   a=D['answers'][c['id']][q['id']];g='' if a['grade'] is None else f' | Reifegrad {a["grade"]}/3 (eigene Einordnung)'
   v=[p('<b>'+tx(D['method']['status'][a['status']]+g)+'</b>','cell'),p(tx(a['text']),'cell')]
   if a['missing']:v.append(p('<b>Noch erforderlich:</b> '+tx(a['missing']),'cell'))
   v.append(p('Beleg: '+tx(a['ref']),'small'));rows.append([p('<b>'+q['id']+' · '+tx(q['topic'])+'</b><br/>'+tx(q['text']),'cell'),v])
  F.extend([table(rows,[160,369.28]),Spacer(1,10)])
 F.append(PageBreak())
F.extend([p('4. Literatur und Herkunft','h1'),p('Verwendet wurden Inhaltsverzeichnisse und relevante Methoden-, Fragen- und Fallkapitel der bereitgestellten Ausgaben. Keine aktuelle Vollprüfung der genannten Unternehmen. Fragen sind eigene Ableitungen; Fallantworten sind Zusammenfassungen und methodische Einordnungen.')])
for s in D['sources']:F.extend([p(s['id']+' · '+tx(s['title']),'h2'),p(tx(s['author']+'. '+s['use']),'small'),p('<link href="https://doi.org/'+s['doi']+'" color="#155b45">https://doi.org/'+s['doi']+'</link>','small')])
F.extend([p('Grenzen und Weiterentwicklung','h2'),p('Der Katalog trennt Prozesswirkung, Kontext und Management. Für eine belastbare Praxistransferarbeit sind Kriterienwahl, Bewertungsanker, Datenerhebung und Pilotresultate zu begründen. Unterschiedliche Bezugsgrößen verhindern hier einen gemeinsamen Nachhaltigkeitsindex.'),p('Die Hörgerätebranche ist ein Sammelfall; einzelne Resultate sind dem jeweiligen Hersteller zugeordnet. SustainableScrum ist ein Konzept. Mercedes-Benz verbindet Modellannahmen und Pilotbeobachtungen. Festo beschreibt vor allem Prozesssteuerung. Diese Ebenen dürfen nicht als gleichartige Wirkungsnachweise behandelt werden.'),p('Weitere Dateien: vergleich.pdf (eine Seite), fragenkatalog.csv (31 Fragen), fallanwendungen.csv (124 Antworten), data.json (Gesamtdaten).','small')])
document('fragenkatalog-und-fallanwendungen.pdf').build(F,onFirstPage=footer,onLaterPages=footer)
for f in ['vergleich.pdf','fragenkatalog-und-fallanwendungen.pdf']:
 n=len(PdfReader(O/f).pages);print(f,n,'Seiten')
 if f=='vergleich.pdf':assert n==1
