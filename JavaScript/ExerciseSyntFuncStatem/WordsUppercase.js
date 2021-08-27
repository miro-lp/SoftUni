function wordsUppercase(text){
    let re = /\w+/g
    let textArray = text.match(re)
    let textArray1 = []
    for(w of textArray){
        textArray1.push(w.toUpperCase())
    }

    console.log(textArray1.join(', '))
}

wordsUppercase('Hi, how are you?')