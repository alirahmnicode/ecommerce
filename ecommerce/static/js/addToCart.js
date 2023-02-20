const addBtn = $('.add-to-cart')
const url_location = window.location
const action = "add"


addBtn.click(function () {
    const product_id = this.dataset.product_id

    $.ajax({
        url: `${url_location}cart/quantity/${product_id}/${action}/`,
        type: 'GET',
        success: (data) => updateCartCounter(data)
    })
})


function updateCartCounter(cart) {
    $('#header-qty').text(cart.cart.quantity)
}