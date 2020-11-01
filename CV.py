import tkinter as tk
import webbrowser
import cvimages as cvi

font = "Cambria"  # Font
col1 = "#008784"  # General background & buttons
col2 = "#191919"  # Menu & text boxes
col3 = "white"    # Titles
col4 = "white"    # Text

window = tk.Tk()
window.iconphoto(False, tk.PhotoImage(data=cvi.icon_string))
window.resizable(False, False)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)

#-----------------------------------CLEAR FRAMES------------------------------------------------------
def clear_frame():
    frame_info.destroy()
    create_frame_info()

#-----------------------------------PROFILE-----------------------------------------------------------
def display_profile(start=1):
    if start == 1: 
        clear_frame()
    display_title("Mart Groenen")
   
    # Upper part of profile page
    frame_desc = tk.Frame(master=frame_info, relief=tk.SUNKEN, borderwidth=7, bg=col2)
    frame_desc.grid(column=0, row=0, sticky="news")

    img_frame = tk.Frame(master=frame_desc, relief=tk.RAISED, borderwidth=3, bg=col2)
    img_frame.grid(column=1, row=0, sticky="e")
    
    # Lower part of profile page
    frame_desc2 = tk.Frame(master=frame_info, bg=col1)
    frame_desc2.grid(column=0, row=1, sticky="news", pady=(10,0))
    frame_desc2.columnconfigure([0, 1, 2], weight=1, minsize=240)
    
    global img
    canvas = tk.Canvas(master=img_frame, width=250, height=250, bg=col2)
    canvas.grid(column=0, row=0, sticky="e")
    img = tk.PhotoImage(data=cvi.pasfoto_string)
    canvas.create_image(0,0, image=img, anchor="nw")
    
    if language == 0: # Dutch
        description = tk.Label(master=frame_desc, text="  Ik heb al mijn hele leven passie voor IT. Daarnaast ben\n  ik een rasechte analist en onderzoeker die zich graag\n  verder wil ontwikkelen in de wereld van data.\n\n  Een grote drijfveer van mij is de kans om \n  verantwoordelijkheid te dragen. Ik hoop dan ook in\n  een rol terecht te komen waar ik de kans krijg om\n  een echte bijdrage te leveren.",
                               font=(font, 15), bg=col2, fg=col4, justify="left")

        # Hobby section
        frame_hobby = tk.Frame(master=frame_desc2, relief=tk.SUNKEN, borderwidth=7, bg=col2)
        label_hobby = tk.Label(master=frame_hobby, text="Hobby's:\n  - Scouting\n  - Literatuur\n  - Gaming",
                              font=(font, 15), bg=col2, fg=col4, justify="left")

        # Languages section
        frame_langs = tk.Frame(master=frame_desc2, relief=tk.SUNKEN, borderwidth=7, bg=col2)
        label_langs = tk.Label(master=frame_langs, text="Talen:\n  - Nederlands (moedertaal)\n  - Engels (vloeiend)\n  - Duits (basis)",
                              font=(font, 15), bg=col2, fg=col4, justify="left")

        # Driver's license section
        frame_driver = tk.Frame(master=frame_desc2, relief=tk.SUNKEN, borderwidth=7, bg=col2)
        label_driver = tk.Label(master=frame_driver, text="Rijbewijs:\n  - B (auto)",
                               font=(font, 15), bg=col2, fg=col4, justify="left")

        # Instruction
        frame_instruction = tk.Frame(master=frame_info, bg=col2, relief=tk.RAISED, borderwidth=7)
        label_instruction = tk.Label(master=frame_instruction, text="Gebruik de knoppen in het menu aan de linkerkant om de verschillende\nonderdelen van mijn CV te bekijken.",
                                    font=(font, 15, "bold"), bg=col2, fg=col4, justify="center")
        
    if language == 1: # English
        description = tk.Label(master=frame_desc, text="  I have had a passion for IT for my whole life. I am an   \n  analyst and researcher at heart and someone who \n  would love to develop his skills in the world of data.\n\n  I am especially motived by the opportunity \n  to bear responsibility. For this reason, I hope to end\n  up in a role where I can provide a real contribution.",
                               font=(font, 15), bg=col2, fg=col4, justify="left")

        # Hobby section
        frame_hobby = tk.Frame(master=frame_desc2, relief=tk.SUNKEN, borderwidth=7, bg=col2)
        label_hobby = tk.Label(master=frame_hobby, text="Hobbies:\n  - Scouting\n  - Literature\n  - Gaming",
                              font=(font, 15), bg=col2, fg=col4, justify="left")

        # Languages section
        frame_langs = tk.Frame(master=frame_desc2, relief=tk.SUNKEN, borderwidth=7, bg=col2)
        label_langs = tk.Label(master=frame_langs, text="Talen:\n  - Dutch (native)\n  - English (fluent)\n  - German (basic)",
                              font=(font, 15), bg=col2, fg=col4, justify="left")

        # Driver's license section
        frame_driver = tk.Frame(master=frame_desc2, relief=tk.SUNKEN, borderwidth=7, bg=col2)
        label_driver = tk.Label(master=frame_driver, text="Driving license:\n  - B (automobile)",
                               font=(font, 15), bg=col2, fg=col4, justify="left")

        # Instruction
        frame_instruction = tk.Frame(master=frame_info, bg=col2, relief=tk.RAISED, borderwidth=7)
        label_instruction = tk.Label(master=frame_instruction, text="Use the buttons in the menu on the left to view the different\nsections of my resume.",
                                    font=(font, 15, "bold"), fg=col4, bg=col2, justify="center")
        
    # Grids
    description.grid(column=0, row=0)
    frame_hobby.grid(column=0, row=0, sticky="news")
    label_hobby.grid(column=0, row=0, pady=(5,5))
    frame_langs.grid(column=1, row=0, sticky="news")
    label_langs.grid(column=0, row=0, pady=(5,5))
    frame_driver.grid(column=2, row=0, sticky="news")
    label_driver.grid(column=0, row=0, pady=(5,5))
    frame_instruction.grid(column=0, row=2, pady=(100,0))
    label_instruction.grid(column=0, row=0, padx=10, pady=10)
    
    # Page memorizer (for switching language)
    global last_pressed
    last_pressed = display_profile

