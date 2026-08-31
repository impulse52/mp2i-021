from fasthtml.common import * 

app, rt = fast_app()

@rt('/')
def get(): 
    return(
        Main(
            Div( 
                Title('MP2ICarnot25-26'),
                H1("MP2I 2025-2026", style="color: black; padding-left: 20px; padding-top: 15px;"),
                P("Lycée Carnot Dijon", style="color: black; padding-left: 20px;"),
                P("\n"),
                Div(
                    Article(
                        P("Bienvenue sur le site de la MP2I de Carnot (Dijon)." \
                        " Vous trouverez ci dessous les documents utilisés durant l'année scolaire 2025-2026." \
                        " Amusez-vous bien !! ")
                        ), style="padding-left: 30px; width: 500px;"
                    ),
                Div(
                    Article(
                        A("Maths", href="/maths")
                        ), style="padding-left: 30px; padding-right: 30px;"
                    ),
                P("\n"),
                Div(
                    Article(
                        A("Physique", href="/physique")
                        ), style="padding-left: 30px; padding-right: 30px;"
                    ),
                P("\n"),
                Div(
                    Article(
                        A("Info", href="/info")
                        ), style="padding-left: 30px; padding-right: 30px;"
                    ),
                P("\n"),
                Div(
                    Article(
                        A("Anglais", href="/anglais")
                        ), style="padding-left: 30px; padding-right: 30px;"
                    )
                ),
            style="""
            background-image: url('/static/font.jpg');
            background-size: cover;
            background-position: center;
            min-height: 100vh;
        """
        ),
            )

