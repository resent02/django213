function reg(){
    document.getElementById('window').style.transform = "translateX(930px)"
    document.getElementById('window').style.opacity = 50
    document.getElementById('window').style.transition = ".6s"
}


function out_reg(){
    document.getElementById('window').style.transform = "translateX(-930px)"
    document.getElementById('window').style.opacity = 0.2
    document.getElementById('window').style.transition = ".6s"
}

var choose = 'mentor'

function to_student(){
    document.getElementById('on-off').style.transform = "translateX(80px)"
    document.getElementById('student').style.color = "#fff"
    document.getElementById('mentor').style.color = "#B22222"
    document.getElementById('on-off').style.transition = ".6s"
    choose = 'student'

}
function to_mentor(){
    document.getElementById('on-off').style.transform = "translateX(0px)"
    document.getElementById('mentor').style.color = "#fff"
    document.getElementById('student').style.color = "#B22222"
    document.getElementById('on-off').style.transition = ".6s"
    choose = 'mentor'

}
function reg(){
    document.getElementById('window').style.transform = "translateX(930px)"
    document.getElementById('window').style.opacity = 50
    document.getElementById('window').style.transition = ".6s"
}


function out_reg(){
    document.getElementById('window').style.transform = "translateX(-930px)"
    document.getElementById('window').style.opacity = 0.2
    document.getElementById('window').style.transition = ".6s"
}

var choose = 'mentor'

function to_student(){
    document.getElementById('on-off').style.transform = "translateX(80px)"
    document.getElementById('student').style.color = "#fff"
    document.getElementById('mentor').style.color = "#B22222"
    document.getElementById('on-off').style.transition = ".6s"
    choose = 'student'

}
function to_mentor(){
    document.getElementById('on-off').style.transform = "translateX(0px)"
    document.getElementById('mentor').style.color = "#fff"
    document.getElementById('student').style.color = "#B22222"
    document.getElementById('on-off').style.transition = ".6s"
    choose = 'mentor'

}
function auth(){
    if (choose == 'mentor'){
        window.location = "/reg-mentor"
    }else{
        window.location = '/reg-student'
    }
}