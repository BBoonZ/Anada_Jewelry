// เพิ่มสินค้าใหม่ popup


let newItem = document.getElementById("new_item");
let newProduct = document.getElementById("newProductPopup");
let overlay = document.getElementById("overlay");
let cancelButton = document.getElementById("newCancelButton");



cancelButton.addEventListener("click", function(){
    console.log("hello")
    newProduct.style.display = 'none';
    overlay.style.display = 'none';
})


// เรื่องรูปภาพ
document.getElementById('add-picture-button').addEventListener('click', function() {
    document.getElementById('fileInput').click();
});


document.getElementById('fileInput').addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
        console.log('File selected: ' + file.name);
    } else {
        console.log('No file selected');
    }
});