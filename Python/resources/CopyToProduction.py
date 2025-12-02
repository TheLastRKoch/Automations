import subprocess
class CopyToProduction:
    '''
    This method funcion as a bridge to execute windows commands in a easy way
    '''

    def ExecuteCommand(self, Command):
        subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",
                         Command])

    def DefineLocations(self):
        return ["C:\\Users\\TheLastRkoch\\Source\\Offline\\Python\\Scripts\\",
                "C:\\Users\\TheLastRkoch\\Source\\Github\\Scripts\\"]

    def CopyToProductionFolder(self, Location):
        Query = "cp "+Location+"*py C:\\Scripts\\"
        print(Query)
        CTP.ExecuteCommand(Query)

    def Menu(self):
        self.ExecuteCommand('cls')
        print('Sending to Production...\n')

if __name__ == "__main__":
    CTP = CopyToProduction()
    CTP.Menu()
    for val in CTP.DefineLocations():
        CTP.CopyToProductionFolder(val)
    print('\nDone !!!\n')

