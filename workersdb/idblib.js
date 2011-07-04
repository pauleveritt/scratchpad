var idblib = {};
var indexedDB = window.indexedDB || window.webkitIndexedDB ||
    window.mozIndexedDB;

if ('webkitIndexedDB' in window) {
    window.IDBTransaction = window.webkitIDBTransaction;
    window.IDBKeyRange = window.webkitIDBKeyRange;
}

idblib.indexedDB = {};
idblib.indexedDB.db = null;

idblib.indexedDB.onerror = function(e) {
    console.log(e);
};

idblib.indexedDB.open = function(dbname) {
    idblib.dbname = dbname;

    var request = indexedDB.open(dbname);

    request.onsuccess = function(e) {
        var v = "1.98";
        idblib.indexedDB.db = e.target.result;
        var db = idblib.indexedDB.db;
        // We can only create Object stores in a setVersion transaction;
        if (v != db.version) {
            var setVrequest = db.setVersion(v);

            // onsuccess is the only place we can create Object Stores
            setVrequest.onfailure = idblib.indexedDB.onerror;
            setVrequest.onsuccess = function(e) {
                if (db.objectStoreNames.contains(idblib.dbname)) {
                    db.deleteObjectStore(idblib.dbname);
                }

                var store = db.createObjectStore(dbname,
                    {keyPath: "timeStamp"});

                idblib.indexedDB.getAllTodoItems();
            };
        }
        else {
            idblib.indexedDB.getAllTodoItems();
        }
    };

    request.onfailure = idblib.indexedDB.onerror;
}

idblib.indexedDB.addItem = function(item) {
    var db = idblib.indexedDB.db;
    var trans = db.transaction([idblib.dbname], IDBTransaction.READ_WRITE, 0);
    var store = trans.objectStore(idblib.dbname);

    var data = {
        "item": item,
        "timeStamp": new Date().getTime()
    };

    var request = store.put(data);

    request.onsuccess = function(e) {
        console.log(e);
    };

    request.onerror = function(e) {
        console.log(e);
    };
};

idblib.indexedDB.deleteItem = function(id) {
    var db = idblib.indexedDB.db;
    var trans = db.transaction([idblib.dbname], IDBTransaction.READ_WRITE, 0);
    var store = trans.objectStore(idblib.dbname);

    var request = store.delete(id);

    request.onsuccess = function(e) {
        idblib.indexedDB.getAllTodoItems();
    };

    request.onerror = function(e) {
        console.log(e);
    };
};

idblib.indexedDB.getAllTodoItems = function() {
    var todos = document.getElementById("todoItems");
    todos.innerHTML = "";

    var db = idblib.indexedDB.db;
    var trans = db.transaction([idblib.dbname], IDBTransaction.READ_WRITE, 0);
    var store = trans.objectStore(idblib.dbname);

    // Get everything in the store;
    var keyRange = IDBKeyRange.lowerBound(0);
    var cursorRequest = store.openCursor(keyRange);

    cursorRequest.onsuccess = function(e) {
        var cursor = e.target.result;
        if (!cursor)
            return;

        renderTodo(cursor.value);
        cursor.
        continue
        ();
    };

    cursorRequest.onerror = idblib.indexedDB.onerror;
};

