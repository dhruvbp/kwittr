$(document).ready(function(){

    $(".message_add_likes").click(function(event) {
        console.log("i funksjonen message_add_likes");
        event.preventDefault();
        var message_id = $(this).data("message_id");
        console.log(message_id);
        $.ajax({
            url: '/messages/message_add_likes/' + message_id
        })
        .done(function(data){
            console.log("done");
            var likes_updated = data['likes_updated'];
            console.log(data);
            //var message_add_likes = "#id-points-for-message-" + message_id;
            $(message_add_likes).html('likes_updated');
           
        });
    });
