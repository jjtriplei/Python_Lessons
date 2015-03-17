/**
 * Created by thing2 on 3/16/15.
 */

$(document).ready(function() {
    function post(location) {
        $.ajax({
           type: "POST",
           url: location
        });
    }

    $("#find").click(function() {
            post("/find");
        }
    )

    $("#process").click(function() {
            post("/process");
        }
    )
});
