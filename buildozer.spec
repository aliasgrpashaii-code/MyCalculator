[app]
title = My Calculator
package.name = mycalculator
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

android.api = 36
android.minapi = 24
android.ndk = 28c
android.archs = arm64-v8a, armeabi-v7a
android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
