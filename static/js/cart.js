cartData = {};
$.getJSON( "/ajax/product_search/", function( data ) {
    cartData = data;
    var items = [];
    var totalValue = 0;
    $.each(data, function(index, value) {
        items.push('<tr><td><img class="img-thumbnail" style="width:30%" alt="Image" id="imageUrl" src="'+value["imageUrl"]+'"></td><td class="text-capitalize">'+value["name"].toLowerCase()+'</td><td>R$ '+value["price"].toFixed(2)+'</td><td><a href="/product/'+value["id"]+'">Ir Para Página</a><br><a href="/product/'+value["id"]+'">Remover</a></td></tr>');
        totalValue += value["price"];
    });
    if (items.length != 0) { $(items.join("")).appendTo("tbody"); }
    $('<tr><td></td><td class="text-capitalize"><b>Preço Total: </b></td><td><b>R$ '+totalValue.toFixed(2)+'</b></td></tr>').appendTo("tbody");
})            
    .fail(function( jqxhr, textStatus, error ) {
        var err = textStatus + ", " + error;
        console.log( "Request Failed: " + err );
    });;
