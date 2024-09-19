//Map redering route:
window.onload = function() {
    //Renders search boxes + retrieves api key
    $.get('/api/mapquest_key', function(data) {
        var mapquestKey = data.key;
        console.log(mapquestKey)
        L.mapquest.key = mapquestKey;
        
        placeSearch({
            key:mapquestKey,
            container: document.querySelector('#origin'),
      });
      
        placeSearch({
            key:mapquestKey,
            container: document.querySelector('#destination')
    });
    });   
  }

//get the button into a JS object
var sendBtn = document.getElementById("form-send");
//create an event listener and handler for the send button
sendBtn.onclick = function () {
    $.get('/api/mapquest_key', function(data) {
        var mapquestKey = data.key;
        L.mapquest.key = mapquestKey;
        //Get origin and destination
        var origin = document.getElementById("origin");
        var destination = document.getElementById("destination");
        //get all the strings in the elements and trim them
        var originStr = origin.value.trim();
        var destinationStr = destination.value.trim();

        L.mapquest.directions().route({
            start: originStr,
            end: destinationStr,
            options: {
                avoids: ['toll road']
            }     
        });

        routeURL = 'http://www.mapquestapi.com/directions/v2/route?key=' + mapquestKey + '&from=' + originStr + '&to=' + destinationStr + '&avoids=' + 'toll road'

        //Sets pickup and dropoff in session for use by flask
        $.ajax({
            type: 'POST',
            url: "/setAddresses",
            headers: {
                'Access-Control-Allow-Origin': '*'},
            data : {
                route :routeURL,
                origin : originStr,
                end: destinationStr
            },
            success: function(response) {
            $('#output').text(response.output).show();
        },
        error : function (status, statusText, responses) {
            var errormsg = "";
            errormsg += "Posting error. Status: " + statusText + " " + responses;
            console.log(errormsg);
        },


    })
});

};