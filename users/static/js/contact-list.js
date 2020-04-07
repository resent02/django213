function bogdan(){
        sergey_()
        vladislav_()
        aikerim_()
    document.getElementById('bogdan-desc').style.opacity = 1
    document.getElementById('bogdan-desc').style.transition = ".5s"
    document.getElementById('bogdan-desc').style.transform = "translateY(-280px)"
    document.getElementById('bogdan').style.backgroundSize = "100% 2px"
}
function bogdan_(){
            document.getElementById('bogdan-desc').style.opacity = 0
            document.getElementById('bogdan-desc').style.transition = ".5s"
            document.getElementById('bogdan-desc').style.transform = "translateY(0px)"
            document.getElementById('bogdan').style.backgroundSize = "0% 2px"
}
function sergey(){
            bogdan_()
            vladislav_()
            aikerim_()
    document.getElementById('sergey-desc').style.opacity = 1
    document.getElementById('sergey-desc').style.transition = ".5s"
    document.getElementById('sergey-desc').style.transform = "translateY(-280px)"
    document.getElementById('sergey').style.backgroundSize = "100% 2px"
}
function sergey_(){
        document.getElementById('sergey-desc').style.opacity = 0
        document.getElementById('sergey-desc').style.transition = ".5s"
        document.getElementById('sergey-desc').style.transform = "translateY(0px)"
        document.getElementById('sergey').style.backgroundSize = "0% 2px"
}
function vladislav(){
            bogdan_()
            sergey_()
            aikerim_()
    document.getElementById('vladislav-desc').style.opacity = 1
    document.getElementById('vladislav-desc').style.transition = ".5s"
    document.getElementById('vladislav-desc').style.transform = "translateY(-280px)"
    document.getElementById('vladislav').style.backgroundSize = "100% 2px"

}
function vladislav_(){
        document.getElementById('vladislav-desc').style.opacity = 0
        document.getElementById('vladislav-desc').style.transition = ".5s"
        document.getElementById('vladislav-desc').style.transform = "translateY(0px)"
        document.getElementById('vladislav').style.backgroundSize = "0% 2px"
}
function aikerim(){
            bogdan_()
            sergey_()
            vladislav_()
    document.getElementById('aikerim-desc').style.opacity = 1
    document.getElementById('aikerim-desc').style.transition = ".5s"
    document.getElementById('aikerim-desc').style.transform = "translateY(-280px)"
    document.getElementById('aikerim').style.backgroundSize = "100% 2px"
}
function aikerim_(){
        document.getElementById('aikerim-desc').style.opacity = 0
        document.getElementById('aikerim-desc').style.transition = ".5s"
        document.getElementById('aikerim-desc').style.transform = "translateY(0px)"
        document.getElementById('aikerim').style.backgroundSize = "0% 2px"
}
window.onload = bogdan()