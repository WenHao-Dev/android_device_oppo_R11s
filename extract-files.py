#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/oppo/R11s',
    'device/oppo/sdm660-common',
    'hardware/qcom-caf/sdm660',
    'vendor/oppo/sdm660-common'
]

blob_fixups: blob_fixups_user_type = {
    (
        'vendor/lib64/android.frameworks.fingerprintservice@1.0.so',
        'vendor/lib64/vendor.oppo.hardware.commondcs@1.0.so',
        'vendor/lib64/vendor.qti.hardware.fingerprint@1.0.so'
    ): blob_fixup()
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'R11s',
    'oppo',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(module, 'sdm660-common', module.vendor)
    utils.run()
