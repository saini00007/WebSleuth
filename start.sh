#!/bin/bash

# Function to print "Domain Checker" in a big format with blue color
print_big_header() {
    echo -e "\033[35;5;1m 
 __          __  _      _____ _            _   _     
 \ \        / / | |    / ____| |          | | | |    
  \ \  /\  / /__| |__ | (___ | | ___ _   _| |_| |__  
   \ \/  \/ / _ \ '_ \ \___ \| |/ _ \ | | | __| '_ \ 
    \  /\  /  __/ |_) | ___) | |  __/ |_| | |_| | | |
     \/  \/ \___|_.__/ _____/|_|\___|\__,_|\__|_| |_|
                                                                              
\033[0m"
    echo -e "\033[31;1m
          __                     __ __        _                       __                      ___       
|  | _|_ (_ | _   |_|_   .  |  ||_ |__)  | _ (_ _  _ _  _ |_. _  _   / _  _ |_|_  _ _. _  _    | _  _ | 
|/\|(-|_)__)|(-|_||_| )  .  |/\||__|__)  || )| (_)| |||(_||_|(_)| )  \__)(_||_| )(-| || )(_)   |(_)(_)| 
                                                                                         _/             

\033[0m"

    echo -e "\033[33;1m[==[[ ->>  Name     :          WebSleuth          <<- ]]==]\033[0m"
    echo
    echo -e "\033[34;1m[==[[ ->>  Telegram :    https://t.me/imnoone07   <<- ]]==]\033[0m"
    echo
    echo -e "\033[35;1m[==[[ ->>  Github   :    github.com/saini00007    <<- ]]==]\033[0m"
    echo
    echo -e "\033[36;1m[==[[ ->>  Author   :           NO_ONE            <<- ]]==]\033[0m"
    echo
    echo -e "\033[37;1m[==[[ ->>  Version  :             1.0             <<- ]]==]\033[0m"
    echo
    echo
}
is_root() {
    if [ "$(id -u)" -eq 0 ]; then
        echo -e "\033[35;5;1m----Warining : Don't use as  root  \033[0m"
        exit
    else
        echo
    fi
}

check_url() {
    if curl --output /dev/null --silent --head --fail "$1"; then
        return 0
    else
        echo -e "\e[91m--->  URL is not reachable. Enter a valid URL or domain name...\e[0m"  # Printing error message in red color
        return 1
    fi
}

