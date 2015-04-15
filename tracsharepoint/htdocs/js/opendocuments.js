$(function() {

    // http://stackoverflow.com/questions/19999388/jquery-check-if-user-is-using-ie
    function msieversion() {
        var ua = window.navigator.userAgent;
        var msie = ua.indexOf("MSIE ");
	
        if (msie > 0 || !!navigator.userAgent.match(/Trident.*rv\:11\./))      // If Internet Explorer, return version number
            return parseInt(ua.substring(msie + 5, ua.indexOf(".", msie)));
        else
            return 0;
	
	return false;
    }
    
    $("a.officelaunchlink").click(function() {
	if (msieversion() > 0) { 
	    if (window.ActiveXObject) {
		ed = new ActiveXObject('SharePoint.OpenDocuments.4');
		if (ed) {
		    ed.EditDocument(this.href);
		}
	    }
	} else {
	    alert("This feature requires Windows, Internet Explorer, and Microsoft Office.")
	}
	return false;
    });

});
