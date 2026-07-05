"""
Sample unit tests to demonstrate pytest structure
"""

import pytest


class TestCalculator:
    """Example test class for calculator functions"""
    
    def add(self, a, b):
        """Simple add function for testing"""
        return a + b
    
    def subtract(self, a, b):
        """Simple subtract function for testing"""
        return a - b
    
    @pytest.mark.unit
    def test_add_positive_numbers(self):
        """Test addition of positive numbers"""
        result = self.add(5, 3)
        assert result == 8
    
    @pytest.mark.unit
    def test_add_negative_numbers(self):
        """Test addition with negative numbers"""
        result = self.add(-5, -3)
        assert result == -8
    
    @pytest.mark.unit
    def test_subtract_numbers(self):
        """Test subtraction"""
        result = self.subtract(10, 3)
        assert result == 7
    
    @pytest.mark.unit
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (100, 50, 150),
    ])
    def test_add_multiple_cases(self, a, b, expected):
        """Test addition with multiple test cases"""
        result = self.add(a, b)
        assert result == expected


class TestStringOperations:
    """Example test class for string operations"""
    
    @pytest.mark.unit
    def test_string_uppercase(self):
        """Test string uppercase conversion"""
        text = "hello"
        assert text.upper() == "HELLO"
    
    @pytest.mark.unit
    def test_string_lowercase(self):
        """Test string lowercase conversion"""
        text = "HELLO"
        assert text.lower() == "hello"
    
    @pytest.mark.unit
    def test_string_contains(self):
        """Test string contains"""
        text = "pytest framework"
        assert "pytest" in text


@pytest.mark.smoke
def test_basic_assertion():
    """Basic smoke test"""
    assert True
    assert 1 == 1


def test_with_fixture(sample_data, logger):
    """Example test using fixtures"""
    logger.info(f"Using sample data: {sample_data}")
    assert sample_data["username"] == "testuser"
    assert "@" in sample_data["email"]
