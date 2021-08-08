import nmap
import sys

nm_scan = nmap.PortScanner()
nm_scanner = nm_scan.scan(sys.atgv[1], '80' ,arguments='-O')

print (nm_scanner)