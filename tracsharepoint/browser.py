from genshi.builder import tag
from trac.core import Component, implements
from trac.web.api import ITemplateStreamFilter
from trac.web.chrome import ITemplateProvider, add_script
from trac.config import ListOption

from contextmenu.contextmenu import SubversionLink, ISourceBrowserContextMenuProvider, is_subversion_repository

from pkg_resources import resource_filename

import os
import re

class BrowserLaunchOffice(SubversionLink):
    implements(ISourceBrowserContextMenuProvider, ITemplateStreamFilter, ITemplateProvider)

    office_file_extensions = {}
    office_file_extensions.update(dict((key, 'word') for key in "doc dot docx docm dotx dotm docb".split()))
    office_file_extensions.update(dict((key, 'excel') for key in "xls xlt xlm xlsx xlsm xltx xltm xlsb xla xlam xll xlw".split()))
    office_file_extensions.update(dict((key, 'powerpoint') for key in "ppt pot pps pptx pptm potx potm ppam ppsx ppsm sldx sldm".split()))

    # ITemplateProvider methods
    def get_htdocs_dirs(self):
        return [('tracsharepoint', resource_filename(__name__, 'htdocs'))]
    
    def get_templates_dirs(self):
        return [resource_filename(__name__, 'templates')]

    # ITemplateStreamFilter methods
    def filter_stream(self, req, method, filename, stream, data):
        if filename == 'browser.html' and is_subversion_repository(data.get('repos')):
            add_script(req, 'tracsharepoint/js/opendocuments.js')
        return stream

    # IContextMenuProvider methods
    def get_order(self, req):
        return 1

    def get_draw_separator(self, req):
        return True
    
    def get_content(self, req, entry, data):
        
        # Make sure that repository is a Subversion repository, since
        # we're relying for now on Subversion to provide WebDAV
        # support.
        if not is_subversion_repository(data.get('repos')):
            return None

        reponame = data['reponame'] or ''
        ext = os.path.splitext(entry.name)[1][1:]

        if not entry.isdir and ext in self.office_file_extensions:

            path = self.get_subversion_path(entry)
            href = self.get_subversion_href(data, path)


            if re.search('(MSIE |Trident/)',
                         req.environ.get('HTTP_USER_AGENT', '')):
                # for IE, we'll use ActiveX as this may work with older Office installations
                return tag.a(tag.i(class_="fa fa-edit"),
                             ' Edit with Microsoft Office',
                             href=href,
                             class_="officelaunchlink")
            else:
                # otherwise, let's try https://msdn.microsoft.com/en-us/library/office/dn906146.aspx
                # which is Office 2010 SP2 and above
                application = self.office_file_extensions[ext]
                return tag.a(tag.i(class_="fa fa-edit"),
                             ' Edit with Microsoft %s' % application.title(),
                             href="ms-%s:ofe|u|%s" % (application, href))

