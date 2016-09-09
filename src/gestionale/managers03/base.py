from .decori import debugme 


class BaseManager(object):

    def __init__(self, debug=False):
        """Init with debug mode on/off."""

        self.fname = fname
        self.debug = debug

    def _do_export(self, rows):
        """
        Do the import job from the specific backend

        WARNING: self.f MUST be an object that
        supports the "write()" method in this phase.
        """
        raise NotImplementedError(
            "To be implemented in subclasses")

    def _do_import(self):
        """
        Do the export job from the specific backend

        WARNING: self.f MUST be an object that
        supports the "write()" method in this phase.
        """
        raise NotImplementedError(
            "To be implemented in subclasses")

    def get_output(self):
        raise NotImplementedError(
            "To be implemented in subclasses")

    def debug_export(self, rows):
        
        if self.debug:
            print(self.get_output(rows)

    def debug_import(self, rows):

        if self.debug:
            print(rows)


class BaseFileManager(BaseManager):

    def __init__(self, fname, debug=False):
        """Init with filename and debug mode on/off."""

        self.fname = fname
        super(BaseFileManager, self).__init__(debug=debug)

    @debugme(kind="export")
    def do_export(self, rows):
        """
        Do the export operation.

        Print data output if object is in debug mode.
        """

        with open(self.fname, "wb") as self.f:
            return self._do_export(rows)

    @debugme(kind="import")
    def do_import(self):
        with open(self.fname, "rb") as self.f:
            rows = self._do_import()

        return rows


