from pathlib import Path
import sys
LIBRARY_DIR=Path(__file__).resolve().parents[1]/'Library'
if str(LIBRARY_DIR) not in sys.path: sys.path.insert(0,str(LIBRARY_DIR))
