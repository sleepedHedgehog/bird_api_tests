class DBConnection:

    def __init__(self):
        self.connect = ''
        self.cursor = ""

    def get_bird_by_id(self, bird_id):
        return self.cursor.exec(f'select * from birds where bird_id={bird_id}')

    def get_bird_description_by_id(self, bird_id):
        return self.cursor.exec(f'select * from bird_description where bird_id={bird_id}')

    def get_cat_by_id(self, cat_id):
        return self.cursor.exec(f'select * from cats where cat_id={cat_id}')

    def get_cat_description_by_id(self, cat_id):
        return self.cursor.exec(f'select * from cat_description where cat_id={cat_id}')
