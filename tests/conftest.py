from pathlib import Path
import sys

# Добавляем папку Library в путь поиска модулей.
# Это нужно именно для текущей структуры Varian2,
# где library.py использует импорты Books и Clients.
LIBRARY_DIR = Path(__file__).resolve().parents[1] / "Library"
if str(LIBRARY_DIR) not in sys.path:
    sys.path.insert(0, str(LIBRARY_DIR))
