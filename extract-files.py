#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/samsung/gta4xl-common',
    'hardware/samsung',
    'hardware/samsung_slsi-linaro/exynos',
    'hardware/samsung_slsi-linaro/graphics',
    'vendor/samsung/gta4xl-common',
]

blob_fixups: blob_fixups_user_type = {
    (
        'vendor/lib64/hw/android.hardware.gnss@2.1-impl.so',
        'vendor/lib64/hw/android.hardware.gnss@2.0-impl.so',
        'vendor/lib64/hw/vendor.samsung.hardware.gnss@2.0-impl.so',
    ): blob_fixup()
        .remove_needed('libhidltransport.so'),
    'vendor/lib64/libsec-ril.so': blob_fixup()
        .sig_replace('80 0E 40 F9 E1 03 16 AA 82 0C 80 52 E3 03 15 AA',
            '80 0E 40 F9 E1 03 16 AA 82 0C 80 52 08 00 80 D2')
        .replace_needed('libprotobuf-cpp-full-21.7.so', 'libprotobuf-cpp-full-21.7-u.so'),
} # fmt: skip

module = ExtractUtilsModule(
    'gta4xl',
    'samsung',
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=True,
    blob_fixups=blob_fixups,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'gta4xl-common', module.vendor
    )
    utils.run()
