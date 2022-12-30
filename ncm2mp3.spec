# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['ncm2mp3.py'],
    pathex=[],
    binaries=[],
    #datas: Pyinstaller 打包添加 customtkinter 作为自定义数据目录，否则打包报错
    datas=[('d:\\pproject\\qmcflac2mp3\\venv\\lib\\site-packages\\customtkinter', 'customtkinter\\')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
a.datas += [('icon.ico','D:\\Pproject\\qmcflac2mp3\\icon.ico','DATA')]
#a.datas 添加程序图标 icon
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ncm2mp3',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    #icon 添加程序图标 icon
    icon='D:\\Pproject\\qmcflac2mp3\\icon.ico'
)