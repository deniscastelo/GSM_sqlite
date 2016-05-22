import sys,os
import win32api
from cx_Freeze import setup,Executable
from ControleVersao.CtrlVersao import *



pywintypes_dll = 'pywintypes{0}{1}.dll'.format(*sys.version_info[0:2])
include = ['style.css',(os.path.join(win32api.GetSystemDirectory(), pywintypes_dll), pywintypes_dll),'Imagens','versao.json']
packages = ['Telas','ControleVersao','Componentes']

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name='GSM',
      version=getVersion(),
      includes=include,
      author='Denis Castelo de Lima',
      description='Gerador de Etiqueta para Produtos Hans',
      options={'build_exe':{'include_files':include,'packages':packages}},
      executables = [Executable("GSM.py",base=base)])

