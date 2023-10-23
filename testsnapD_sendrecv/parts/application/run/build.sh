#!/bin/bash
set -euo pipefail
source /home/masahiro/06.Customer/01.SSS/QA/TwoWayFileShare/testsnapD_sendrecv/parts/application/run/environment.sh
set -x
cp --archive --link --no-dereference . "/home/masahiro/06.Customer/01.SSS/QA/TwoWayFileShare/testsnapD_sendrecv/parts/application/install"
