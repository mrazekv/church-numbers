# Zastaralé návody
(není třeba, pokud budeme používat jiný WiFi router)

Snížení počtu přístupů na kartu
-------------
Zdroj: https://medium.com/@andreas.schallwig/how-to-make-your-raspberry-pi-file-system-read-only-raspbian-stretch-80c0f7be7353

    sudo apt-get remove --purge wolfram-engine triggerhappy anacron logrotate dphys-swapfile xserver-common lightdm
    sudo apt-get autoremove --purge
    sudo systemctl disable bootlogs
    sudo systemctl disable console-setup
    sudo apt-get install busybox-syslogd
    sudo dpkg --purge rsyslog

Edit the file /boot/cmdline.txt and add the following three words at the end of the line: fastboot noswap ro

Nastavení WiFi přístupového bodu
-----------
Nastavení přístupového bodu vychází z tohoto [návodu](https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md). Budou se nastavovat dva balíčky *dnsmasq*, který se stará zejména o DHCP adrey; a o *hostapd*, který dělá WiFi AP.

    sudo nano /etc/dhcpcd.conf

A na konci do souboru zapíšeme text

    interface wlan0
        static ip_address=192.168.4.1/24
        nohook wpa_supplicant

Zazálohujeme a vytvoříme nový konfigurační soubor pro adresu rozashu

    sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.old
    sudo nano /etc/dnsmasq.conf

Do souboru vložíme text

    interface=wlan0      # Use the require wireless interface - usually wlan0  
        dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h

Pro nastavení WiFi vytvoříme další konfigurační soubor
   
    sudo nano /etc/hostapd/hostapd.conf

Do kterého vložíme

```config
interface=wlan0
driver=nl80211
ssid=NaseSit
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=NaseHesloKtereByMeloBytTajne
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
```

Změnou parametru na `ignore_broadcast_ssid=1` naši síť potom skryjeme. Potom musíme systému v souboru 
     
    sudo nano /etc/default/hostapd

říct, kde najde konfiguraci úpravou následujícího řádku

    DAEMON_CONF="/etc/hostapd/hostapd.conf"

Nyní potřebné služby aktivujeme a spustíme

    sudo systemctl enable hostapd.service
    sudo systemctl enable dnsmasq.service
    sudo service hostapd start
    sudo service dnsmasq start




    sudo systemclt status hostapd.service
    # mělo by vrátit "masked"
    sudo systemctl unmask hostapd.service
    # nyní by odkaz neměl být nulový
    sudo ls -l /lib/systemd/system/hostapd.service



