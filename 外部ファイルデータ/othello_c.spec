# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['othello_c.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\oonoy\\OneDrive\\デスクトップ\\othello_cus\\dist\\EXITボタン.png', '.'), ('C:\\Users\\oonoy\\OneDrive\\デスクトップ\\othello_cus\\dist\\haikei_renga.png', '.'), ('C:\\Users\\oonoy\\OneDrive\\デスクトップ\\othello_cus\\dist\\OPTIONボタン.png', '.'), ('C:\\Users\\oonoy\\OneDrive\\デスクトップ\\othello_cus\\dist\\othello_black.png', '.'), ('C:\\Users\\oonoy\\OneDrive\\デスクトップ\\othello_cus\\dist\\othello_icon.ico', '.'), ('C:\\Users\\oonoy\\OneDrive\\デスクトップ\\othello_cus\\dist\\othello_tail.png', '.'), ('C:\\Users\\oonoy\\OneDrive\\デスクトップ\\othello_cus\\dist\\othello_tail1.png', '.'), ('C:\\Users\\oonoy\\OneDrive\\デスクトップ\\othello_cus\\dist\\othello_wall.png', '.'), ('C:\\Users\\oonoy\\OneDrive\\デスクトップ\\othello_cus\\dist\\othello_white.png', '.'), ('C:\\Users\\oonoy\\OneDrive\\デスクトップ\\othello_cus\\dist\\PLAYボタン.png', '.'), ('C:\\Users\\oonoy\\OneDrive\\デスクトップ\\othello_cus\\dist\\spo_ge_osero02.mp3', '.'), ('C:\\Users\\oonoy\\OneDrive\\デスクトップ\\othello_cus\\dist\\ビープ音4.mp3', '.'), ('C:\\Users\\oonoy\\OneDrive\\デスクトップ\\othello_cus\\dist\\歓声と拍手.mp3', '.'), ('C:\\Users\\oonoy\\OneDrive\\デスクトップ\\othello_cus\\dist\\決定ボタンを押す1.mp3', '.'), ('C:\\Users\\oonoy\\OneDrive\\デスクトップ\\othello_cus\\dist\\決定ボタンを押す7.mp3', '.'), ('C:\\Users\\oonoy\\OneDrive\\デスクトップ\\othello_cus\\dist\\決定ボタンを押す35.mp3', '.')],
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
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='othello_c',
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
    icon=['C:\\Users\\oonoy\\Downloads\\othello_icon.ico'],
)
