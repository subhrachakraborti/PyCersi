# Security Policy

## Overview

PyCersi is maintained with security-conscious defaults and dependency tracking.
No software is risk-free, so security issues are handled through coordinated disclosure.

This project is **not malware** and is intended for educational and productive use.

## Supported Versions

The following table lists the versions of the project that are currently receiving security updates.

| Version      | Supported          |
|--------------|--------------------|
| 7.0.x        | ✅                 |
| 6.x and below| :x:                |

Please make sure to keep your installation up to date to receive the latest security patches and improvements.

## Reporting a Vulnerability

If you find a vulnerability, please report it responsibly and avoid public disclosure until a fix is available.

To report a vulnerability:

- **Primary Contact**: [Email](mailto:mail@subhrachakraborti.com)
- **Public Tracker (non-sensitive issues only)**: [GitHub Issues](https://github.com/subhrachakraborti/PyCersi/issues)

### Guidelines for Reporting

1. **Provide a clear description**: Include impact, affected component, and attack path.
2. **Include reproduction steps**: Add PoC details if safe to share privately.
3. **Share environment details**: OS, Python version, package version, and install method.
4. **Avoid publishing secrets**: Remove API keys, tokens, and personal data from reports.

## Safety Certification

This project has undergone a security check and has been certified safe by [SafetyCLI](https://data.safetycli.com/packages/pypi/pycersi/).

- [SafetyCLI Certificate](https://data.safetycli.com/packages/pypi/pycersi/)

## Security Best Practices

Please ensure that you follow general security best practices when using this project:

1. **Keep dependencies up to date**: Regularly upgrade PyCersi and pinned dependencies.
2. **Use trusted sources**: Install from PyPI or the official GitHub repository only.
3. **Protect API keys**: Do not hardcode OpenRouter or other credentials in source files.
4. **Run least privilege**: Avoid running apps with elevated permissions unless necessary.
5. **Audit periodically**: Use dependency and static scans in CI where possible.

---

By using this project, you agree to adhere to its intended use and help create a safer web for everyone. Thank you for your support and contributions.
