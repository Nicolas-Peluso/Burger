window.addEventListener("DOMContentLoaded", () => {
    const Email = document.querySelector(".Campo input[type=email]")
    const Senha = document.querySelector(".Campo input[type=password]")
    const form = document.querySelector('form')
    const rules = document.querySelectorAll('.rulesPass ul li p')
    
    form.addEventListener("submit", (e) => {
        e.preventDefault()
        const PassIsOk = VerifyPass(Senha, rules);
        if (PassIsOk === true) form.submit();
    })
})

//funções de verificação
function VerifyPass(element, rules){
    let elementValue = element.value;

    if (!/[A-Z]/.test(elementValue)){
        handdleErro(element, 1, rules)
        return false
    } 

    if(!(elementValue.length > 8) && !(elementValue.length > 150)){
        handdleErro(element, 0, rules)
        return false
    } 

    if (!/[a-z]/.test(elementValue)){
        handdleErro(element, 2, rules)
        return false
    } 
    return true
}

// funções de adicção e remoção de listeners
function Listener(element, relation, rule){
    switch (relation){
        case 'add':
            element.addEventListener('click', removeClass = () => {
                element.classList.remove('erro')
                rule.classList.remove('erro')
                Listener(element, "rem", null)
            })
            break;
        case 'rem':
            element.removeEventListener('click', removeClass)
            break;
    }
}

function handdleErro(element, indexRules, rules){
    element.classList.add("erro");
    rules[indexRules].classList.add("erro");
    Listener(element, 'add', rules[indexRules]);
}