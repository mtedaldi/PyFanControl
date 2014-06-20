Munin-Node
==========

A munin-node module to track the temperature of an MCP9808
temperature sensor attached vi i2c.

Files:
temperature - the shell script that is called by munin-node
temperature.py - the python program that reads and returns the temperature
99-temperature.conf - a config file to be placed in /etc/munin/plugin-conf.d
rpm - shell script called by munin-node that return the fan speed

Installation:
copy rpm, temperature and temperature.py to
/usr/share/munin/plugins
Change settings in temperature.py to meet your needs

make a symlink from /etc/munin/plugins/ to /usr/share/munin/plugins/temperature
make a symlink from /etc/minin/plugins/ to /usr/share/munin/plugins/rpm
copy 99-temperature.conf to /etc/munin/plugin-conf.d

restart munin-node


