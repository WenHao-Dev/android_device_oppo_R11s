#
# Copyright (C) 2025 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from sdm660-common
$(call inherit-product, device/oppo/sdm660-common/common.mk)

# Inherit the proprietary files
$(call inherit-product, vendor/oppo/R11s/R11s-vendor.mk)

# Overlays
PRODUCT_PACKAGES += \
    FrameworkResOverlayR11s

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)