@rt('/maths')
def get():
    return(
    H1("Maths de Mathieu MANSUY", style="padding-left: 20px; padding-top: 15px;"),
    Br(),
    Div(
        Article(
            H3("Cours"),
            P("\n"),
            Div(
                Div(
                    A("1.Raisonner et rédiger", href="/static/CM/1.pdf"), Br(),
                    A("2.Rappels et compléments calculatoires en analyse", href="/static/CM/2.pdf"), Br(),
                    A("3.Calculs algébriques et trigonométriques", href="/static/CM/3.pdf"), Br(),
                    A("4.Rappels et compléments sur les fonctions", href="/static/CM/4.pdf"), Br(),
                    A("5.Systèmes linéaires", href="/static/CM/5.pdf"), Br(),
                    A("6.Fonctions usuelles", href="/static/CM/6.pdf"), Br(),
                    A("7.Nombres complexes", href="/static/CM/7.pdf"), Br(),
                    A("8.Calculs de primitives et d'intégrales", href="/static/CM/8.pdf"), Br(),
                    A("9.Arithmétique des entiers relatifs", href="/static/CM/9.pdf"), Br(),
                    A("10.Equations différentielles", href="/static/CM/10.pdf"), Br(),
                    A("11.Ensembles et relations binaires", href="/static/CM/11.pdf"), Br(),
                    A("12.Nombres réels", href="/static/CM/12.pdf"), Br(),
                    ),
                Div(
                    A("13.Applications", href="/static/CM/13.pdf"), Br(),
                    A("14.Suites", href="/static/CM/14.pdf"), Br(),
                    A("15.Dénombrement", href="/static/CM/15.pdf"), Br(),
                    A("16.Limites, continuité", href="/static/CM/16.pdf"), Br(),
                    A("17.Calcul matriciel", href="/static/CM/17.pdf"), Br(),
                    A("18.Dérivabilité", href="/static/CM/18.pdf"), Br(),
                    A("19.Structures algébriques", href="/static/CM/19.pdf"), Br(),
                    A("20.Analyse asymptotique", href="/static/CM/20.pdf"), Br(),
                    A("21.Polynômes", href="/static/CM/21.pdf"), Br(),
                    A("22.Développements limités", href="/static/CM/22.pdf"), Br(),
                    A("23.Espaces vectoriels", href="/static/CM/23.pdf"), Br(),
                    A("24.Dimension finie", href="/static/CM/24.pdf"), Br(),
                    ),
                Div(
                    A("25.Séries numériques", href="/static/CM/25.pdf"), Br(),
                    A("26.Applications linéaires", href="/static/CM/26.pdf"), Br(),
                    A("27.Espaces probabilisés", href="/static/CM/27.pdf"), Br(),
                    A("28.Représentations matricielles", href="/static/CM/28.pdf"), Br(),
                    A("29.Variables aléatoires finies", href="/static/CM/29.pdf"), Br(),
                    A("30a.Groupes symétriques", href="/static/CM/30a.pdf"), Br(),
                    A("30b.Déterminants", href="/static/CM/30b.pdf"), Br(),
                    A("31.Couples et vecteurs aléatoires", href="/static/CM/31.pdf"), Br(),
                    A("32.Intégration", href="/static/CM/32.pdf"), Br(),
                    A("33.Fonctions convexes", href="/static/CM/33.pdf"), Br(),
                    A("34.Espaces préhilbertiens", href="/static/CM/34.pdf"), Br(),
                    A("35.Familles sommables", href="/static/CM/35.pdf"), Br(),
                    A("36.Fonctions de deux variables", href="/static/CM/36.pdf"), Br()
                ),
                style="padding-left: 30px; padding-right: 30px;",
                cls="grid"
                ),
                 style="padding-left: 30px; padding-right: 30px;"
            )
        ),
        Br(),
        Div(
            Article(
                H3("TD"),
                P("\n"),
                Div(
                    Div(
                        A("TD 1", href="/static/TDM/TD1.pdf"), Br(),
                        A("TD 2", href="/static/TDM/TD2.pdf"), Br(),
                        A("TD 3", href="/static/TDM/TD3.pdf"), Br(),
                        A("TD 4", href="/static/TDM/TD4.pdf"), Br(),
                        A("TD 5", href="/static/TDM/TD5.pdf"), Br(),
                        A("TD 6", href="/static/TDM/TD6.pdf"), Br(),
                        A("TD 7", href="/static/TDM/TD7.pdf"), Br(),
                        A("TD 8", href="/static/TDM/TD8.pdf"), Br(),
                        A("TD 9", href="/static/TDM/TD9.pdf"), Br(),
                        A("TD 10", href="/static/TDM/TD10.pdf"), Br(),
                        A("TD 11", href="/static/TDM/TD11.pdf"), Br(),
                        A("TD 12", href="/static/TDM/TD12.pdf"), Br(),
                    ),
                    Div(
                        A("TD 13", href="/static/TDM/TD13.pdf"), Br(),
                        A("TD 14", href="/static/TDM/TD14.pdf"), Br(),
                        A("TD 15", href="/static/TDM/TD15.pdf"), Br(),
                        A("TD 16", href="/static/TDM/TD16.pdf"), Br(),
                        A("TD 17", href="/static/TDM/TD17.pdf"), Br(),
                        A("TD 18", href="/static/TDM/TD18.pdf"), Br(),
                        A("TD 19", href="/static/TDM/TD19.pdf"), Br(),
                        A("TD 20", href="/static/TDM/TD20.pdf"), Br(),
                        A("TD 21", href="/static/TDM/TD21.pdf"), Br(),
                        A("TD 22", href="/static/TDM/TD22.pdf"), Br(),
                        A("TD 23", href="/static/TDM/TD23.pdf"), Br(),
                        A("TD 24", href="/static/TDM/TD24.pdf"), Br(),
                    ),
                    Div(
                        A("TD 25", href="/static/TDM/TD25.pdf"), Br(),
                        A("TD 26", href="/static/TDM/TD26.pdf"), Br(),
                        A("TD 27", href="/static/TDM/TD27.pdf"), Br(),
                        A("TD 28", href="/static/TDM/TD28.pdf"), Br(),
                        A("TD 29", href="/static/TDM/TD29.pdf"), Br(),
                        A("TD 30", href="/static/TDM/TD30.pdf"), Br(),
                        A("TD 31", href="/static/TDM/TD31.pdf"), Br(),
                        A("TD 32", href="/static/TDM/TD32.pdf"), Br(),
                        A("TD 33", href="/static/TDM/TD33.pdf"), Br(),
                        A("TD 34", href="/static/TDM/TD34.pdf"), Br(),
                        A("TD 35", href="/static/TDM/TD35.pdf"), Br(),
                        A("TD 36", href="/static/TDM/TD36.pdf"), Br()
                    ),
                    style="padding-left: 30px; padding-right: 30px;",
                    cls="grid"
                ),
                style="padding-left: 30px; padding-right: 30px;"
            )
        ),
        Br(),
        Div(
            Article(
                H3("DS"),
                P("\n"),
                Div(
                    Div(
                        H4("Sujets"),
                            A("DS1", href="/static/DSM/MP2I-DS1.pdf"), Br(),
                            A("DS2", href="/static/DSM/MP2I-DS2.pdf"), Br(),
                            A("DS3", href="/static/DSM/MP2I-DS3.pdf"), Br(),
                            A("DS4", href="/static/DSM/MP2I-DS4.pdf"), Br(),
                            A("DS5", href="/static/DSM/MP2I-DS5.pdf"), Br(),
                            A("DS6", href="/static/DSM/MP2I-DS6.pdf"), Br(),
                            A("DS8", href="/static/DSM/MP2I-DS8.pdf"), Br(),
                            A("CB1", href="/static/DSM/MP2I-DS9-CB1.pdf"), Br(),
                            A("CB2", href="/static/DSM/MP2I-DS6-CB2.pdf"), Br(),
                            A("DS10", href="/static/DSM/MP2I-DS10.pdf"), Br()
                    ),
                    Div(
                        H4("Corrections"),
                            A("DS1", href="/static/DSM/MP2I-DS1-correction.pdf"), Br(),
                            A("DS2", href="/static/DSM/MP2I-DS2-correction.pdf"), Br(),
                            A("DS3", href="/static/DSM/MP2I-DS3-correction.pdf"), Br(),
                            A("DS4", href="/static/DSM/MP2I-DS4-correction.pdf"), Br(),
                            A("DS5", href="/static/DSM/MP2I-DS5-correction.pdf"), Br(),
                            A("DS6", href="/static/DSM/MP2I-DS6-correction.pdf"), Br(),
                            A("DS8", href="/static/DSM/MP2I-DS8-correction.pdf"), Br(),
                            A("CB1", href="/static/DSM/MP2I-DS9-CB1-correction.pdf"), Br(),
                            A("CB2", href="/static/DSM/MP2I-DS6-CB2-correction.pdf"), Br(),
                            A("DS10", href="/static/DSM/MP2I-DS10-correction.pdf"), Br()
                    ),
                    style="padding-left: 30px; padding-right: 30px;",
                    cls="grid"
                )
            )
        )
    )

