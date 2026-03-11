# Security Policy

## Supported Versions

| Version | Status |
| ------- | ------ |
| 1.0.x   | Supported |
| < 1.0   | Not supported |

## Reporting a Vulnerability

We take the security of Keynote-MCP seriously. If you discover a security vulnerability, please report it responsibly.

### How to Report

Please **do not** report security vulnerabilities in public GitHub Issues. Instead, contact us privately:

1. **GitHub Security Advisory** (recommended)
   - Use GitHub's [private security advisory](https://github.com/ByAxe/keynote-mcp/security/advisories/new)

2. **Email**
   - Create a [GitHub Issue](https://github.com/ByAxe/keynote-mcp/issues) marked `[SECURITY]`

### What to Include

- **Vulnerability type**: Nature of the vulnerability
- **Affected scope**: Which versions and features are affected
- **Reproduction steps**: Detailed steps to reproduce
- **Proof of concept**: PoC code if available
- **Impact assessment**: Potential security impact
- **Suggested fix**: Fix recommendations if any

### Response Timeline

- **24 hours**: Acknowledge receipt
- **72 hours**: Initial assessment and response
- **7 days**: Detailed analysis and fix plan
- **30 days**: Release fix (if applicable)

## Known Security Considerations

### AppleScript Execution
- **Risk**: Execution of malicious AppleScript code
- **Mitigation**: Strict input validation, predefined script templates, limited operation types

### File System Access
- **Risk**: Unauthorized file access
- **Mitigation**: Path validation, safe file operations, restricted access scope

### Network Requests
- **Risk**: Malicious network requests
- **Mitigation**: URL and domain validation, HTTPS only, rate limiting

### API Key Exposure
- **Risk**: Third-party API key leakage
- **Mitigation**: Environment variable storage, no logging of sensitive data, regular key rotation

## Security Best Practices

### For Users
1. Never hardcode API keys in source code
2. Use `.env` files for sensitive configuration (ensure it's in `.gitignore`)
3. Grant only necessary macOS permissions
4. Use HTTPS for all external API calls

### For Developers
1. Keep dependencies up to date
2. Use security scanning tools
3. Review all code changes
4. Include security test cases