#-----------------------------------EDUCATION---------------------------------------------------------
def display_education():
    clear_frame()
    
    if language == 0: # Dutch
        display_title("Opleiding")
        programmes = ["Political Science, International Relations (MSc.)", "Politicologie (BSc.)", 
                      "VWO"]
        dates = ["september 2017 - november 2018", "september 2014 - augustus 2017", 
                 "september 2006 - augustus 2013"]
        schools = ["Radboud University, Nijmegen", "Radboud University, Nijmegen", 
                   "Rythovius College, Eersel"]
        notes = ["\t- WO-master, gespecialiseerd in internationale betrekkingen \n\t   en gericht op kwantitatieve onderzoeksmethoden.", 
             "\t- Brede WO-bachelor, raakvlakken met o.a.: sociologie, recht,\n\t  economie, \
filosofie, psychologie en geschiedenis.\n         \t- Minor: Conflictstudies (CICAM)", 
             "\t -Profiel: Natuur en Gezondheid (N&G)\n\t- Keuzevak: Geschiedenis"]
        
    if language == 1: # English
        display_title("Education")
        programmes = ["Political Science, International Relations (MSc.)", 
                      "Political Science (BSc.)", "VWO"]
        dates = ["september 2017 - november 2018", "september 2014 - august 2017", 
                 "september 2006 - august 2013"]
        schools = ["Radboud Universiteit, Nijmegen", "Radboud Universiteit, Nijmegen", 
                   "Rythovius College, Eersel"]
        notes = ["\t- Master of Science, specialized in international relations \n\t   with a focus on quantitative research methods.", 
             "\t- Bachelor of Science, intersecting with: sociology, law,\n\t  economy, \
philosophy, psychology and history.\n         \t- Minor: Conflict Studies (CICAM)", 
             "\t -Profiel: Nature and Health (N&G)\n\t- Elective: History"]
    
    # Create content
    for i in range(len(programmes)):
        frame = tk.Frame(master=frame_info, relief=tk.SUNKEN, borderwidth=7, bg=col2)
        frame.grid(column=0, row=i, sticky="news", pady=(0,10))

        label1 = tk.Label(master=frame, text=programmes[i], font=(font, 15, "bold"), 
                          bg=col2, fg=col4)
        label1.grid(column=0, row=0, sticky="w", padx=5, pady=(5,0))

        label2 = tk.Label(master=frame, text=dates[i], font=(font, 15), 
                          bg=col2, fg=col4)
        label2.grid(column=0, row=1, sticky="w", padx=5)

        label3 = tk.Label(master=frame, text=schools[i], font=(font, 15), bg=col2, fg=col4)
        label3.grid(column=0, row=2, sticky="w", padx=5)

        label4 = tk.Label(master=frame, text=notes[i], font=(font, 15), bg=col2, fg=col4, 
                          justify='left')
        label4.grid(column=0, row=3, sticky="w", padx=5, pady=(0,5))
        
    # Page memorizer (for switching language)
    global last_pressed
    last_pressed = display_education

