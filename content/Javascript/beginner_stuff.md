# Beginner Javascript #

* Javascript loads before the page does, if you run into a lot of undefined use an onload or put the script down lower

## Function ##
* Use functions for help controlling code flow

        for (var i=0; i < myarr.length; i++) {
            doThisStuff(myarr[i])
        }

        function doThisStuff(arrThing) {
            console.log(arrThing.innerHtml)
        }

## Getting Elements Out of A Table ##

* The below can add an ID to a table row based on a matching element in the table
* Then use and #id in the css to add specific styling

~

    // Get All Tables 
    var tables = document.getElementsByTagName("table");    

    // Iterate through all tables and check statuses
    for (var i = 0; i < tables.length; i++) {
        checkStatus(tables[i])
    }

    // Check Statuses
    function checkStatus(table) {
        // get all the table rows
        var tbody = table.getElementsByTagName("tbody")[0];
        var rows = tbody.getElementsByTagName("tr");

        // Iterate through all rows, check last column for value
        for (i=0; i < rows.length; i++) {
            var elements = rows[i].getElementsByTagName("td");
            var value = elements[elements.length - 1];
            // Skip undefined, the first row (headers) contain no TD so undefined throws
            if (value == undefined) {
                continue;
            }

            if (value.innerHTML == 'something') {
                rows[i].id = 'somethingId'
            }
            
        }
    }