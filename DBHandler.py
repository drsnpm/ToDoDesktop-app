import sqlite3


class DBHandler:
    def __init__(self):
        self.con = sqlite3.connect("task.db")
        try:
            self.con.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT,tasktitle TEXT, "
                         "taskdesc TEXT,taskdate TEXT,tasktime TEXT)")
            self.con.commit()
        except Exception as e:
            print(e)

    def insertTask(self, t1):
        taskTouple = [t1.title,t1.desc,t1.date,t1.time]
        try:
            self.con.execute("INSERT INTO tasks(tasktitle, taskdesc, taskdate, tasktime) values(?, ?, ?, ?)", taskTouple)
            self.con.commit()
        except Exception as e:
            print(e)

    def getTasks(self,date):
        cursor = self.con.cursor()
        rows = cursor.execute("SELECT * FROM tasks")
        return rows

    def deleteTask(self,id):
        try:
            cursor = self.con.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ? ", (id))
            self.con.commit()
            # self.update_task_numbers(self.con)
        except Exception as e:
            print(e)

    # def update_task_numbers(self,con):
        # cursor = self.con.cursor()
        # cursor.execute('SELECT COUNT(*) FROM tasks')
        # self.con.commit()


        # cursor = self.con.cursor()
        # cursor.execute('UPDATE tasks SET id = id - 1 WHERE id > (SELECT id FROM tasks ORDER BY id DESC LIMIT 1)')
        # self.con.commit()
        #


        # cursor = self.con.cursor()
        # cursor.execute('SELECT id FROM tasks ORDER BY id')
        # tasks = cursor.fetchall()
        # for index, task in enumerate(tasks, start=1):
        #     cursor.execute('UPDATE tasks SET id = ? WHERE id = ?', (index, task[0]))
        # self.con.commit()





