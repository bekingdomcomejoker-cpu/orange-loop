# Contributing to Orange Loop
Thank you for your interest in contributing to Orange Loop!
## How to Contribute
### Reporting Issues
- Check existing issues first
- Provide clear reproduction steps
- Include your Termux/Android version
- Attach relevant config files (remove sensitive data)
### Suggesting Features
- Open an issue with `[Feature]` prefix
- Explain the use case
- Consider architectural impact
### Code Contributions
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Test on Termux
5. Commit with clear message
6. Push and create PR
### Areas We Need Help
- **Model optimization** - Finding better model combinations
- **Documentation** - Improving clarity, adding examples
- **Testing** - Cross-device compatibility
- **Performance** - Memory and battery optimizations
- **Extensions** - New hands, tools, or features
## Code Style
- Follow PEP 8 for Python
- Add docstrings to functions
- Keep functions focused and small
- Comment complex logic
## Architecture Principles
When contributing, respect these core principles:
1. **Single Spine** - Don't fragment the main loop
2. **Zero-One Alternation** - Maintain meaning/wire alternation
3. **Human Sovereignty** - Always return to Node 0
4. **Optional Limbs** - Extensions branch, never replace
5. **Mobile-First** - Optimize for Termux/Android
## Testing
Test your changes on actual Termux before submitting:
```bash
cd ~/orange-loop
python orange-loop.py
```
## Commit Message Format
```
type: brief description
Longer description if needed
Fixes #issue-number
```
Types: `feat`, `fix`, `docs`, `test`, `refactor`
## Questions?
Open a discussion or issue. We're here to help!
---
_🍊 Chicka chicka orange._
