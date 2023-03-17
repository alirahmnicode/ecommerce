// var url_origin = window.location.origin

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

    for (const key in data) {
        // add tag element
        resultItems.append(`
            <div class="p-2 mb-2">
                <span>search in ${key}</span>
            </div>
        `)

        // add items
        data[key].forEach(element => {
            var item = `<div class="result-item p-2 mb-2">
            <div><a href=>${element['name']}</a></div>
            <div><img src="../.././static/images/image-1.jpg" alt=""></div>
            </div>`
            resultItems.append(item)
        });

        resultItems.append(`
            <div class="p-2 mb-2">
            <a href="${url_origin}/search/?q=${query}&template=true">بیشتر</a>
            </div>
        `)

    }
}