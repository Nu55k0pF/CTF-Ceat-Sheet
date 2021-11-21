#!/bin/bash
killall nc 2> /dev/null
nc -klvvp $1 &
