class DebugManager(BaseManager):

    def do_export(self, rows):
        for row in rows:
            print("{}".format(row))
            


