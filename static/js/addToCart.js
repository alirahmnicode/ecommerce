const addBtn = $('.add-to-cart')
const url_origin = window.location.origin


addBtn.click(function () {
    const product_id = this.dataset.product_id
    $.ajax({
        url: `${url_origin}/cart/add/${product_id}/1/`,
        type: 'GET',
        success: function (data) {
            updateCartCounter(data)
        }
    })

})


function updateCartCounter(data) {
    var cart = data.cart
    var quantity = 0

    for (const i in cart) {
        quantity += cart[i].quantity
    }

    $('#header-qty').text(quantity)
}