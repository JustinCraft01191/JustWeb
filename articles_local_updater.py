import json

class Updater:

    def __init__(self):

        with open("static/articles/coconut.json", "r") as f_coconut:
            self.coco = json.loads(f_coconut.read())["articles"]
        self.coco_length = len(self.coco)
        if self.coco_length > 3:
            self.coco_length = 3

        with open("static/articles/palm.json", "r") as f_palm:
            self.palm = json.loads(f_palm.read())["articles"]
        self.palm_length = len(self.palm)
        if self.palm_length > 3:
            self.palm_length = 3

    def palm_preview_update(self):
        return self.palm[0:self.palm_length]

    def coconut_preview_update(self):
        return self.coco[0:self.coco_length]

    def palm_articles(self):
        return self.palm

    def coconut_articles(self):
        return self.coco