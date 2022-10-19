class FileOps:
    FileObj=None

    #returns file as string
    @staticmethod
    def readFileAsStr(Path, mode):
        FileObj=open(Path, mode)
        return FileObj.read()