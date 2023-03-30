#!/bin/bash
# shows Http methods 
curl -s -H "Content-type: application/json" -X POST -d @"$2" "$1"
