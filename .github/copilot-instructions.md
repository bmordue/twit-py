# twit-py - Twitter API Python Utilities

Twitter API utilities written in Python for managing favorites, identifying duplicates, and extracting URLs from tweets.

**ALWAYS reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

## Quick Setup and Validation

Bootstrap the development environment:
```bash
cd /home/runner/work/twit-py/twit-py
pip3 install -r requirements.txt
pip3 install pytest flake8 black
```
- Dependencies install in ~20 seconds. NEVER CANCEL.
- No build process required - this is interpreted Python.

**CRITICAL VALIDATION**: After setup, always run:
```bash
python3 -c "import dupes; print('dupes.py imports successfully')"
python3 -m flake8 dupes.py
```

## Working Effectively

### Development Dependencies
```bash
pip3 install -r requirements.txt      # Core dependencies: python-twitter, twitter-text-python, urllib3
pip3 install pytest flake8 black      # Development tools for testing and linting
```

### Code Quality and Linting
**ALWAYS run linting before committing changes:**
```bash
python3 -m flake8 dupes.py            # Check code style and syntax
python3 -m black dupes.py --check     # Check code formatting
```
- Linting takes <2 seconds. NEVER CANCEL.
- noodling.py has Python 2 syntax errors - see Known Issues section.

### Testing
```bash
python3 -m pytest test/ -v            # Run all tests (currently empty test files)
python3 -m unittest discover test -v  # Alternative test runner
```
- Test runs take <5 seconds. NEVER CANCEL.
- No actual test cases exist yet - test files are empty placeholders.

### Import and Syntax Validation
```bash
python3 -m py_compile dupes.py        # Check syntax compilation
python3 -c "import dupes"             # Test module import
```

## Validation Scenarios

**MANUAL VALIDATION REQUIREMENT**: After making changes, always test functionality:

1. **Basic Module Import Test**:
   ```bash
   python3 -c "import dupes; print('Functions:', [f for f in dir(dupes) if not f.startswith('_')])"
   ```

2. **Code Quality Validation**:
   ```bash
   python3 -m flake8 dupes.py --max-line-length=88
   python3 -m black dupes.py --check --line-length=88
   ```

3. **Dependency Verification**:
   ```bash
   python3 -c "import twitter; import ttp; print('All dependencies available')"
   ```

## Key Project Components

### Core Modules
- **dupes.py**: Twitter duplicate detection utilities
  - Functions: `twitter_authenticate()`, `identify_dupes()`, `remove_dupes()`, `get_tweets()`
  - Status: Imports successfully, functions are placeholders
  
- **noodling.py**: Twitter API interaction and favorites management
  - Functions: `twitter_login()`, `get_all_favs()`, `get_urls()`, `main()`
  - Status: **BROKEN** - uses Python 2 syntax, needs print() parentheses

### Test Structure
- **test/test_dupes.py**: Empty test file for dupes module
- **test/test_noodling.py**: Empty test file for noodling module
- Tests can be run with pytest or unittest, but no test cases exist yet

### Configuration
- **config.py**: NOT included in repo (in .gitignore)
- Required for noodling.py Twitter API authentication
- Must contain: `TWITTER_CONSUMER_KEY`, `TWITTER_CONSUMER_SECRET`, etc.

## Known Issues and Workarounds

### Python 2/3 Compatibility
- **noodling.py has Python 2 syntax**: Line 19 uses `print 'text'` instead of `print('text')`
- **Workaround**: Fix print statements when working with noodling.py
- **Do not try to run noodling.py** until print statements are fixed

### Missing Configuration
- **config.py is required but not included** (intentionally in .gitignore)
- **Workaround**: Create config.py with placeholder values for testing:
  ```python
  TWITTER_CONSUMER_KEY = "test_key"
  TWITTER_CONSUMER_SECRET = "test_secret"
  ```

### Testing Infrastructure
- **Test files exist but are empty** - no actual test cases implemented
- **Workaround**: Add test cases when implementing new functionality

## Timing Expectations

| Operation | Expected Time | Timeout Setting |
|-----------|---------------|-----------------|
| pip install dependencies | 20 seconds | 60 seconds |
| Linting (flake8) | <2 seconds | 30 seconds |
| Code formatting (black) | <2 seconds | 30 seconds |
| Test execution | <5 seconds | 30 seconds |
| Import validation | <1 second | 10 seconds |

**NEVER CANCEL operations** - all commands complete quickly in this project.

## File Structure Reference

```
twit-py/
├── .gitignore              # Excludes config.py, *.pyc, etc.
├── requirements.txt        # python-twitter, twitter-text-python, urllib3
├── dupes.py               # Duplicate detection (working)
├── noodling.py            # Twitter API interaction (Python 2 syntax)
└── test/
    ├── test_dupes.py      # Empty test file
    └── test_noodling.py   # Empty test file
```

## Common Commands Reference

### Quick Status Check
```bash
ls -la                                    # Repository overview
python3 --version && pip3 --version     # Python environment
pip3 list | grep -E "(twitter|ttp)"     # Verify Twitter dependencies
```

### Development Workflow
```bash
# 1. Validate current state
python3 -c "import dupes; print('OK')"

# 2. Make changes to dupes.py

# 3. Validate changes
python3 -m py_compile dupes.py
python3 -m flake8 dupes.py
python3 -c "import dupes; print('Updated module imports OK')"

# 4. Run tests (when they exist)
python3 -m pytest test/ -v
```

### Emergency Troubleshooting
```bash
# Reset pip cache if package issues
pip3 cache purge

# Reinstall dependencies
pip3 uninstall python-twitter twitter-text-python urllib3 -y
pip3 install -r requirements.txt

# Check Python path issues
python3 -c "import sys; print('\n'.join(sys.path))"
```