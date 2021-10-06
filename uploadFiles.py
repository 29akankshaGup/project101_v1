from posixpath import relpath
import dropbox
from dropbox.files import WriteMode;
import os;

class TransferData:
    def __init__(self,accessToken):
        self.accessToken=accessToken;
    
    def upload_files_to_dropbox(self,file_to,file_from):
        dbx=dropbox.Dropbox(self.accessToken);
        #f=open(file_from,'rb');
        #dbx.files_upload(f.read(),file_to,mode=files.WriteMode.add);
        
        for root, dirs, files in os.walk(file_from):

            for fileName in files:
                filePath=os.path.join(root,fileName);
                relPath=os.path.relpath(filePath,file_from);

                f=open(filePath,'rb');
                dest_Path=os.path.join(file_to,relPath);
                print(dest_Path);
                dbx.files_upload(f.read(),dest_Path,mode=WriteMode("overwrite"));



def main():
    accessToken='sl.A50ZGqjiMMOI7gRSlrtGdPNwuiAroy0siKmFrLz6tFywIPeOzuTskpINeOG46Egpk52NN0L8My_dGJezbTZCFOF6YjTVAy01MY0Hht11Lfg1P-lXbPjH_YBOVezPsZyFwwXPm8o';
    obj=TransferData(accessToken);

    file_from=input("Please enter folder path to upload:");
    file_to=input("Enter Dropbox destination path");
    obj.upload_files_to_dropbox(file_to,file_from);
    


if __name__=='__main__':
    main();