[app]

# (str) Title of your application
title = Cache Direto

# (str) Package name
package.name = cachedireto

# (str) Package domain (needed for android/ios packaging)
package.domain = org.cachedireto

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,kivymd,pillow,sdl2
# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use (usar a versão 25b para evitar o erro da r28c)
android.ndk = 25b

# (str) Android NDK integration
android.ndk_api = 21

# (bool) Use --private data directory (True) or --dir public storage (False)
android.private_storage = True

# (bool) Accept all SDK licences requested by buildozer tools
android.accept_sdk_license = True

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = disable)
warn_on_root = 1
