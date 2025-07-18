# test_artificialeaseltechnext.py
"""
Tests for ArtificialEaselTechNext module.
"""

import unittest
from artificialeaseltechnext import ArtificialEaselTechNext

class TestArtificialEaselTechNext(unittest.TestCase):
    """Test cases for ArtificialEaselTechNext class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArtificialEaselTechNext()
        self.assertIsInstance(instance, ArtificialEaselTechNext)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArtificialEaselTechNext()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
