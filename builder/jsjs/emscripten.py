import os
import sys

EMSCRIPTEN_CONFIG = """########
# This .emscripten file generated by js.js build.py
########
EMSCRIPTEN_ROOT = "%EMSCRIPTEN_ROOT%"
LLVM_ROOT = "%LLVM_ROOT%"
SPIDERMONKEY_ENGINE = ["%SPIDERMONKEY_ENGINE%", '-m', '-n']
NODE_JS = "%NODE_JS%"
V8_ENGINE = "%V8_ENGINE%"
CLOSURE_COMPILER = "%CLOSURE_COMPILER%"
TEMP_DIR = '/tmp'
COMPILER_ENGINE = V8_ENGINE
JS_ENGINES = [NODE_JS, SPIDERMONKEY_ENGINE, V8_ENGINE]
"""

def write_emscripten_config(llvm_root, v8_engine, closure_compiler, emscripten_root,
                            spidermonkey_engine, nodejs_path, dot_emscripten="~/.emscripten"):
    dot_emscripten = os.path.abspath(os.path.expanduser(dot_emscripten))
    
    filled_config = EMSCRIPTEN_CONFIG
    filled_config = filled_config.replace("%EMSCRIPTEN_ROOT%", emscripten_root)
    filled_config = filled_config.replace("%LLVM_ROOT%", llvm_root)
    filled_config = filled_config.replace("%V8_ENGINE%", v8_engine)
    filled_config = filled_config.replace("%SPIDERMONKEY_ENGINE%", spidermonkey_engine)
    filled_config = filled_config.replace("%NODE_JS%", nodejs_path)
    filled_config = filled_config.replace("%CLOSURE_COMPILER%", closure_compiler)
    
    if os.path.exists(dot_emscripten):
        previous_config = open(dot_emscripten, 'r').read()
        if previous_config == filled_config:
            return
        
        choice = raw_input("Emscripten config file ('%s') already exists and will be overwritten. Continue (y/n)? " % dot_emscripten).lower()
        if choice != 'y':
            sys.stderr.write("Okay, nothing to do here then. Exiting.\n")
            sys.exit(1)
        
    open(dot_emscripten, 'w').write(filled_config)
    print("Emscripten config file written to '%s'." % dot_emscripten)