#-----------------------------------EXPERIENCE--------------------------------------------------------
def display_experience():
    clear_frame()
    
    if language == 0: # Dutch
        display_title("Ervaring")
        functions = ["Trainee (Big Data)", "Administratief Medewerker", 
                     "Trainee (MasterClass Professional)", "Lid steunfractie & beheer database"]
        dates = ["augustus 2020 - heden", "december 2019 - juli 2020", 
                 "juni 2019 - oktober 2019", "april 2019 - heden"]
        organizations = ["YoungCapital NEXT", "Topturn Special Products", "Calco", "VVD"]
        notes = ["\t- In dit traineeship heb ik theoretische kennis over de wereld van Big Data\n\t  opgedaan, en bijbehorende technische vaardigheden ontwikkeld, waaronder\n\t  SQL, Python, Microsoft Azure en PowerBI.", 
                 "\t- Breed administratief werk, zoals: het op orde stellen van\n\t  \
bedrijfsadministratie, beheer van informatie in Word en Excel, en het\n\t  opstellen \
en verzendklaar maken van correspondentie.",
                "\t- IT-traineeship, ervaring opgedaan met agile werken, SQL, ITIL en cloud.",
                "\t- Vergaderen, adviseren en meedenken met de lokale VVD-fractie in de\n\t  \
gemeente Bergeijk.\n \
\t- Opbouw en beheer van een database van contacten in de regio."]

    if language == 1: # English
        display_title("Experience")
        functions = ["Trainee (Big Data)", "Administrative Assistant", 
                     "Trainee (MasterClass Professional)", "Party member & database manager"]
        dates = ["august 2020 - present", "december 2019 - july 2020", 
                 "june 2019 - october 2019", "april 2019 - present"]
        organizations = ["YoungCapital NEXT", "Topturn Special Products", "Calco", "VVD"]
        notes = ["\t- In this traineeship I have gained theoretical insight in the world of Big Data,\n\t  and developed accompanying technical skills, such as SQL, Python,\n\t  Microsoft Azure and PowerBI.", 
                 "\t- Broad administrative work, such as: categorizing and ordering company\n\t  \
files, information management in Word en Excel, and the preparation of\n\t  \
company correspondence.",
                "\t- IT traineeship, gained experience with Agile, SQL, ITIL and cloud.",
                "\t- Discussing, advising en deliberating with members of the local VVD in the\n\t  \
municipality of Bergeijk.\n \
\t- Building and maintenance of a database of regional contacts."]
    
    # Create content
    for i in range(len(functions)):
        frame = tk.Frame(master=frame_info, relief=tk.SUNKEN, borderwidth=7, bg=col2)
        frame.grid(column=0, row=i, sticky="news", pady=(0,10))

        label1 = tk.Label(master=frame, text=functions[i], font=(font, 15, "bold"), bg=col2, fg=col4)
        label1.grid(column=0, row=0, sticky="w", padx=5)

        label2 = tk.Label(master=frame, text=dates[i], font=(font, 15), bg=col2, fg=col4)
        label2.grid(column=0, row=1, sticky="w", padx=5)

        label3 = tk.Label(master=frame, text=organizations[i], font=(font, 15), bg=col2, fg=col4)
        label3.grid(column=0, row=2, sticky="w", padx=5)

        label4 = tk.Label(master=frame, text=notes[i], font=(font, 15), bg=col2, fg=col4, 
                          justify='left')
        label4.grid(column=0, row=3, sticky="w", padx=5)
        
    # Page memorizer (for switching language)
    global last_pressed
    last_pressed = display_experience