@rt('/physique')
def get():
    return(
    H1("Physique de Florian OZON", style="padding-left: 20px; padding-top: 15px;"),
    Br(),
    Article(
        H3("Cours", style="padding-left: 20px;"),
        Div(
            Div(
                Div(
                    Article(
                        H4("Unitées de mesure"),
                        P("\n"),
                        A("UM1", href="/static/CP/UM1.pdf"), Br(),
                        A("UM2", href="/static/CP/UM2.pdf"), Br()
                    )
                ),
                Div(
                    Article(
                        H4("Optique géométrique"),
                        P("\n"),
                        A("OG1", href="/static/CP/OG1.pdf"), Br(),
                        A("OG2", href="/static/CP/OG2.pdf"), Br(),
                        A("OG3", href="/static/CP/OG3.pdf"), Br(),
                        A("OG4", href="/static/CP/OG4.pdf"), Br(),
                    )
                ),
                Div(
                    Article(
                        H4("Ondes"),
                        P("\n"),
                        A("OS1", href="/static/CP/OS1.pdf"), Br(),
                        A("OS2", href="/static/CP/OS2.pdf"), Br(),
                        A("OS3", href="/static/CP/OS3.pdf"), Br(),
                    )
                ),
                Div(
                    Article(
                        H4("Chimie (option)"),
                        P("\n"),
                        A("SPM", href="/static/CP/SPM.pdf"), Br(),
                        A("TM", href="/static/CP/TM.pdf"), Br()
                    )
                )
            ),
            Div(
                Div(
                    Article(
                        H4("Electricité"),
                        P("\n"),
                        A("EL1", href="/static/CP/EL1.pdf"), Br(),
                        A("EL2", href="/static/CP/EL2.pdf"), Br(),
                        A("EL3", href="/static/CP/EL3.pdf"), Br(),
                        A("EL4", href="/static/CP/EL4.pdf"), Br(),
                        A("EL5", href="/static/CP/EL5.pdf"), Br(),
                        A("EL6", href="/static/CP/EL6.pdf"), Br(),
                    )
                ),
                Div(
                    Article(
                        H4("Mécanique"),
                        P("\n"),
                        A("M1", href="/static/CP/M1.pdf"), Br(),
                        A("M2.1", href="/static/CP/M2.pdf"), Br(),
                        A("M2.2", href="/static/CP/M2_2.pdf"), Br(),
                        A("M3", href="/static/CP/M3.pdf"), Br(),
                        A("M4", href="/static/CP/M4.pdf"), Br(),
                        A("M5", href="/static/CP/M5.pdf"), Br(),
                        A("M6", href="/static/CP/M6.pdf"), Br(),
                    )
                ),
                Div(
                    Article(
                        H4("Mécanique quantique"),
                        P("\n"),
                        A("MQ", href="/static/CP/MQ.pdf"), Br()
                    )
                )
            ),
            Div(
                Div(
                    Article(
                        H4("Thermodynamique"),
                        P("\n"),
                        A("TH1", href="/static/CP/TH1.pdf"), Br(),
                        A("TH2", href="/static/CP/TH2.pdf"), Br(),
                        A("TH3", href="/static/CP/TH3.pdf"), Br(),
                        A("Intro TH4", href="/static/CP/Aspect historique second principe complet.pdf"), Br(),
                        A("TH4", href="/static/CP/TH4.pdf"), Br(),
                        A("TH5", href="/static/CP/TH5.pdf"), Br(),
                        A("TH6", href="/static/CP/TH6.pdf"), Br(),
                    )
                ),
                Div(
                    Article(
                        H4("Electromagnétisme"),
                        P("\n"),
                        A("EM0", href="/static/CP/EM0.pdf"), Br(),
                        A("EM1", href="/static/CP/EM1.pdf"), Br(),
                        A("EM2.1", href="/static/CP/EM2.pdf"), Br(),
                        A("EM2.2", href="/static/CP/EM2_2.pdf"), Br(),
                        A("EM3", href="/static/CP/EM3.pdf"), Br(),
                        A("EM4", href="/static/CP/EM4.pdf"), Br(),
                        A("EM5", href="/static/CP/EM5.pdf"), Br(),
                    )
                )
            ),
            style="padding-left: 30px; padding-right: 30px;",
            cls="grid"
        ),
    ),
        Br(),
        Br(),
        Article(
        H3("TD", style="padding-left: 20px;"),
        Div(
            Div(
                Div(
                    Article(
                        H4("Unitées de mesure"),
                        P("\n"),
                        A("UM", href="/static/TDP/USI.pdf"), Br(),
                    )
                ),
                Div(
                    Article(
                        H4("Optique géométrique"),
                        P("\n"),
                        A("OG", href="/static/TDP/OG.pdf"), Br(),
                    )
                ),
                Div(
                    Article(
                        H4("Ondes"),
                        P("\n"),
                        A("OS", href="/static/TDP/OS.pdf"), Br(),
                    )
                ),
                Div(
                    Article(
                        H4("Mécanique quantique"),
                        P("\n"),
                        A("MQ", href="/static/TDP/MQ.pdf"), Br()
                    )
                ),
            ),
            Div(
                Div(
                    Article(
                        H4("Electricité"),
                        P("\n"),
                        A("EL1-3", href="/static/TDP/ELpartie1.pdf"), Br(),
                        A("EL4", href="/static/TDP/EL4.pdf"), Br(),
                        A("EL5", href="/static/TDP/EL5.pdf"), Br(),
                    )
                ),
                Div(
                    Article(
                        H4("Mécanique"),
                        P("\n"),
                        A("M1", href="/static/TDP/M1.pdf"), Br(),
                        A("M2", href="/static/TDP/M2.pdf"), Br(),
                        A("M3", href="/static/TDP/M3.pdf"), Br(),
                        A("M4-6", href="/static/TDP/M456.pdf"), Br(),
                    )
                )
            ),
            Div(
                Div(
                    Article(
                        H4("Thermodynamique"),
                        P("\n"),
                        A("TH1-3", href="/static/TDP/TH1-3.pdf"), Br(),
                        A("TH4", href="/static/TDP/TH4.pdf"), Br(),
                        A("TH5", href="/static/TDP/TH5.pdf"), Br(),
                        A("TH6", href="/static/TDP/TH6.pdf"), Br(),
                    )
                ),
                Div(
                    Article(
                        H4("Electromagnétisme"),
                        P("\n"),
                        A("EM1", href="/static/TDP/EM1.pdf"), Br(),
                        A("EM2-3", href="/static/CP/EM23.pdf"), Br()
                    )
                )
            ),
            style="padding-left: 30px; padding-right: 30px;",
            cls="grid"
        )
        ),
       Br(),
       Br(),
        Article(
            H3("DS", style="padding-left: 20px;"),
            Div(
                Div(
                    Article(
                        P("\n"),
                        H4("Sujets"),
                        A("DS1", href="/static/CP/DS n1.pdf"), Br(),
                        A("DS2", href="/static/CP/DS n2.pdf"), Br(),
                        A("DS3", href="/static/CP/DS n3.pdf"), Br(),
                        A("DS4", href="/static/CP/DS n4.pdf"), Br(),
                        A("DS5", href="/static/CP/DS n5.pdf"), Br(),
                        A("DS6", href="/static/CP/DS n6.pdf"), Br(),
                        A("CCB", href="/static/CP/CCB.pdf"), Br(),
                    )
                ),
                Div(
                    Article(
                        P("\n"),
                        H4("Corrections"),
                        A("DS1", href="/static/CP/Correction DS n1.pdf"), Br(),
                        A("DS2", href="/static/CP/Correction DS n2.pdf"), Br(),
                        A("DS3", href="/static/CP/Correction DS n3.pdf"), Br(),
                        A("DS4", href="/static/CP/Correction DS n4.pdf"), Br(),
                        A("DS5", href="/static/CP/Correction DS n5.pdf"), Br(),
                        A("DS6", href="/static/CP/Correction DS n6.pdf"), Br(),
                        A("CCB", href="/static/CP/Correction CCB.pdf"), Br(),
                        )
                    ),
                    style="padding-left: 30px; padding-right: 30px;",
                    cls="grid"
                )
            )
        ) 

