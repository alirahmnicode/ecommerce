const addBtn = $('.add-to-cart')
const url_origin = window.location.origin
const action = "add"


addBtn.click(function () {
    const product_id = this.dataset.product_id
    $.ajax({
        url: `${url_origin}/cart/quantity/${product_id}/${action}/`,
        type: 'GET',
        success: function (data) {
            updateCartCounter(data)
        }
    })

})


function updateCartCounter(cart) {
    $('#header-qty').text(cart.cart.quantity)
}