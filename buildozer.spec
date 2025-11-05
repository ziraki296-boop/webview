[app]
title = TransformApp
package.name = transformapp
package.domain = org.kivy
source.dir = .
source.include_exts = py,kv,json,xlsx
version = 1.0
orientation = portrait
fullscreen = 0
log_level = 2
android.allow_backup = True

# Entry point aplikasi (main.py)
source.main = main.py

# Dependencies / library Python yang diperlukan
requirements = python3,kivy,openpyxl

# Platform Android
android.api = 33
android.minapi = 27
android.ndk = 25b
android.archs = arm64-v8a

# Activity utama
android.entrypoint = org.kivy.android.PythonActivity

# Tambahan opsional (biar build lebih stabil)
p4a.branch = master
android.gradle_dependencies = androidx.appcompat:appcompat:1.4.1
android.sdk_path = /usr/lib/android-sdk
