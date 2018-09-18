
$.getJSON("demo_ajax_json.js", function(result){
    $.each(result, function(i, field){
        $("div").append(field + " ");
    });
});

console.log("ready!");
