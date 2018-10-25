#!/usr/bin/env bash

chmod 600 Hackathon_AWS_Key_Pair.pem
ssh -i Hackathon_AWS_Key_Pair.pem ubuntu@52.208.11.95
