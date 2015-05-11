import win32com.client
import uuid

# http://conda.pydata.org/miniconda.html
# conda install pywin32

# TODO take from environment?
SITE="https://vagrant.vagrantup.com/svn/"


import unittest

class TestOfficeEditing(unittest.TestCase):

	def setUp(self):
		self.word_app = win32com.client.DispatchEx("Word.Application")
		self.word_app.Visible = True

		self.path = "%s/%s.docx" % (SITE, uuid.uuid4())

	def tearDown(self):
		self.word_app.Quit()
	
	def test_create(self):
		word_doc = self.word_app.Documents.Add()
		word_doc.Content = "Test 1"
		# TODO Can we provide the credentials for the webdav server?
		word_doc.SaveAs(self.path)
		word_doc.Close()

	def test_edit(self):
		word_doc = self.word_app.Documents.Add()
		word_doc.Content = "Test 1"
		word_doc.SaveAs(self.path)
		word_doc.Close()

		word_doc = self.word_app.Documents.Open(path)
		# TODO I'd like to check svn lock info here
		word_doc.Content = "Test 2"
		word_doc.SaveAs(self.path)
		word_doc.Close()

    
if __name__ == '__main__':
    unittest.main()

