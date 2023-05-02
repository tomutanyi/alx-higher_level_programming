#!/bin/bash
#script checks if url argument is provided
curl -s "$1" | wc -c