#-----------------------------------SKILLS------------------------------------------------------------
def display_skills():
    clear_frame()
    
    if language == 0: #Dutch
        display_title("Vaardigheden")
        skills = ["Big Data", "Statistiek en data analyse", "Onderzoek",
                  "Python (NumPy, pandas, matplotlib, statsmodels)", "R (dplyr, tidyr, ggplot2)", 
                  "SPSS", "Databases/SQL", "PowerBI", "Tableau", "Microsoft Office"]
        for i in range(len(skills)):
            frame = tk.Frame(master=frame_info, relief=tk.SUNKEN, borderwidth=7, bg=col2)
            frame.grid(column=0, row=i, sticky="news", pady=5)
            
            label = tk.Label(master=frame, text=skills[i], font=(font, 17), bg=col2, fg=col4)
            label.grid(column=0, row=0, sticky="w", padx=5, pady=3)
            
    if language == 1: #English
        display_title("Skills")
        skills = ["Big Data", "Statistics and data analysis", "Research",
                  "Python (NumPy, pandas, matplotlib, statsmodels)", "R (dplyr, tidyr, ggplot2)", 
                  "SPSS", "Databases/SQL", "PowerBI", "Tableau", "Microsoft Office"]
        for i in range(len(skills)):
            frame = tk.Frame(master=frame_info, relief=tk.SUNKEN, borderwidth=7, bg=col2)
            frame.grid(column=0, row=i, sticky="news", pady=5)
            
            label = tk.Label(master=frame, text=skills[i], font=(font, 17), bg=col2, fg=col4)     
            label.grid(column=0, row=0, sticky="w", padx=5, pady=3)
            
    # Page memorizer (for switching language)
    global last_pressed
    last_pressed = display_skills

#-----------------------------------CERTIFICATES------------------------------------------------------
def display_certificates():
    clear_frame()

    if language == 0: # Dutch      
        display_title("Certificaten")

        dates = ["oktober 2020", "oktober 2020", "oktober 2020", "augustus 2020", "augustus 2019",
                 "juli 2019", "juli 2019", "juli 2019"]
        certificates = ["Certified Big Data Consultant", "Certified Big Data Professional", 
                    "Certified Big Data Science Professional", "EXIN Agile Scrum Foundation",
                   "ITIL® 4 Foundation Certificate",
                   "EXIN Cloud Computing Foundation", "EXIN Databases en SQL Foundation",
                   "Professional Scrum Master I (PSM I)"]  
        organizations = ["Arcitura Education Inc.", "Arcitura Education Inc.", 
                         "Arcitura Education Inc.","EXIN", "PeopleCert", "EXIN", 
                         "EXIN", "Scrum.org"]
        
    if language == 1: # English
        display_title("Certificates")

        dates = ["october 2020", "october 2020", "october 2020", "august 2020", "august 2019",
                 "july 2019", "july 2019", "july 2019"]
        certificates = ["Certified Big Data Consultant", "Certified Big Data Professional", 
                    "Certified Big Data Science Professional", "EXIN Agile Scrum Foundation",
                   "ITIL® 4 Foundation Certificate",
                   "EXIN Cloud Computing Foundation", "EXIN Databases and SQL Foundation",
                   "Professional Scrum Master I (PSM I)"] 
        organizations = ["Arcitura Education Inc.", "Arcitura Education Inc.", 
                         "Arcitura Education Inc.","EXIN", "PeopleCert", "EXIN", 
                         "EXIN", "Scrum.org"]
    
    # Create content
    for i in range(0,4):
        frame = tk.Frame(master=frame_info, relief=tk.SUNKEN, borderwidth=7, bg=col2)
        frame.grid(column=0, row=i, sticky="news", pady=5, padx=5)
        
        label1 = tk.Label(master=frame, text=certificates[i], font=(font, 15, "bold"), 
                          bg=col2, fg=col4)
        label1.grid(column=0, row=0, sticky="w", padx=5, pady=(5,0))
        
        label2 = tk.Label(master=frame, text=organizations[i], font=(font, 15), bg=col2, fg=col4)
        label2.grid(column=0, row=1, sticky="w", padx=5)
        
        label3 = tk.Label(master=frame, text=dates[i], font=(font, 15), bg=col2, fg=col4)
        label3.grid(column=0, row=2, sticky="w", padx=5, pady=(0,5))
        
    cert_row_counter = 0
    for i in range(4,8):
        frame = tk.Frame(master=frame_info, relief=tk.SUNKEN, borderwidth=7, bg=col2)
        frame.grid(column=1, row=cert_row_counter, sticky="news", pady=5, padx=5)
        cert_row_counter += 1
        
        label1 = tk.Label(master=frame, text=certificates[i], font=(font, 15, "bold"), 
                          bg=col2, fg=col4)
        label1.grid(column=0, row=0, sticky="w", padx=5, pady=(5,0))
        
        label2 = tk.Label(master=frame, text=organizations[i], font=(font, 15), bg=col2, fg=col4)
        label2.grid(column=0, row=1, sticky="w", padx=5)
        
        label3 = tk.Label(master=frame, text=dates[i], font=(font, 15), bg=col2, fg=col4)
        label3.grid(column=0, row=2, sticky="w", padx=5, pady=(0,5))
        
    # Page memorizer (for switching language)
    global last_pressed
    last_pressed = display_certificates


