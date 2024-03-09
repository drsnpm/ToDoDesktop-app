from DBHandler import *


class Task:

    def __init__(self,title, desc, date, time):
        self.title = title
        self.desc = desc
        self.date = date
        self.time = time

    def __str__(self):
        return (self.title + ":" + self.desc + ":" + self.date + ":" + self.time)

#if __name__ == '__main__':
 #   t = Task("hi","do perfect","22-05-2023","08:40:00 AM")
 #   db = DBHandler()
 #   db.insertTask(t)


