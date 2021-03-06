# Copyright 2022 kaigonzalez
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys


NAME="accept"
TYPE='full-lib'

def accept_flush(args):
    i = 0;
    while (i < args[0]):
        sys.stdout.flush()
        i += 1
    if args[1] == True:
        print("accept: Flushed " + str(args[0]) + " times")

rcfg_registers = {
    'flush': accept_flush
}