// document.getElementById("dropdown_financial_id").addEventListener("click", function() {
//     const drop = document.getElementById("drop");
//     const dropdown_financial_id = document.getElementById("dropdown_financial_id");

//     if (drop.style.display === "block") {
//         drop.style.display = "none";
//         dropdown_financial_id.classList.remove("active");
//     } else {
//         drop.style.display = "block";
//         dropdown_financial_id.classList.add("active");
//     }
// });

function openPopup(url) {
    document.getElementById('popupContainer').style.display = 'block';
    var iframe = document.getElementById('contentIframe');
    iframe.src = url;  // Set the iframe's src to the clicked link's href
    console.log(url)
}

function closePopup() {
    document.getElementById('popupContainer').style.display = 'none';
}

function openPopup2(url) {
    document.getElementById('popup_cart').style.display = 'block';
    var iframe = document.getElementById('contentIframe2');
    iframe.src = url;  // Set the iframe's src to the clicked link's href
    console.log(url)
}

function closePopup2() {
    document.getElementById('popup_cart').style.display = 'none';
}

// document.querySelector('.button_sale_record').addEventListener('click', function() {
//     window.location.href = '/home';
// });

// document.querySelector('.dropdown_Stock_class').addEventListener('click', function() {
//     window.location.href = 'stock.html';
// });
