#!/usr/bin/env python3
# Copyright (c) 2017 The Bitcoin Pizza developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from test_framework.script import *
from test_framework.util import *

pubkeys = [
    [ "03c894fa067707f621cd7e7a0a6c16086eb23ffebb1ee06beab9d70c2c902e650e", "0219cd458d9a3494ded17d373db741f5271d360cfedb6cfd168e745e22b3524992", "03562ee227896a630fa6a921f23ceec1a2824c4d3eaf9d67fd52790dd7e3c4c6d3", "02051188a9c99bafca5b3ca511af232bc32b78c8b45b6943d74771857880ad8cfc", "026902afaf00a07af7e987375178eb95c96d35aa1cd171b6ef8c03aa27c94a121e", "03882cd9d60b8e9b5f5700cbb8dbf73d60cf292156f7959926380cca66218d2921"  ],
    [ "03edbc1eb8ab9ac40ee9365f9c3be20e8e435714edd47c627e00d6fed89ae6b8d7", "025476b2550def4512ae609af511ac0f27e074f63831a48bfb028cd2c091b207a4", "03117b020cf757bdffb571f92d798cd3537d2609dbf14cdd511c61ecc52cfe8be7", "0255e488de2371e2d8acdccfe642a0480802d2a9c85b59b31f401183522d8b3d66", "02752f63f566c497079c0fdb59e2341d5bcb89eb3d400e75fb4b1efb79c2db080b", "026ced89f10fa5207aa407130d8b99df78fd4b83d0f88ea6ed832a341f4de8caa9"  ],
    [ "026448c5da717a7a0614bc5b9be6f71d4a247a379f2972d3f9ab7c7503dca88f3e", "02ce49f173ed2ffe78ea6a4ef4fcfcb3cf4c16d81e000e09b380587fee92bbd1ce", "02614c4954703e343ad4f65cd85b294de9f16d015caf133aac43c832a3d25e5671", "03d2f24b4d6e6c5811751bf994064c43c8c8f5c73342f5eb6c67d021c7e26cfcd1", "03ad408c294c53ff6e3cc0fc53aafacbb5d27106d44de0e76909c30e604017e4e8", "02da380a8ece3fae59845069d7438e847952f5b73e7774656a386b80613be8700c"  ],
    [ "0368b5c06d666d677eaf117da02105c3f0f5e7635fc2713069cac6a21596e9130e", "029b6f1924fc3dc816b953702de56d2fbdb63f9cfe2084f8c770327a3114a376b4", "0254c15dc6327ec8bcb1b1949dc13e952feeeb1bac3d4e41f627facd5c40b96472", "032a61da700b0092dae4ce419bc4bca76dfd2e640cf6a721b35cbe6160bd7bd7e4", "023199d443676e3b06b357fe58f30daa425f2c75e18283d6d785a909343bd44800", "02682546f1532d85b9887230a487e9be1b091e4cae88a5ae1b1a4e497da5b39d5a"  ],
]

if __name__ == '__main__':
    for keys in pubkeys:
        script = CScript([4, hex_str_to_bytes(keys[0]), hex_str_to_bytes(keys[1]), hex_str_to_bytes(keys[2]), hex_str_to_bytes(keys[3]), hex_str_to_bytes(keys[4]), hex_str_to_bytes(keys[5]), 6, OP_CHECKMULTISIG])
        print(script.hex())
