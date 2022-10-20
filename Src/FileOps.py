class FileOps:
    FileObj=None

    #returns file as file obj
    @staticmethod
    def openFile(Path, mode):
        FileObj=open(Path, mode)
        return FileObj