document.querySelector('.button_sale_record').addEventListener('click', function() {
    window.location.href = '/recordsales/none';
});

document.querySelector('.dropdown_Stock_class').addEventListener('click', function() {
    window.location.href = 'stock.html';
});

function openCreate(url){
    document.getElementById('createContainer').style.display = 'block';
    var iframe = document.getElementById('createIframe');
    iframe.src = url;  // Set the iframe's src to the clicked link's href
    console.log(url)
}

// เปิดหน้าต่าง Create สินค้าใหม่ แก้การทำงานได้เลย
newItem.addEventListener("click", function(){
    // newProduct.style.display = 'block';
    // overlay.style.display = 'block';
});

// เปิดหน้าต่าง Edit สินค้าต่างๆ
function openEdit(url){
    // let editPopup = document.getElementById("edit-popup");
    // editPopup.style.display = "block";
    // overlay.style.display = "block";
    // // url
    // editPopup.src = url;
};


