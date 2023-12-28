import mysql.connector
import numpy as np
class comboBoxFiller:
    def __init__(self,container):
        self.container = container
        self.dbWorld = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ma77266100$1372mysql",
            database="world"
        )
        self.cursorWorld = self.dbWorld.cursor()
    def fillCountry(self):
        #match page
        matchPageCountryCombo = self.container.ui.matchPageCountryCombo
        matchPageCityCombo = self.container.ui.matchPageCityCombo
        matchPageStadiumCombo = self.container.ui.matchPageStadiumCombo

        self.cursorWorld.execute("SELECT Name FROM country")
        results = np.array(self.cursorWorld.fetchall()).flatten()
        matchPageCountryCombo.addItems(results)
        matchPageCountryCombo.setCurrentIndex(list(results).index("Iran"))



