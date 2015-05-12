$(function() {

    $("a.officelaunchlink").click(function() {
	var ua = window.navigator.userAgent;
	window.console.log("Checking UA %s", ua);
	if (~ua.indexOf('MSIE ') || ~ua.indexOf('Trident/')) {
	    // http://stackoverflow.com/questions/19999388/jquery-check-if-user-is-using-ie
	    window.console.log("Detected IE");
	    window.console.log("ActiveXObject is %s", window.ActiveXObject);	    
	    ed = new ActiveXObject('SharePoint.OpenDocuments.4');
	    window.console.log("ActiveXObject: %s", ed);		
	    if (ed) {
		ed.EditDocument(this.href);
	    }
	} else {
	    alert("This feature requires Windows, Internet Explorer, and Microsoft Office.")
	}
	return false;
    });

});