@rt('/info')
def get():
    return(
    H1("Info de Mathilde DEPRES", style="padding-left: 20px; padding-top: 15px;"),
    Br(),
        Div(
            Article(
                H3("Cours", style="padding-left: 10px;",),
                P("\n"),
                Div(
                    A("memo_bash.pdf", href="/static/IN/memo_bash.pdf"), Br(),
                    A("Cours_C.pdf", href="/static/IN/Cours_C.pdf"), Br(),
                    A("Cours_Ocaml.pdf", href="/static/IN/Cours_Ocaml.pdf"), Br(),
                    A("Cours_listes.pdf", href="/static/IN/Cours_listes.pdf"), Br(),
                    A("Cours_piles.pdf", href="/static/IN/Cours_piles.pdf"), Br(),
                    A("Cours_discipline", href="/static/IN/Cours_discipline.pdf"), Br(),
                    style="padding-left: 30px; padding-right: 30px;"
                )
            ),
        ),
        Br(),
        Div(
            Article(
                H3("TD", style="padding-left: 10px;"),
                P("\n"),
                Div(
                    Div(
                        A("TD1-Introduction au binaire", href="/static/IN/td1.pdf"), Br(),
                        A("TD2-Pointeurs en C", href="/static/IN/td2.pdf"), Br(),
                        A("TD3-Prouver les programmes", href="/static/IN/td3.pdf"), Br(),
                        P("TD4-Représentation des nombres (rupture de stock sur le site (404))"),
                        A("TD5-Nombres et complexité", href="/static/IN/td5.pdf"), Br(),
                        A("TD6-Complexité", href="/static/IN/td6.pdf"), Br(),
                        A("TD7-Types Ocaml", href="/static/IN/td7.pdf"), Br(),
                        A("TD8-Récursivité terminale", href="/static/IN/td8.pdf"), Br(),
                        A("TD9-Wordle", href="/static/IN/td9.pdf"), Br(),
                    ),
                    Div(
                        A("TD10-Structure sac", href="/static/IN/td10.pdf"), Br(),
                        A("TD11-Piles et files", href="/static/IN/td11.pdf"), Br(),
                        A("TD12-Dichotomie", href="/static/IN/td12.pdf"), Br(),
                        A("TD13-Arbres", href="/static/IN/td13.pdf"), Br(),
                        A("TD14-Recherche exhaustive", href="/static/IN/td14.pdf"), Br(),
                        A("TD15-Induction structurelle", href="/static/IN/td15.pdf"), Br(),
                        A("TD16-Algorithmes gloutons", href="/static/IN/td16.pdf"), Br(),
                        A("TD17-Logique", href="/static/IN/td17.pdf"), Br(),
                        A("TD18-ABR et arbres rouge-noir", href="/static/IN/td18.pdf"), Br(),
                    ),
                    style="padding-left: 30px; padding-right: 30px;",
                    cls="grid"
                )
            )
        ),
        Br(),
        Div(
            Article(
                H3("DS", style="padding-left: 10px;"),
                P("\n"),
                Div(
                    Div(
                        H4("Sujets"),
                        P("\n"),
                        A("DS1", href="/static/IN/ds1.pdf"), Br(),
                        A("DS2", href="/static/IN/ds2.pdf"), Br(),
                        A("DS3", href="/static/IN/DS3.pdf"), Br(),
                        A("DS4", href="/static/IN/DS4.pdf"), Br(),
                        A("CCB", href="/static/IN/DS5.pdf"), Br(),
                        A("DS6", href="/static/IN/DS6.pdf"), Br(),
                    ),
                    Div(
                        H4("Corrections"),
                        P("\n"),
                        A("DS1", href="/static/IN/ds1_corrige.pdf"), Br(),
                        A("DS2", href="/static/IN/ds2_corrige.pdf"), Br(),
                        A("DS3", href="/static/IN/DS3_corrige.pdf"), Br(),
                        A("DS4", href="/static/IN/DS4_corrige.pdf"), Br(),
                        A("CCB", href="/static/IN/corrige_DS5.pdf"), Br(),
                        A("DS6", href="/static/IN/corrige_DS6.pdf"), Br(),
                    ),
                    style="padding-left: 30px; padding-right: 30px;",
                    cls="grid"
                )
            )
        ),
    )