#-----------------------------------ABOUT-------------------------------------------------------------
def display_about():
    clear_frame()  
    
    # Programming language frame   
    frame_python1 = tk.Frame(master=frame_info, relief=tk.SUNKEN, borderwidth=7, bg=col2)
    frame_python1.grid(column=0, row=0, sticky="ew", pady=(0,10))   
    frame_python2= tk.Frame(master=frame_python1, bg=col2)
    frame_python2.grid(column=0, row=1, sticky="w", pady=(10,10))
    
    # CV PDF
    frame_pdf1 = tk.Frame(master=frame_info, relief=tk.SUNKEN, borderwidth=7, bg=col2)
    frame_pdf1.grid(column=0, row=1, sticky="ew")
    frame_pdf2 = tk.Frame(master=frame_pdf1, bg=col2)
    frame_pdf2.grid(column=0, row=1, sticky="w", pady=(0,10))
    
    # Python button functionality
    def link_python(event):
        webbrowser.open_new_tab("https://www.python.org/")
    button_python = tk.Button(master=frame_python2, text="Python", font=(font, 15, "bold"), 
                              bg=col1, relief=tk.RAISED, borderwidth=5, fg=col3)
    button_python.grid(column=1, row=0, sticky="news", pady=(0,5))
    button_python.bind("<ButtonRelease-1>", link_python)
        
    # TkInter button functionality
    def link_tkinter(event):
        webbrowser.open_new_tab("https://docs.python.org/3/library/tkinter.html")
    button_tkinter = tk.Button(master=frame_python2, text="TkInter", font=(font, 15, "bold"), 
                               bg=col1, relief=tk.RAISED, borderwidth=5, fg=col3)
    button_tkinter.grid(column=1, row=1, sticky="news", pady=(0,5))
    button_tkinter.bind("<ButtonRelease-1>", link_tkinter)

    # Source code button functionality
    def link_source(event):
        webbrowser.open_new_tab("https://github.com/mghgroenen/CV")
    button_source = tk.Button(master=frame_python2, text="GitHub", font=(font, 15, "bold"), 
                               bg=col1, relief=tk.RAISED, borderwidth=5, fg=col3)
    button_source.grid(column=1, row=2, sticky="news")
    button_source.bind("<ButtonRelease-1>", link_source)
        
    # PDF button functionality
    def link_pdf(event):
        webbrowser.open_new_tab("https://www.docdroid.net/G33Lr69/cv-mart-groenen-pdf")
    button_pdf = tk.Button(master=frame_pdf2, text="Bekijken" if language==0 else "View", 
                           font=(font, 15, "bold"), bg=col1, relief=tk.RAISED, borderwidth=5, fg=col3)
    button_pdf.grid(column=1, row=0)
    button_pdf.bind("<ButtonRelease-1>", link_pdf)
        
    if language == 0: #Dutch
        display_title("Overige informatie")

        # Programming language frame contents
        info_programming = tk.Label(master=frame_python1, text="Deze applicatie is geschreven in Python. De Graphical User Interface (GUI) is\ngemaakt met behulp van de package TkInter. Gebruik onderstaande knoppen om\nhier meer over te weten te komen, of om de complete source code te bekijken.",
                                    font=(font, 15), bg=col2, fg=col4, justify="left")
        label_python = tk.Label(master=frame_python2, text="Programmeertaal:  ", font=(font, 15), 
                                bg=col2, fg=col4)  
        label_tkinter = tk.Label(master=frame_python2, text="GUI package:", font=(font, 15), 
                                 bg=col2, fg=col4)

        label_source = tk.Label(master=frame_python2, text="Source code:", font=(font, 15), 
                                bg=col2, fg=col4)

        # PDF frame contents
        info_pdf = tk.Label(master=frame_pdf1, text="Gebruik onderstaande knop om een PDF-versie van dit CV te bekijken.",
                           font=(font, 15), bg=col2, fg=col4, justify="left")
        label_pdf = tk.Label(master=frame_pdf2, text="PDF-bestand:  ", font=(font, 15), 
                             bg=col2, fg=col4)
        
    if language == 1: #English
        display_title("Extra information")

        # Programming language frame contents
        info_programming = tk.Label(master=frame_python1, text="This application is written in Python. The Graphical User Interface (GUI) is\nmade using the TkInter package. Use the buttons below to learn more or to\nview the complete source code.",
                                    font=(font, 15), bg=col2, fg=col4, justify="left")
        label_python = tk.Label(master=frame_python2, text="Programming language:  ", 
                                font=(font, 15), bg=col2, fg=col4)  
        label_tkinter = tk.Label(master=frame_python2, text="GUI package:", font=(font, 15), 
                                 bg=col2, fg=col4)
        label_source = tk.Label(master=frame_python2, text="Source code:", font=(font, 15), 
                                bg=col2, fg=col4)

        # PDF frame contents
        info_pdf = tk.Label(master=frame_pdf1, text="Use the button below to view a PDF version of this resume.",
                           font=(font, 15), bg=col2, fg=col4, justify="left")
        label_pdf = tk.Label(master=frame_pdf2, text="PDF file (in Dutch):  ", font=(font, 15), 
                             bg=col2, fg=col4)
    
    # Grids
    info_programming.grid(column=0, row=0, padx=(10,0), pady=(10,0))
    label_python.grid(column=0, row=0, sticky="w", padx=(10,0))
    label_tkinter.grid(column=0, row=1, sticky="w", padx=(10,0))
    label_source.grid(column=0, row=2, sticky="w", padx=(10,0))
    info_pdf.grid(column=0, row=0, padx=(10,0), pady=(10,10))
    label_pdf.grid(column=0, row=0, padx=(10, 0), pady=10)
    
    # Page memorizer (for switching language)
    global last_pressed
    last_pressed = display_about
        
