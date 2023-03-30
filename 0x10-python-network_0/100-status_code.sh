#!/bin/bash
# shows Http methods 
curl -s -o /dev/null -I -w "%{http_code}" "$1"
