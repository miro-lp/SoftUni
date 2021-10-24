function generateReport() {
    let columninfo = Array.from(document.querySelectorAll('thead tr th'))

    let info = []
    for (i = 0; i < columninfo.length; i++) {

        let inputCheck = columninfo[i].querySelector('input')
        if (inputCheck.checked == true) {
            let infoByChecked = Array.from(document.querySelectorAll(`tbody tr td:nth-child(${i + 1})`))
            for (j = 0; j < infoByChecked.length; j++) {
                if (info.length < infoByChecked.length) {
                    info.push({})
                }
                let a = {}

                a[inputCheck.name] = infoByChecked[j].textContent
                info[j] = Object.assign(info[j], a)
            }

        }
    }


    document.getElementById('output').value = JSON.stringify(info)
}