#-----------------------------------CONTACT-----------------------------------------------------------
def display_contact():
    clear_frame()
        
    # Contact frame
    frame_contact = tk.Frame(master=frame_info, bg=col1)
    frame_contact.grid(column=0, row=0)
    
    # Mart frame
    frame_mart = tk.Frame(master=frame_contact, relief=tk.SUNKEN, borderwidth=7, bg=col2)
    frame_mart.grid(column=0, row=0, sticky="news")
    frame_mart.columnconfigure(0, minsize=150)
    
    #YC title
    yc_title = tk.Label(master=frame_contact, text="YoungCapital NEXT", font=(font, 30, "bold"), 
                        bg=col1, fg=col3)
    yc_title.grid(column=0, row=1, pady=(80,20))
    
    # YC frame
    frame_yc = tk.Frame(master=frame_contact, relief=tk.SUNKEN, borderwidth=7, bg=col2)
    frame_yc.grid(column=0, row=2)
    frame_yc.columnconfigure(0, minsize=150)
    
    if language == 0: # Dutch
        display_title("Contactinformatie")
        
        # Contact attribute descriptors
        contact_name1 = tk.Label(master=frame_mart, text="Naam:", font=(font, 15, "bold"), 
                                 bg=col2, fg=col4)
        contact_phone1 = tk.Label(master=frame_mart, text="Telefoon:", font=(font, 15, "bold"), 
                                  bg=col2, fg=col4)
        contact_mail1 = tk.Label(master=frame_mart, text="E-mail:", font=(font, 15, "bold"), 
                                 bg=col2, fg=col4)
        contact_linkedin1 = tk.Label(master=frame_mart, text="LinkedIn:", font=(font, 15, "bold"),
                                     bg=col2, fg=col4)
        contact_github1 = tk.Label(master=frame_mart, text="GitHub:", font=(font, 15, "bold"),
                                   bg=col2, fg=col4)
        # YoungCapital NEXT attribute descriptors
        yc_name1 = tk.Label(master=frame_yc, text="Naam:", font=(font, 15, "bold"), 
                            bg=col2, fg=col4)
        yc_function1 = tk.Label(master=frame_yc, text="Functie:", font=(font, 15, "bold"), 
                                 bg=col2, fg=col4)
        yc_phone1 = tk.Label(master=frame_yc, text="Telefoon:", font=(font, 15, "bold"), 
                              bg=col2, fg=col4)
        yc_mail1 = tk.Label(master=frame_yc, text="E-mail:", font=(font, 15, "bold"), 
                             bg=col2, fg=col4)

    if language == 1: # English
        display_title("Contact information")
        
        # Contact attribute descriptors
        contact_name1 = tk.Label(master=frame_mart, text="Name:", font=(font, 15, "bold"), 
                                 bg=col2, fg=col4)
        contact_phone1 = tk.Label(master=frame_mart, text="Telephone:", font=(font, 15, "bold"), 
                                  bg=col2, fg=col4)
        contact_mail1 = tk.Label(master=frame_mart, text="Email:", font=(font, 15, "bold"), 
                                 bg=col2, fg=col4)
        contact_linkedin1 = tk.Label(master=frame_mart, text="LinkedIn:", font=(font, 15, "bold"),
                                     bg=col2, fg=col4)
        contact_github1 = tk.Label(master=frame_mart, text="GitHub:", font=(font, 15, "bold"),
                                   bg=col2, fg=col4)
        # YoungCapital NEXT attribute descriptors
        yc_name1 = tk.Label(master=frame_yc, text="Name:", font=(font, 15, "bold"), 
                            bg=col2, fg=col4)
        yc_function1 = tk.Label(master=frame_yc, text="Function:", font=(font, 15, "bold"), 
                                 bg=col2, fg=col4)
        yc_phone1 = tk.Label(master=frame_yc, text="Telephone:", font=(font, 15, "bold"), 
                              bg=col2, fg=col4)
        yc_mail1 = tk.Label(master=frame_yc, text="Email:", font=(font, 15, "bold"), 
                             bg=col2, fg=col4)
    
    # Contact attribute values
    contact_name2 = tk.Label(master=frame_mart, text="Mart Groenen", font=(font, 15), 
                             bg=col2, fg=col4)
    contact_phone2 = tk.Label(master=frame_mart, text="+31 6 20001682", font=(font, 15), 
                              bg=col2, fg=col4)
    contact_mail2 = tk.Label(master=frame_mart, text="mgh.groenen@gmail.com", font=(font, 15),
                            bg=col2, fg=col4)   
    def link_linkedin(event):
        webbrowser.open_new_tab("https://www.linkedin.com/in/mart-groenen-a00524134/")
    contact_linkedin2 = tk.Button(master=frame_mart, 
                                  text="Klik hier" if language==0 else "Click here", 
                                  font=(font, 15, "bold"), bg=col1, fg=col3, 
                                  relief=tk.RAISED, borderwidth=5)
    def link_github(event):
        webbrowser.open_new_tab("https://github.com/mghgroenen")
    contact_github2 = tk.Button(master=frame_mart, 
                                text="Klik hier" if language==0 else "Click here", 
                                font=(font, 15, "bold"), bg=col1, fg=col3, 
                                relief=tk.RAISED, borderwidth=5)
    #YoungCapital Next attribute values
    yc_name2 = tk.Label(master=frame_yc, text="Jessy Antonis", font=(font, 15), 
                        bg=col2, fg=col4)
    yc_function2 = tk.Label(master=frame_yc, text="Account Manager IT", font=(font, 15), 
                            bg=col2, fg=col4)
    yc_phone2 = tk.Label(master=frame_yc, text="+31 6 20001682", font=(font, 15), 
                         bg=col2, fg=col4)
    yc_mail2 = tk.Label(master=frame_yc, text="j.antonis@next.youngcapital.nl", font=(font, 15), 
                        bg=col2, fg=col4)
    
    # Grids & binds
    contact_name1.grid(column=0, row=0, sticky="w", padx=5, pady=(5,0))    
    contact_name2.grid(column=1, row=0, sticky="w", padx=5)
    contact_phone1.grid(column=0, row=1, sticky="w", padx=5)
    contact_phone2.grid(column=1, row=1, sticky="w", padx=5)
    contact_mail1.grid(column=0, row=2, sticky="w", padx=5)
    contact_mail2.grid(column=1, row=2, sticky="w", padx=5)
    contact_linkedin1.grid(column=0, row=3, sticky="w", padx=5)
    contact_linkedin2.grid(column=1, row=3, sticky="w", pady=(0,5), padx=5)
    contact_linkedin2.bind("<ButtonRelease-1>", link_linkedin)
    contact_github1.grid(column=0, row=4, sticky="w", padx=5)
    contact_github2.grid(column=1, row=4, sticky="w", padx=5, pady=(0,5))
    contact_github2.bind("<ButtonRelease-1>", link_github)
    
    yc_name1.grid(column=0, row=0, sticky="w", padx=5, pady=(5,0))
    yc_name2.grid(column=1, row=0, sticky="w", padx=5)
    yc_function1.grid(column=0, row=1, sticky="w", padx=5)
    yc_function2.grid(column=1, row=1, sticky="w", padx=5)
    yc_phone1.grid(column=0, row=2, sticky="w", padx=5)
    yc_phone2.grid(column=1, row=2, sticky="w", padx=5)
    yc_mail1.grid(column=0, row=3, sticky="w", padx=5)
    yc_mail2.grid(column=1, row=3, sticky="w", padx=5, pady=(0,5))
    
    # Page memorizer (for switching language)
    global last_pressed
    last_pressed = display_contact

