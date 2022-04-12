from importlib.util import find_spec
from types import ModuleType
from importlib import import_module
import toolkitorm


def test_all_list(module: ModuleType = toolkitorm) -> None:
    assert hasattr(module, "__all__")
    for name in getattr(module, "__all__"):
        try:
            test_all_list(import_module(f"{module.__name__}.{name}"))
        except ModuleNotFoundError:
            continue
