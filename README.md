# Docker Detector

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/ysskrishna/docker-detector/blob/main/LICENSE)
[![Tests](https://github.com/ysskrishna/docker-detector/actions/workflows/test.yml/badge.svg)](https://github.com/ysskrishna/docker-detector/actions/workflows/test.yml)
[![PyPI](https://img.shields.io/pypi/v/docker-detector)](https://pypi.org/project/docker-detector/)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/docker-detector?period=total&units=INTERNATIONAL_SYSTEM&left_color=GREY&right_color=BLUE&left_text=downloads)](https://pepy.tech/projects/docker-detector)
[![Author site](https://img.shields.io/badge/author-ysskrishna.space-informational)](https://ysskrishna.space)
[![Context7](https://img.shields.io/badge/Context7-docs-18181B)](https://context7.com/ysskrishna/docker-detector)
[![Ask DeepWiki](https://img.shields.io/badge/DeepWiki-ask-18181B)](https://deepwiki.com/ysskrishna/docker-detector)

Detect if your Python process is running inside a Docker container. Inspired by the popular [is-docker](https://github.com/sindresorhus/is-docker) npm package. Supports cached results with optional refresh.

## Features

- Fast and reliable Docker container detection
- Multiple detection methods for robustness
- Cached results for performance optimization
- Zero dependencies, minimal overhead
- Type hints for better IDE support

## Installation

```bash
pip install docker-detector
```

Or using `uv`:

```bash
uv add docker-detector
```

## Usage

### Check if running inside Docker

```python
from docker_detector import is_docker

if is_docker():
    print("Running inside a Docker container")
else:
    print("Not running inside a Docker container")
```

### Force refresh cache

```python
from docker_detector import is_docker

# Use cached result (default)
is_docker()  # Fast, uses cache

# Force a fresh check, bypassing cache
is_docker(force_refresh=True)  # Performs new detection
```

## API Reference

Install with `pip install docker-detector` and import from `docker_detector`. Signatures and descriptions below match the source code of `docker_detector`.

### `is_docker(force_refresh: bool = False) -> bool`

Return True if the current process is running inside Docker.

Linux-only detection. Returns False on macOS and Windows.

**Parameters**

- `force_refresh`: If True, bypass the cache and perform a fresh check. Defaults to False.

**Returns**

- True if running inside Docker, False otherwise.

**Example**

```python
from docker_detector import is_docker

is_docker()  # False  (Uses cache)
is_docker(force_refresh=True)  # False  (Bypasses cache)
```

## Credits

This package is inspired by the [is-docker](https://github.com/sindresorhus/is-docker) npm package by [Sindre Sorhus](https://github.com/sindresorhus).

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details on our code of conduct, development setup, and the process for submitting pull requests.

## Built and maintained by

Docker Detector is built and maintained by:

| | Name | GitHub | Role |
|---|------|--------|------|
| <img src="https://github.com/ysskrishna.png?size=120" width="60" height="60" alt="Y. Siva Sai Krishna"> | **Y. Siva Sai Krishna** | [@ysskrishna](https://github.com/ysskrishna) | Creator |

## Changelog

See [CHANGELOG](CHANGELOG.md) for release history.

## Support

If you find this library helpful:

- ⭐ Star the repository
- 🐛 [Report issues](https://github.com/ysskrishna/docker-detector/issues)
- 🔀 Submit pull requests
- 💝 [Sponsor on GitHub](https://github.com/sponsors/ysskrishna)

## License

MIT © [Y. Siva Sai Krishna](https://github.com/ysskrishna) — see [LICENSE](LICENSE) for details.

---

<p align="left">
  <a href="https://github.com/ysskrishna">Author's GitHub</a> •
  <a href="https://linkedin.com/in/ysskrishna">Author's LinkedIn</a> •
  <a href="https://ysskrishna.space">Author's site</a> •
  <a href="https://pypi.org/project/docker-detector/">Package on PyPI</a> •
  <a href="https://github.com/ysskrishna/docker-detector/issues">Report Issues</a>
</p>
