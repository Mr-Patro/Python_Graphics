import subprocess
data=subprocess.check_output(['nets','wlan','show','profiles']).decode('utf-8',error="backslashreplace").split("\n")
profiles=[i.split(":")[1][1:-1]for i in data if "All user profile" in i]
for i in profiles:
            try:
                result=subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('utf-8',errors="backslashreplace").split('\n')
                results=[b.split(":")[1][1:-1]for b in result if "key content" in b]
                try:
                    print("{:<30}|{:<}".formate(i,results[0]))
                except indexerror:
                        print("{:<30}|{:<}".formate(i,""))
                except subprocess.calledprocesserror:
                        print("{:<30}|{:<}".formate(i,"encoding error"))
                input("") 
