# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['formulario_libros_leidos.py'],
             pathex=['C:\\Users\\Marcelo\\Desktop\\Programación\\pildorasinformaticas_python\\proyecto_bbdd_libros'],
             binaries=[],
             datas=[('resources/libros.gif', 'resources'), ('resources/libros_icono.ico', 'resources')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='formulario_libros_leidos',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='resources\\icono_windows.ico')
