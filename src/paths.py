PATHS_SLOUP = {
    "url_level": "https://hydro.chmi.cz/hppsoldv/hpps_prfdata.php?seq=38908612",
    "xpath_l_table": "/html/body/div[1]/div[3]/div/table[2]/tr[3]/td/div/table",
    "xpath_l_table_extended": "/html/body/div[1]/div/div/table[2]/tr[4]/td/div/table",
    "file_reports": "data/reports_sloup.csv",
}

PATHS_TRAM = {
    "url_salina_center": "https://idos.idnes.cz/vlakyautobusymhdvse/spojeni/vysledky/?f=Vojensk%C3%A1%20nemocnice&fc=302003&t=Jugosl%C3%A1vsk%C3%A1&tc=302003",
    "url_salina_out": "https://idos.idnes.cz/vlakyautobusymhdvse/spojeni/vysledky/?f=Vojensk%C3%A1%20nemocnice&fc=302003&t=Kuldova&tc=302003",
    "xpath_first_num": "/html/body/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div/a/div/div/h3/span",
    "xpath_first_num": "/html/body/div[2]/div/div/div",
}

PATHS = {"SLOUP": PATHS_SLOUP, "TRAM": PATHS_TRAM}
