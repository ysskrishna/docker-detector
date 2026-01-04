from functools import lru_cache
from pathlib import Path
import sys

@lru_cache(maxsize=1)
def is_docker() -> bool:
    """
    Return True if the current process is running inside Docker.
    
    Linux-only detection. Returns False on macOS and Windows.
    """
    if not sys.platform.startswith("linux"):
        return False

    # Check for Docker environment file
    if Path("/.dockerenv").exists():
        return True

    # Check cgroup for docker
    try:
        if "docker" in Path("/proc/self/cgroup").read_text():
            return True
    except OSError:
        pass

    # Check mountinfo for Docker container paths
    try:
        if "/docker/containers/" in Path("/proc/self/mountinfo").read_text():
            return True
    except OSError:
        pass

    return False
