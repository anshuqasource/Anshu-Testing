# Pytest Framework Setup

This is a complete pytest automation framework structure.

## Project Structure

```
AutomationFramework/
├── tests/
│   ├── conftest.py              # Shared fixtures and configuration
│   ├── test_sample.py           # Sample test file
│   └── __init__.py              # Package marker
├── pytest.ini                   # Pytest configuration
├── requirements.txt             # Python dependencies
└── venv/                        # Virtual environment
```

## Installation

1. **Activate virtual environment:**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

### Run all tests:
```bash
pytest
```

### Run with verbose output:
```bash
pytest -v
```

### Run specific test file:
```bash
pytest tests/test_sample.py
```

### Run specific test class:
```bash
pytest tests/test_sample.py::TestCalculator
```

### Run specific test method:
```bash
pytest tests/test_sample.py::TestCalculator::test_add_positive_numbers
```

### Run tests with specific marker:
```bash
pytest -m unit
pytest -m smoke
pytest -m integration
```

### Run with coverage report:
```bash
pytest --cov=tests --cov-report=html
```

### Run tests in parallel:
```bash
pytest -n auto
```

### Run with timeout (30 seconds per test):
```bash
pytest --timeout=30
```

### Generate HTML report:
```bash
pytest --html=report.html --self-contained-html
```

## Configuration

### pytest.ini
- Configures test discovery patterns
- Defines custom markers (unit, integration, smoke, regression)
- Sets output verbosity and error display

### conftest.py
- Contains shared fixtures available to all tests
- Provides session and function-level configuration
- Includes logging setup
- Sample fixtures: `session_config`, `logger`, `sample_data`

## Creating Tests

### Basic Test Structure:
```python
import pytest

def test_something():
    """Simple test function"""
    assert 1 + 1 == 2

class TestFeature:
    """Test class for grouping related tests"""
    
    def test_case_1(self):
        assert True
    
    @pytest.mark.unit
    def test_case_2(self):
        assert True
```

### Using Fixtures:
```python
def test_with_fixture(sample_data, logger):
    """Test using fixtures from conftest.py"""
    logger.info(f"Data: {sample_data}")
    assert sample_data["username"] == "testuser"
```

### Parametrized Tests:
```python
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 3),
    (3, 4),
])
def test_with_parameters(input, expected):
    assert input + 1 == expected
```

## Useful Plugins Installed

- **pytest-cov**: Code coverage reporting
- **pytest-xdist**: Parallel test execution
- **pytest-timeout**: Timeout for slow tests
- **pytest-mock**: Enhanced mocking capabilities
- **pytest-html**: HTML report generation

## Best Practices

1. Name test files with `test_` prefix
2. Name test functions/classes with `test_` prefix
3. Use descriptive test names
4. Group related tests in classes
5. Use fixtures for setup/teardown
6. Mark tests with appropriate markers
7. Keep tests independent and isolated
8. Use parametrization for testing multiple inputs

## Next Steps

1. Add your test files to the `tests/` directory
2. Create additional fixture files in `conftest.py` as needed
3. Update `requirements.txt` with any additional dependencies
4. Integrate with CI/CD pipeline
