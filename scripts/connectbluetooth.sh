#!/bin/bash

DEVICE=$(bluetoothctl paired-devices | grep Device |awk '$1=""; {print $0}'| sort -r | dmenu) 
MAC=$(echo $DEVICE | awk '{print $1}')

bluetoothctl disconnect $MAC 
bluetoothctl connect $MAC 