# Function to add "http://" to URL if not present
add_http() {
    if [[ $1 != http://* && $1 != https://* ]]; then
        url="https://$1"
    else
        url="$1"
    fi
    echo "$url"  # Print the modified URL
}



who_is() { python3 SRC/who_is.py "$1"; }
location() { python3 SRC/location.py "$1"; }
ssl_info() { python3 SRC/ssl_info.py "$1"; }
DNS_Server() { python3 SRC/DNS_Server.py "$1"; }
DNSSEC() { python3 SRC/DNSSEC.py "$1"; }
HTTP_Security() { python3 SRC/HTTP_Security.py "$1"; }
Security_txt() { python3 SRC/Security_txt.py "$1"; }
Firewall() { python3 SRC/Firewall.py "$1"; }
Block_Detection() { python3 SRC/Block_Detection.py "$1"; }
HSTS() { python3 SRC/HSTS.py "$1"; }
Linked_Pages() { python3 SRC/Linked_Pages.py "$1"; }
Archive() {
    python3 SRC/Archive.py "$1" &
    archive_pid=$!  # Capture the process ID of the background process

    # Wait for 10 seconds
    sleep 10

    # Check if the process is still running
    if ps -p $archive_pid > /dev/null; then
        echo "===================="
        echo -e "\e[1;34mWayback Data \e[0m" 
        echo "===================="
        echo
        echo "Error Finding Wayback Data for Now."
        echo
        kill $archive_pid
    fi
}

header() { python3 SRC/header.py "$1"; }
port_scan() { sudo python3 SRC/port_scan.py "$1"; }
Tech_Stack() { python3 SRC/Tech_Stack.py "$1"; }
Social_tags() { python3 SRC/Social_tags.py "$1"; }
crewl_rules() { python3 SRC/crewl_rules.py "$1"; }
cookies() { python3 SRC/cookies.py "$1"; }
carbon() { python3 SRC/carbon.py "$1"; }
Associated_hosts() { python3 SRC/Associated_hosts.py "$1"; }
DNS_records() { python3 SRC/DNS_records.py "$1"; }
Email_config() { python3 SRC/Email_config.py "$1"; }
features() { python3 SRC/features.py "$1"; }
Quality() { python3 SRC/Quality.py "$1"; }
redirect() { python3 SRC/redirect.py "$1"; }
Server_status() { python3 SRC/Server_status.py "$1"; }
threath() { python3 SRC/threath.py "$1"; }
TLS_Cipher_suites() { python3 SRC/TLS_Cipher_suites.py "$1"; }
TXT_Records() { python3 SRC/TXT_Records.py "$1"; }
web_Stats() { python3 SRC/web_Stats.py "$1"; }

# Function to run all Python scripts with URL as argument
run_all_scripts() {
    url=$1
    who_is "$1" &
    wait 
    location "$1" &
    wait 
    ssl_info "$1" &
    wait 
    DNS_Server "$1" &
    wait 
    DNSSEC "$1" &
    wait 
    HTTP_Security "$1" &
    wait 
    Security_txt "$1" &
    wait 
    Firewall "$1" &
    wait 
    Block_Detection "$1" &
    wait 
    HSTS "$1" &
    wait 
    Linked_Pages "$1" &
    wait 
    Archive "$1" &
    wait 
    header "$1" &
    wait 
    port_scan "$1" &
    wait 
    Tech_Stack "$1" &
    wait 
    Social_tags "$1" &
    wait 
    crewl_rules "$1" &
    wait 
    cookies "$1" &
    wait 
    carbon "$1" &
    wait 
    Associated_hosts "$1" &
    wait 
    DNS_records "$1" &
    wait 
    Email_config "$1" &
    wait 
    features "$1" &
    wait 
    
    redirect "$1" &
    wait 
    Server_status "$1" &
    wait 
    threath "$1" &
    wait 
    TLS_Cipher_suites "$1" &
    wait 

    TXT_Records "$1" &
    wait 
    web_Stats "$1" &
    wait 
    Quality "$1" &
    wait  
}

# Main function
main() {
    is_root 
    

    
        print_big_header

        echo -e "\e[33;1m--->Enter the URL like 'www.example.com' or https://example.com  :\e[0m"
        read url
        if [ "$url" = "exit" ]; then
            echo -e "\e[31;----Exiting...\e[0"
            exit 0
        fi

        modified_url=$(add_http "$url")  # Capture the modified URL
        check_url "$modified_url"
        if [ $? -eq 1 ]; then
            exit 1
        fi

        echo 
        echo
        echo -e "\e[1;31m ----------Choose an option: ----------\e[0m"
        echo
        echo -e "\e[1;32m1. ---> WHO_IS_Info \e[0m"
        echo 
        echo -e "\e[1;33m2. ---> Location_Info\e[0m"
        echo 
        echo -e "\e[1;34m3. ---> SSL_info\e[0m"
        echo 
        echo -e "\e[1;35m4. ---> DNS_Server_Info\e[0m"
        echo 
        echo -e "\e[1;36m5. ---> DNSSEC_Info\e[0m"
        echo 
        echo -e "\e[1;31m6. ---> HTTP_Security_Info\e[0m"
        echo 
        echo -e "\e[1;33m7. ---> Security_txt_Info\e[0m"
        echo 
        echo -e "\e[1;33m8. ---> Firewall_Info\e[0m"
        echo 
        echo -e "\e[1;34m9. ---> Block_Detection_Info\e[0m"
        echo 
        echo -e "\e[1;35m10.---> HSTS_Info\e[0m"
        echo 
        echo -e "\e[1;36m11.---> Linked_Pages_Info\e[0m"
        echo 
        echo -e "\e[1;31m12.---> Archive_Info\e[0m"
        echo 
        echo -e "\e[1;32m13.---> HeaderS_Info\e[0m"
        echo 
        echo -e "\e[1;33m14.---> Port_scan_Info\e[0m"
        echo 
        echo -e "\e[1;34m15.---> Tech_Stack_Info\e[0m"
        echo 
        echo -e "\e[1;35m16.---> Social_tags_Info\e[0m"
        echo 
        echo -e "\e[1;36m17.---> Crewl_rules_Info\e[0m"
        echo 
        echo -e "\e[1;31m18.---> Cookies_Info\e[0m"
        echo 
        echo -e "\e[1;32m19.---> Carbon_Info\e[0m"
        echo 
        echo -e "\e[1;33m20. ---> Associated_hosts_Info\e[0m"
        echo 
        echo -e "\e[1;34m21. ---> DNS_records_Info\e[0m"
        echo 
        echo -e "\e[1;35m22. ---> Email_configuration_Info\e[0m"
        echo 
        echo -e "\e[1;36m23. ---> Features_Info\e[0m"
        echo 
        echo -e "\e[1;31m24. ---> Web_Stats_Info\e[0m"
        echo 
        echo -e "\e[1;32m25. ---> Redirect_Info\e[0m"
        echo 
        echo -e "\e[1;33m26. ---> Server_status_Info\e[0m"
        echo 
        echo -e "\e[1;34m27. ---> Threath_Info\e[0m"
        echo 
        echo -e "\e[1;35m28. ---> TLS_Cipher_suites_Info\e[0m"
        
        echo 
        echo -e "\e[1;31m29. ---> TXT_Records_Info\e[0m"
        echo 
        echo -e "\e[1;32m30. ---> Quality_Info\e[0m"
        echo 
        echo -e "\e[1;33m31. ---> Get all Information\e[0m"
        echo 
        echo -e "\e[1;34m32. ---> Exit\e[0m"
        echo 
        read choice
        case $choice in
            1) who_is "$modified_url";;
            2) location "$modified_url";;
            3) ssl_info "$modified_url";;
            4) DNS_Server "$modified_url";;
            5) DNSSEC "$modified_url";;
            6) HTTP_Security "$modified_url";;
            7) Security_txt "$modified_url";;
            8) Firewall "$modified_url";;
            9) Block_Detection "$modified_url";;
            10) HSTS "$modified_url";;
            11) Linked_Pages "$modified_url";;
            12) Archive "$modified_url";;
            13) header "$modified_url";;
            14) port_scan "$modified_url";;
            15) Tech_Stack "$modified_url";;
            16) Social_tags "$modified_url";;
            17) crewl_rules "$modified_url";;
            18) cookies "$modified_url";;
            19) carbon "$modified_url";;
            20) Associated_hosts "$modified_url";;
            21) DNS_records "$modified_url";;
            22) Email_config "$modified_url";;
            23) features "$modified_url";;
            24)  web_Stats "$modified_url";;
            25) redirect "$modified_url";;
            26) Server_status "$modified_url";;
            27) threath "$modified_url";;
            28) TLS_Cipher_suites "$modified_url";;
        
            29) TXT_Records "$modified_url";;
            30) Quality "$modified_url";;
            31) run_all_scripts "$modified_url";;  # Corrected the function call here
            32) echo "Exiting..."; exit;;
            *) echo -e "\e[31m---------Invalid choice---------\e[0m";;
        esac

       
    
    
}

main
bash pdf.sh "$url"
