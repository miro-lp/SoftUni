function attachEventsListeners() {
    const convertor = {
        '0': 1000, '1': 1, '2': 0.01, '3': 0.001, '4': 1609.34,
        '5': 0.9144, '6': 0.3048, '7': 0.0254
    }
    document.getElementById('convert').addEventListener('click', () => {
        let inputIndex = document.getElementById('inputUnits').selectedIndex
        let convertIndex = document.getElementById('outputUnits').selectedIndex
        let inputValue = document.getElementById('inputDistance').value
        let coverValue = inputValue*convertor[inputIndex]/convertor[convertIndex]
        document.getElementById('outputDistance').value = coverValue 
        document.getElementById('outputDistance').disabled = ''
        console.log(coverValue)

    })
}
