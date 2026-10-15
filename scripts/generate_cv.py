"""Genera el CV desde el contenido del portfolio. Requiere reportlab."""
from pathlib import Path
from html import escape
from urllib.parse import unquote

from html.parser import HTMLParser
from xml.etree.ElementTree import Element, SubElement


class HTMLTree(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = Element("document")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = SubElement(self.stack[-1], tag, {k: v or "" for k, v in attrs})
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        node = self.stack[-1]
        if len(node):
            node[-1].tail = (node[-1].tail or "") + data
        else:
            node.text = (node.text or "") + data

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import SimpleDocTemplate, Paragraph, KeepTogether, Image, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/pdf/Sebastian-Fernandez-CV.pdf"
parser = HTMLTree()
parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))
soup = parser.root
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

styles = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=24, leading=28, spaceAfter=5),
    "role": ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=11, leading=15, textColor=colors.HexColor("#922331"), spaceAfter=7),
    "section": ParagraphStyle("section", fontName="Helvetica-Bold", fontSize=11, leading=14, spaceBefore=7, spaceAfter=5, textColor=colors.HexColor("#922331")),
    "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=10, leading=13, spaceAfter=4),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9, leading=11, spaceAfter=2, alignment=TA_LEFT),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=8, leading=11, spaceAfter=3),
}


def text(node):
    return " ".join(" ".join(node.itertext()).split())


def para(value, kind="body"):
    return Paragraph(escape(value), styles[kind])


story = [para(text(soup.find(".//h1")), "name"), para(text(soup.find(".//div[@class='hero-copy']/p")), "role")]
for item in soup.findall(".//ul[@class='contact-list']/li"):
    label = text(item.find("span"))
    link = item.find("a")
    if link is not None:
        visible = unquote(link.attrib["href"]).removeprefix("mailto:").removeprefix("https://").rstrip("/")
        story.append(Paragraph(f'{escape(label)}: <link href="{escape(link.attrib["href"], quote=True)}">{escape(visible)}</link>', styles["contact"]))
    else:
        story.append(para(text(item).removeprefix(label).strip(), "contact"))

# El perfil aprovecha la columna izquierda mientras la foto y el QR ocupan la derecha.
story.append(para("Perfil profesional", "section"))
story.append(para(text(soup.find(".//*[@id='perfil']"))))
profile_image = soup.find(".//div[@class='frame frame-profile']/img")
photo = Image(str(ROOT / profile_image.attrib["src"]), width=108, height=108)
photo.hAlign = "CENTER"
portfolio_url = "https://pfo1-dsw-front.vercel.app/"
# QR vectorial con margen blanco para conservar la legibilidad al imprimir.
qr = QrCodeWidget(portfolio_url, barLevel="M", barBorder=4)
x0, y0, x1, y1 = qr.getBounds()
qr_size = 72
qr_image = Drawing(qr_size, qr_size, transform=[qr_size / (x1 - x0), 0, 0, qr_size / (y1 - y0), 0, 0])
qr_image.add(qr)
qr_image.hAlign = "CENTER"
qr_caption = Paragraph(f'<link href="{portfolio_url}">Portfolio online</link>',
                       ParagraphStyle("qr_caption", fontName="Helvetica-Bold", fontSize=9, leading=12, alignment=1,
                                      textColor=colors.HexColor("#922331")))
# Una única columna fija centra foto, QR y leyenda sobre el mismo eje.
profile_block = Table([[photo], [qr_image], [qr_caption]], colWidths=[112])
profile_block.setStyle(TableStyle([
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (0, 0), 4),
]))
header = Table([[story, profile_block]], colWidths=[A4[0] - 80 - 12 - 124, 124])
header.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ("LEFTPADDING", (1, 0), (1, 0), 12),
]))
story = [header]

story.append(para("Experiencia profesional", "section"))
experience = soup.find(".//*[@id='experiencia']//article")
story.append(para(text(experience.find("h3")), "title"))
for p in experience.findall("p"):
    story.append(para(text(p)))
for li in experience.findall(".//ul[@class='detail-list']/li"):
    story.append(para("- " + text(li)))

story.append(para("Competencias técnicas", "section"))
for card in soup.findall(".//*[@id='habilidades']//li[@class='card']"):
    if text(card.find("h3")) == "En exploración":
        continue
    names = [text(n) for n in card.findall(".//span[@class='skill-name']") if text(n) not in ("Herramientas de IA", "Inglés")]
    story.append(para(text(card.find("h3")) + ": " + ", ".join(names) + "."))

story.append(para("Proyectos destacados", "section"))
for project in soup.findall(".//*[@id='proyectos']//article"):
    block = [para(text(project.find("h3")), "title")]
    for p in project.findall("p"):
        if "project-state" not in p.get("class", "") and "project-link" not in p.get("class", ""):
            block.append(para(text(p)))
    link = project.find("a")
    if link is not None:
        block.append(Paragraph(f'<link href="{escape(link.attrib["href"], quote=True)}">{escape(link.attrib["href"])}</link>', styles["contact"]))
    story.append(KeepTogether(block))

story.append(para("Formación e idiomas", "section"))
education = soup.find(".//*[@id='formacion']//article")
story.append(para(text(education.find("h3")), "title"))
story.append(para(text(education.find("p[@class='education-institution']"))))
story.append(para(text(education.find("p[@class='experience-meta']"))))
story.append(para(text(education.findall("p")[-1])))

doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=40, leftMargin=40,
                        topMargin=32, bottomMargin=30, title="Sebastián Fernández - CV",
                        author="Sebastián Fernández")
doc.build(story)
print(OUTPUT)
