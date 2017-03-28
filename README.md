# Purpose

This repository was created in order to share tools with other students who want to test their implementation of a 4 stage pipelined architecture against random ARM Thumb assembly code.

# Intended Audience

The intended audience and users of this code are students taking EECE320 at CSU Chico and who are having a tough time diagnosing RAW hazards in their implementation.

# Contents

You will find the following in this repository:
- [generate-data.py](https://github.com/califrench/ecee320/blob/master/generate-data.py) which is a tool to generate random assembly code with potential data hazards. It's not guaranteed that all the possible data hazards will be included in the code.
- [generate.py](https://github.com/califrench/ecee320/blob/master/generate.py), a tool to generate random assembly code with data hazards as well as control hazards. Since the code is random, you may run into infinite loops.
- [data-hazard-test.s](https://github.com/califrench/ecee320/blob/master/data-hazard-test.s), an already generated assmebly file with all the possible data hazards.
- [branch.s](https://github.com/califrench/ecee320/blob/master/branch.s), an assembly file that contains several branch instructions. Note: this does not contain all possible branch instructions but all control hazards are resolved in the same way regardless of the branch condition. This has been verified to not contain any infinite loops.

