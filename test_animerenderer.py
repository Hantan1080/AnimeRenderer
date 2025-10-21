# test_animerenderer.py
"""
Tests for AnimeRenderer module.
"""

import unittest
from animerenderer import AnimeRenderer

class TestAnimeRenderer(unittest.TestCase):
    """Test cases for AnimeRenderer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AnimeRenderer()
        self.assertIsInstance(instance, AnimeRenderer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AnimeRenderer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
