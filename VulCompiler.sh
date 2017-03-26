#!/bin/bash

gcc $1 -o $2 -zexecstack -fno-stack-protector -g
