$(document).ready(function () {
    const searchInput = $('#search')
    searchInput.keyup(() => {
        query = searchInput.val()
        if (query.length > 2) {
            var url = `${url_origin}/search/?q=${query}`
            $.ajax({
                url: url,
                type: 'GET',
                success: function (data) {
                    createElement(data)
                }
            })
        }
    })
})


function createElement(data) {
    var resultItems = $('.result-items')
    resultItems.empty()

    resultItems.append(`
            <div class="p-2 mb-2">
                <span>search in Product:</span>
            </div>
    `)

    // add products items
    data['products'].forEach(element => {
        var item = `<div class="result-item p-2 mb-2">
        <div><a href="${url_origin}/product/detail/${element['slug']}/">${element['name']}</a></div>
        <div><img src="../.././static/images/image-1.jpg" alt=""></div>
        </div>`
        resultItems.append(item)
    });


    if (data.products.length > 3) {
        resultItems.append(`
            <div class="p-2 mb-2">
            <a href="${url_origin}/search/?q=${query}&template=true">بیشتر</a>
            </div>
        `)
    }

    resultItems.append(`
            <div class="p-2 mb-2">
                <span>search in Category:</span>
            </div>
    `)

    // add categories items
    data['categories'].forEach(element => {
        var item = `<div class="result-item p-2 mb-2">
        <div>
            <a href="${url_origin}/products/filter/?product__category=${element.id}">${element['name']}</a>
        </div>
        <div><img src="../.././static/images/image-1.jpg" alt=""></div>
        </div>`
        resultItems.append(item)
    });



    $('.close').parent().css("display", "block")
}