# tests/test_file_organizer.py

import unittest
import tempfile
import os
from pathlib import Path
from file_organizer.organizer import organize_directory, get_target_folder

class TestFileOrganizer(unittest.TestCase):
    def setUp(self):
        """Create a temporary directory for testing."""
        self.test_dir = Path(tempfile.mkdtemp())
        # Create sample files
        (self.test_dir / "test.pdf").write_text("PDF content")
        (self.test_dir / "image.jpg").write_text("Image content")
        (self.test_dir / "script.py").write_text("# Python code")
        (self.test_dir / ".hidden").write_text("Hidden file")
        
    def tearDown(self):
        """Clean up test directory."""
        import shutil
        shutil.rmtree(self.test_dir, ignore_errors=True)
    
    def test_get_target_folder(self):
        """Test extension-to-folder mapping."""
        self.assertEqual(get_target_folder(".pdf"), "Documents")
        self.assertEqual(get_target_folder(".jpg"), "Images")
        self.assertEqual(get_target_folder(".py"), "Code")
        self.assertEqual(get_target_folder(".xyz"), "Others")
    
    def test_organize_directory(self):
        """Test file organization logic."""
        # Verify initial state
        files_before = list(self.test_dir.iterdir())
        self.assertEqual(len([f for f in files_before if f.is_file()]), 3)  # Excludes .hidden
        
        # Run organizer
        organize_directory(self.test_dir)
        
        # Verify organization
        docs_dir = self.test_dir / "Documents"
        images_dir = self.test_dir / "Images"
        code_dir = self.test_dir / "Code"
        
        self.assertTrue(docs_dir.exists())
        self.assertTrue(images_dir.exists())
        self.assertTrue(code_dir.exists())
        
        # Verify files moved correctly
        self.assertTrue((docs_dir / "test.pdf").exists())
        self.assertTrue((images_dir / "image.jpg").exists())
        self.assertTrue((code_dir / "script.py").exists())

if __name__ == "__main__":
    unittest.main()