@rt('/anglais')
def get():
    return(
    H1("Anglais de Jutine RENAULT", style="padding-left: 20px; padding-top: 15px;"),
    Br(),
        Div(
            Article(
                H3("Liens vers les padlets", style="padding-left: 10px;"),
                P("\n"),
                Div(
                    A("The Media", href="https://padlet.com/MissRenault/the-media-kaaqobz6x8yr9ynl"), Br(),
                    A("Dystopian Futures", href="https://padlet.com/MissRenault/ai-computer-science-4qigod72ab0qc58p"), Br(),
                    A("Space", href="https://padlet.com/MissRenault/space-n540mkk8a80ejsll"), Br(),
                    A("Brexit", href="https://padlet.com/MissRenault/brexit-u3vj5v285b5i"), Br(),
                    A("Environment", href="https://padlet.com/MissRenault/environment-pc-jvw8oxjjfi51"), Br(),
                    A("Gender", href="https://padlet.com/MissRenault/gender-q8now2iguykdi1jn"), Br(),
                    A("Feeding the world", href="https://padlet.com/MissRenault/feeding-the-world-health-jhh138amd2nn"), Br(),
                    A("Racism", href="https://padlet.com/MissRenault/racism-fhk2l78co4k1"), Br(),
                    A("Democracies", href="https://padlet.com/MissRenault/us-democracy-32jx9gg7ojjfy5rw"), Br(),
                    A("Health", href="https://padlet.com/missrenault1/health-cffkcpjpxls39ock"), Br(),
                    A("Work", href="https://padlet.com/missrenault1/work-jpbbwgyimzx0m0mk"), Br(),
                    A("Méthodo concours", href="https://padlet.com/justinehelenarenault/conseils-concours-j1sxuhsbgfzb15dtl"), Br(),
                    A("Thèmes et corrigés", href="https://padlet.com/justinehelenarenault/des-th-mes-des-th-mes-des-th-mes-aj5b1piqvo795o9p"), Br(),
                    style="padding-left: 25px; padding-right: 30px;"
                )
            )
        ),
    )



if __name__ == "__main__":
    serve()

