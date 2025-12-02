import subprocess
import webbrowser

'''
    @Name: Laravel Setting Project
    @Author: http://github.com/TheLastRKoch
    @Version: 1.3.5
'''

class SettingProject(object):

    MenuLevel = 0

    '''
    This method add chars to make a better view
    '''
    def AddSpacer(self, Num, Char):
        Bar = '\n'
        for i in range(Num):
            Bar += Char
        print(Bar+'\n')

    '''
    This method funcion as a bridge to execute windows commands in a easy way
    '''
    def ExecuteCommand(self, Command):
        subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",
                         Command])

    '''
    This method clear the screen
    '''
    def ClearScreen(self):
        self.ExecuteCommand("cls")

    def PressKeyContinue(self):
        input("Press Enter to continue...\n")
        self.AddSpacer(100, "-")

    def Banner(self, ModeName):
        self.ClearScreen()
        print('\n\tWelcome to TheLastRKoch Laravel Setting tool')
        self.AddSpacer(70, '=')
        print('\t--'+ModeName+'--\t')

    '''
    This method show the main message
    '''
    def Greeting(self):
        self.Banner('Start')
        print('\nThis Scritp generate all the configuration to create a new laravel project\n')
        print('\n1) Download XAMMP on https://www.apachefriends.org/es/index.html\n')
        print('\n2) Install composer on https://getcomposer.org/ and add it on PATH\n')
        print('\n3) Install Larave with the command composer global require "laravel/installer=~1.1"\n')
        print('\n4) Add laravel to PATH C:\\Users\\<Your_User>\\AppData\\Roaming\\Composer\\vendor\\bin"\n')
        print('\nYou are right now on: ')
        self.ExecuteCommand('pwd')
        print('Important note: U must run this script from C:\\xampp\\htdocs\n')
        self.AddSpacer(100,'-')

    '''
    This method Show the menu and ask for everything
    '''
    def Menu(self):
        self.Greeting()
        resp = input ('\nIt\'s everything really ? (y/n)\n')
        if resp == 'y':
            self.Greeting()
            return input ('\nWrite the name of the project:\n')
        print('\nSee u later !!!\n')
        return None

    '''
    This method show all the options
    '''
    def OptionSelector(self):
        self.Banner('Options')
        print('\nThis tool has the next functionalities\n')
        print('\n1) Initialize a new project\n')
        print('\n2) Install a cloned project\n')
        return input('Choose the operation to make\n')


    def InstallDependecys(self):
        self.Banner('Install a cloned project')
        self.ClearScreen()
        print('Starting process...\n')
        self.ExecuteCommand('composer update --no-scripts')
        self.PressKeyContinue()

    def RenameEnvFile(self):
        self.ExecuteCommand('ren .\.env.example .env')

    def GenerateKey(self):
        self.Banner('Install a cloned project')
        self.ExecuteCommand('php artisan key:generate')
        print('\nDone !!!\n')
        self.PressKeyContinue()

    '''
    This method create the project with laravel
    '''
    def CreateProject(self, ProjectName):
        self.Greeting()
        resp = input('\nDid u create your project ? (y/n)\n')
        if resp == 'n':
            self.ExecuteCommand('laravel new ' + ProjectName)
            self.PressKeyContinue()
        else:
            print('Ok (y) cool')

    '''
    This method Generate the config for vhost on XAMPP
    '''
    def GenerateVhostsInfo(self, Location, ProjectName):
        self.Greeting()
        ProjectName = ProjectName.lower()
        Location = 'C:\\xampp\\apache\\conf\\extra\\httpd-vhosts.conf'
        Query = 'notepad '+Location
        self.ExecuteCommand(Query)
        print('\n1) Copy the next code at the end of '+Location+'\n')
        print('<VirtualHost '+ProjectName+'.local:80>\r')
        print('\tServerAdmin '+ProjectName+'.local\r' )
        print('\tDocumentRoot \'C:\\xampp\\htdocs\\'+ProjectName+'\\public\'\r' )
        print('\t<Directory \'C:\\xampp\\htdocs\\'+ProjectName+'\'>\r' )
        print('\t\tOptions Indexes FollowSymLinks\r' )
        print('\t\tAllowOverride All\r' )
        print('\t\tRequire all granted\r' )
        print('\t</Directory>\r' )
        print('</VirtualHost>\r' )
        print('\n')
        self.PressKeyContinue()

    '''
    This method Generate the config for windows hots
    '''
    def GenerateHostConfig(self, Location, ProjectName):
        self.Greeting()
        ProjectName = ProjectName.lower()
        Location = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
        Query = 'notepad '+Location
        self.ExecuteCommand(Query)
        print('\n2) Copy the next code at the end of '+Location+'\n\n')
        print('#'+ProjectName+' host')
        print('127.0.0.1 '+ProjectName+'.local\n')
        self.PressKeyContinue()

    '''
    This method show the message for XAMPP
    '''
    def RefreshXAMMP(self):
        self.Greeting()
        print('\n3) Now close and open XAMP remember shotdown all the services first\n')
        self.PressKeyContinue()

    '''
    This method open the Project URL on the webbrowser
    '''
    def OpenSite(self,ProjectName):
        self.Greeting()
        Url = ProjectName+'.local/'
        print('\n4) Open the next URL on a web browser: '+Url)
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(Url)
        self.AddSpacer(100, "-")

'''
Main method
'''
if __name__ == "__main__":
    Setting = SettingProject()
    ProjectName = Setting.Menu()
    if ProjectName is not None:
        if Setting.OptionSelector() == '1':
            Setting.CreateProject(ProjectName)
            Setting.GenerateVhostsInfo("", ProjectName)
            Setting.GenerateHostConfig("", ProjectName)
        else:
            Setting.InstallDependecys()
            Setting.RenameEnvFile()
            Setting.GenerateKey()
        Setting.RefreshXAMMP()
        Setting.OpenSite(ProjectName)
