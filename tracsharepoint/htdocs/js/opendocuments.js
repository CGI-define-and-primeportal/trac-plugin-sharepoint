$(function() {

    $("a.officelaunchlink-edit").click(function() {
	var ua = window.navigator.userAgent;
	if (~ua.indexOf('MSIE ') || ~ua.indexOf('Trident/')) {
	    // http://stackoverflow.com/questions/19999388/jquery-check-if-user-is-using-ie
	    ed = new ActiveXObject('SharePoint.OpenDocuments.4');
	    if (ed) { ed.EditDocument(this.href); }
	} else {
	    alert("This feature requires Windows, Internet Explorer, and Microsoft Office.")
	}
	return false;
    });
  
    $("a.officelaunchlink-view").click(function() {
	var ua = window.navigator.userAgent;
	if (~ua.indexOf('MSIE ') || ~ua.indexOf('Trident/')) {
	    // http://stackoverflow.com/questions/19999388/jquery-check-if-user-is-using-ie
	    ed = new ActiveXObject('SharePoint.OpenDocuments.4');
	    if (ed) { ed.ViewDocument(this.href); }
	} else {
	    alert("This feature requires Windows, Internet Explorer, and Microsoft Office.")
	}
	return false;
    });

});
