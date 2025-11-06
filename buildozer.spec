[app]
title = TransformApp
package.name = transformapp
package.domain = org.kivy
source.dir = .
source.include_exts = py,kv,json,xlsx
version = 1.0
requirements = python3,kivy,openpyxl
orientation = portrait
fullscreen = 0
android.api = 33
android.minapi = 27
android.ndk = 25b
android.archs = arm64-v8a
android.entrypoint = org.kivy.android.PythonActivity
log_level = 2
android.allow_backup = True
