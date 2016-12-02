git clone https://github.com/dakk/termux-liskmonitor $HOME/termux-liskmonitor
cd $HOME/termux-liskmonitor
apt install python termux-api termux-tools
pip install requests
nano liskmonitor.py
cp shortcuts/* $HOME/.shortcuts
echo Done.
