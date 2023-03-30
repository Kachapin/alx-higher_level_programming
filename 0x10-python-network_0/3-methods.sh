#!/bin/bash
# shows Http methods 
curl -sI -X OPTIONS "$1" | sed -n '/Allow/p' | cut -b 8-
