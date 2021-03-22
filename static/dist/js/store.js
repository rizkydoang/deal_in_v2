function Update_Item(id_item){
    document.getElementById('id').value = document.getElementById(id_item+'_updt_id_item').value
    document.getElementById('item').value = document.getElementById(id_item+'_updt_name').value
    document.getElementById('qty').value = document.getElementById(id_item+'_updt_quantity').value
    document.getElementById('category').value = document.getElementById(id_item+'_updt_id_category').value
    document.getElementById('desc').value = document.getElementById(id_item+'_updt_description').value
    document.getElementById('price').value = document.getElementById(id_item+'_updt_price').value
}

function Clear_Update_Item(){
    document.getElementById('id').value = ''
    document.getElementById('item').value = ''
    document.getElementById('qty').value = ''
    document.getElementById('category').value = ''
    document.getElementById('desc').value = ''
    document.getElementById('price').value = ''
}