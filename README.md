# trac-plugin-sharepoint

A Trac plugin to provide Microsoft Office interoperability through implementation of SharePoint Protocols.

Trademarks such as SharePoint and Office are intended to be used as
per guidelines published at
http://www.microsoft.com/en-us/legal/intellectualproperty/Trademarks/Usage/General.aspx

Microsoft published documentation on SharePoint interoperability is
hosted at
https://msdn.microsoft.com/en-us/library/office/cc339475%28v=office.12%29.aspx

## Development environment

Run 'vagrant up', then visit https://localhost:10443/trac

To see logs:

`vagrant ssh -c "tail -f /var/local/trac/log/*"`

To set the URL to SVN, in case your vagrant host is not the machine
with Microsoft Office:

`vagrant ssh -c "sudo -u www-data trac-admin /var/local/trac config set svn repository_url https://server:10443/svn/"`

To list SVN locks:

`vagrant ssh -c "sudo -u www-data svnadmin lslocks /var/local/svn/"`

## Dependencies

Requires Trac >= 1.0.1

Requires subversion > 1.8.8 - maybe >= 1.8.11 (https://mail-archives.apache.org/mod_mbox/subversion-dev/201404.mbox/%3CCAJrmsKZtYQGUuPH7WAL5HKNXDGk7ADd4gmzURuRTT-Q+KzZ=xQ@mail.gmail.com%3E)

## Contact information

To reach CGI with regards to this plugin, please contact coreteam.service.desk.se@cgi.com
