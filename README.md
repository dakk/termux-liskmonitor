# termux-liskmonitor

A monitor script for the android termux env with push notifications.


## Installation

- Install termux for Android: https://play.google.com/store/apps/details?id=com.termux
- Install termux api: https://play.google.com/store/apps/details?id=com.termux.api
- ```curl https://raw.githubusercontent.com/dakk/termux-liskmonitor/master/install.sh | sh```
- Add the termux shortcuts widget in your home screen

Edit $HOME/termux-liskmonitor/liskmonitor and modify:
```
NODE = "ip:port"
DELEGATE = "delegatename"
DELEGATE_ADDRESS = "delegate_lisk_address"
```


## Start

From the termux shortcuts widget you will see two scripts:
- lm.sh: check the node / delegate every minute
- lm_os.sh: check the node /delegate one time
