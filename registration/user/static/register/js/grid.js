$(function() {

    $("#grid").jsGrid({
      width: "100%",
      height: "400px",
      filtering: true,
      inserting:true,  
      editing: true,
      sorting: true,
      paging: true,
      data:"",
      fields: [
        { name: "Name", type: "text", width: 100 },
        { name: "Age", type: "number", width: 50 },
        { name: "Cool", type: "checkbox", width: 40, title: "Is Cool", sorting: false },
        { type: "control" }
      ]
    })  
  })
  
  
  
  