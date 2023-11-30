#!/usr/bin/env bash

set -ex

# bots

gh repo sync KumaTeaBot/KumaTea-bot --force --branch master
gh repo sync KumaTeaBot/NextBot     --force
gh repo sync KumaTeaBot/EvalBot     --force
gh repo sync KumaTeaBot/daka        --force

# py projects

gh repo sync KumaTeaBot/pypy-wheels --force

# others

gh repo sync KumaTeaBot/blog        --force