#-----------------------------------MENU FRAME--------------------------------------------------------
frame_menu = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5, bg=col2)
frame_menu.grid(row=0, column=0, sticky="news")

# Menu buttons
button_list = ["Profiel", "Opleiding", "Ervaring", "Vaardigheden", "Certificaten", 
               "Overig", "Contact"]
command_list = [display_profile, display_education, display_experience, display_skills,
               display_certificates, display_about, display_contact]

button_list_en = ["Profile", "Education", "Experience", "Skills", "Certificates", 
                  "Extra", "Contact"]

def create_frame_menu():
    if language == 0:
        button_counter=0
        for i in range(len(button_list)):
            button = tk.Button(master=frame_menu, text=button_list[i], font=(font, 25), bg=col1, 
                               relief=tk.RAISED, borderwidth=7, command=command_list[i], fg=col3)
            button.grid(column=0, row=button_counter, sticky="news", padx=5, pady=7)
            button_counter += 1 

        label_language = tk.Label(master=frame_menu, text="Taalkeuze", font=(font, 17, "bold"), 
                                  bg=col2, fg=col4)
        label_language.grid(column=0, row=button_counter+1, pady=(55, 15))

    if language == 1:
        button_counter=0
        for i in range(len(button_list)):
            button = tk.Button(master=frame_menu, text=button_list_en[i], font=(font, 25), bg=col1, 
                               relief=tk.RAISED, borderwidth=7, command=command_list[i], fg=col3)
            button.grid(column=0, row=button_counter, sticky="news", padx=5, pady=7)
            button_counter += 1
            
        label_language = tk.Label(master=frame_menu, text="Language", font=(font, 17, "bold"), 
                                  bg=col2, fg=col4)
        label_language.grid(column=0, row=button_counter+1, pady=(55, 15))

