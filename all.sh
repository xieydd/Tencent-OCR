#!/bin/bash
i=2
while [ `ls /Users/xieyuandong/Downloads/photo/json/ | wc -l` -ne 100 ];
do
    python ocr-tencent.py > ocr${i}.log
    ((i++))
done