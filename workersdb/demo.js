function renderTodo(row) {
    $('#todoItems').append(
        $('<li/>').text(row.item).append(
            $('<a/>').text(' [Delete]').click(
                function (e) {
                    idblib.indexedDB.deleteItem(row.timeStamp, renderTodo)
                }
            )
        ));
}

function addToDo() {
    var new_val = $('#todo').val();
    idblib.indexedDB.addItem(new_val);
    $('#todoItems').empty();
    idblib.indexedDB.getAllTodoItems(renderTodo);
    $('#todo').val('');
}

$(document).ready(function() {

    // Create
    //$.indexeddb("BookShop1").createObjectStore("BookList").then(console.info, console.error);

    var book = [
        {"id": 99, "text": "yessir"},
        {"id": 98, "text": "nosir"}
    ];
    $.indexeddb("BookShop1").objectStore("BookList").add(book).then(function(val) {
        book.id = val;
        console.info(val);
    }, console.error);

    $.indexeddb("BookShop1").objectStore("BookList").get(book.id).then(console.info, console.error);
});

