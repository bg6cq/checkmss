for h in `cat host.txt`; do python3 checkmss.py -4 $h 80; done | sort -k3 -n > ipv4.txt 
for h in `cat host.txt`; do python3 checkmss.py -6 $h 80; done | sort -k3 -n > ipv6.txt 

