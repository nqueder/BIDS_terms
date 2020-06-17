
from os import system
try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.pagesizes import landscape, portrait
    from reportlab.platypus import Image, SimpleDocTemplate, Paragraph, Spacer, Table, BaseDocTemplate, Frame, PageTemplate, PageBreak
    from reportlab.lib.units import inch, mm, cm
    from reportlab.lib.styles import StyleSheet1, ParagraphStyle, getSampleStyleSheet
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT, TA_CENTER
except ImportError:
    print("trying to install required module: reportlab")
    system('python -m pip install --upgrade pip reportlab')
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.pagesizes import landscape, portrait
    from reportlab.platypus import Image, SimpleDocTemplate, Paragraph, Spacer, Table, BaseDocTemplate, Frame, \
        PageTemplate, PageBreak
    from reportlab.lib.units import inch, mm, cm
    from reportlab.lib.styles import StyleSheet1, ParagraphStyle, getSampleStyleSheet
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT, TA_CENTER



def call_stylesheet():
    styles= {
        'default': ParagraphStyle(
            'default',
            fontName='Times-Roman',
            fontSize=10,
            leading=12,
            leftIndent=0,
            rightIndent=0,
            firstLineIndent=0,
            alignment=TA_LEFT,
            spaceBefore=0,
            spaceAfter=0,
            bulletFontName='Times-Roman',
            bulletFontSize=10,
            bulletIndent=0,
            textColor= colors.black,
            backColor=None,
            wordWrap=None,
            borderWidth= 0,
            borderPadding= 0,
            borderColor= None,
            borderRadius= None,
            allowWidows= 1,
            allowOrphans= 0,
            textTransform=None,  # 'uppercase' | 'lowercase' | None
            endDots=None,
            splitLongWords=1,
        ),
    }
    styles['subj'] = ParagraphStyle(
        'subj',
        parent=styles["default"],
        fontName='Helvetica',
        fontSize=12,
    )
    styles['alert'] = ParagraphStyle(
        'alert',
        parent=styles['default'],
        leading=14,
        backColor=colors.yellow,
        borderColor=colors.black,
        borderWidth=1,
        borderPadding=5,
        borderRadius=2,
        spaceBefore=10,
        spaceAfter=10,
    )
    return styles

def generate_pdf(term_dictionary,selected_properties,file_name):

    def header(canvas, c):
        canvas.saveState()

    c = BaseDocTemplate(file_name, pagesize=letter)
    frame = Frame(c.leftMargin, c.bottomMargin, c.width, c.height - 2 * mm, id='normal')
    template = PageTemplate(id='term_table', frames=frame, onPage=header)
    c.addPageTemplates([template])

    styles = getSampleStyleSheet()
    styles = call_stylesheet()

    story = []
    spacer = Spacer(1, 10*mm)


    # add table
    header = []
    cell = ['BIDS Terms']
    # header.append(cell)
    numberOfColumns = len(list(my_dict.keys())[0])
    for i in range(1,numberOfColumns):
        cell.append([''])
    header.append(cell)
    t = Table(header, colWidths=numberOfColumns*[(7.5/numberOfColumns)*inch],
              style=[('BOX', (0,0), (-1,-1), 0.25, colors.black),
                     ('SPAN', (0,0), (-1, 0)),
                     ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                     ('FONT', (0,0), (-1,0), 'Helvetica-Bold'),
                     ('BACKGROUND', (0,0), (-1,0), '#3498DB')
                     ])
    story.append(t)

    table_style= []
    for i, row in enumerate(data):
        if i%2==0:
            table_style.append(('BACKGROUND',(0,i), (-1,i), '#D6EAF8'))

    t = Table(data, repeatRows=1,
              colWidths=numberOfColumns * [(7.5 / numberOfColumns) * inch],
              style=[('BOX', (0,0), (-1,-1), 0.25, colors.black),
                     ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                     ('FONT', (0,0), (-1,0), 'Helvetica-Bold')
                     ])
    t.setStyle(table_style)
    story.append(t)
    # story.append(spacer)


    c.build(story)
