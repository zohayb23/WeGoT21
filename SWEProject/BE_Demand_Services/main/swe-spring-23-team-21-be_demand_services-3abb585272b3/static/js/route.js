//Map redering route:
window.onload = function() {
    //Get api key
    $.get('/api/mapquest_key', function(data) {
        var mapquestKey = data.key;
        L.mapquest.key = mapquestKey;

        //renders map
        var map = L.mapquest.map('map', {
        center: [30.2672, -97.7431],
        layers: L.mapquest.tileLayer('map'),
        zoom: 13
        });
    });
        //Call to Flask to get the template mapRoute
        $.ajax({
            type: "GET",
            url: '/mapRoute',
            error : function (status, statusText, responses) {
                var errormsg = "";
                errormsg += "Error. Status: " + statusText + " " + responses;
                console.log(errormsg);
            },
            
            //If successful, then display route
            success: function (data, statusText, responses) {
                var callbackresponse = responses.status;
                if (callbackresponse === 200) {
                    destinationStr = responses.responseJSON.dest;
                    originStr = responses.responseJSON.origin;
                 }  
                else  {
                    console.log("API server Error");
                }
    
                
                //set Route options + pickUp dropOff locations
                L.mapquest.directions().route({
                start: originStr,
                end: destinationStr,
                options: {
                    avoids: ['toll road']
                }     
                });
            }
        });
}


  