# Flag images
    global img_nl
    global img_en
    
    frame_flags = tk.Frame(master=frame_menu, bg=col2)
    frame_flags.grid(column=0, row=button_counter+2, pady=(0,10))

    canvas_nl = tk.Canvas(master=frame_flags, width=60, height=35, relief=tk.RAISED, borderwidth=3, 
                          bg=col2)
    canvas_nl.grid(column=0, row=0, padx=(0,7))
    img_nl = tk.PhotoImage(data=cvi.nl_string)
    canvas_nl.create_image(5,5, image=img_nl, anchor="nw")

    canvas_en = tk.Canvas(master=frame_flags, width=60, height=35, relief=tk.RAISED, borderwidth=3, 
                          bg=col2)
    canvas_en.grid(column=1, row=0, padx=(7,0))
    img_en = tk.PhotoImage(data=cvi.uk_string)
    canvas_en.create_image(5,5, image=img_en, anchor="nw")

    # Flag buttons
    def select_language(input):
        global language
        language = input
        window_title()
        create_frame_menu() # Recursion!
        clear_frame()
        last_pressed()

    def on_press_nl(event):
        canvas_nl.configure(relief="sunken")
    def on_release_nl(event):
        canvas_nl.configure(relief="raised") 
        select_language(0)
    canvas_nl.bind("<ButtonPress-1>", on_press_nl)
    canvas_nl.bind("<ButtonRelease-1>", on_release_nl)

    def on_press_en(event):
        canvas_en.configure(relief="sunken")
    def on_release_en(event):
        canvas_en.configure(relief="raised")  
        select_language(1)    
    canvas_en.bind("<ButtonPress-1>", on_press_en)
    canvas_en.bind("<ButtonRelease-1>", on_release_en)

#-----------------------------------DISPLAY FRAME-----------------------------------------------------
frame_display = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5, bg=col1)
frame_display.columnconfigure(0, weight=1, minsize=850)
frame_display.grid(row=0, column=1, sticky = "news")

# Display title frame
frame_title = tk.Frame(master=frame_display, bg=col1)
frame_title.grid(column=0, row=0, pady="20")

def display_title(title_input):
    display_title = tk.Label(master=frame_title, text=title_input, font=(font, 30, "bold"), 
                             fg=col3, bg=col1)
    display_title.grid(column=0, row=0, sticky="news")

# Display information frame
def create_frame_info():
    global frame_info
    frame_info = tk.Frame(master=frame_display, bg=col1)
    frame_info.grid(column=0, row=1)

#-----------------------------------MAIN LOOP---------------------------------------------------------
language = 0
def window_title():
    window.title("CV van Mart Groenen" if language==0 else "Resume of Mart Groenen")
window_title()
create_frame_menu()
create_frame_info()
display_profile(start=0)
window.mainloop()
