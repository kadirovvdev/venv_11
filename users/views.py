from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def get_info(request):
    return HttpResponse("""
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Calculator</title>
</head>
<body>
   <style>
      *{
    margin: 50;
    padding: 0;
    box-sizing: border-box;
    outline: 0;
    transition: all 0.5s ease;
}
/* a{
    text-decoration: none;
    color: #fff;
} */
body{
background-color: tomato;
}
.container{
    height: 450px;
    width: 100vw;
    display: grid;
    place-items: center;
}
.calculator{
    position: relative;
    height: auto;
    width: auto;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 30px #000;
    text-align: center;
    background: var(--grad-2, linear-gradient(130deg, #ff5500 0%, #0d00ff 100%));
}
.theme-toggler{
    position: absolute;
    top: 30px;
    right: 30px;
    color: #fff;
    cursor: pointer;
    z-index: 1;
}
.theme-toggler.active{
    color: #333;
}
.theme-toggler.active ::before{
background-color: #fff;
}
.theme-toggler ::before{
    content: '';
    height: 30px;
    width: 30px;
    position: absolute;
    top: 50%;
    transform: translate(-50%,-50%);
    border-radius: 50%;
    background-color: #333;
    z-index: -1;
}
#display{
    margin: 0 10px;
    height: 50px;
    width: 600px;
    max-width: 400px;
    display: flex;
    align-items: flex-end;
    justify-content: flex-end;
    font-size: 30px;
    margin-bottom: 20px;
    display: block;
    overflow-x: scroll;
border-radius: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
}
/* button{
    height: 60px;
    width: 60px;
    border: 0;
    border-radius: 30px;
    margin: 5px;
    font-size: 20px;
    cursor: pointer;
    transition: all 200ms ease;
} */
button#equal{
    height: 85px;
}
button {
    margin-top: 10px;
    margin-left: 5px;
    width: 80px;
    height: 80px;
    justify-content: center;
    align-items: center;
    font-size: 30px;
    border-radius: 10px;
    background-color: #ffffff;
    border: solid 3px rgb(255, 136, 0);
}
button:hover {
    height: 83px;
    transform: scale(1.15);
    justify-content: center;
    align-items: center;
    border-radius: 10px;
    background-color: rgb(255, 136, 0);
}
.calculator{
    background-color: #fff;
}
.calculator#display{
    color: #63f121;
}
#display {
    background: var(--grad-2, linear-gradient(130deg, #00ffea 0%, #00ff59 100%));
}
   </style>
  <div class="container">
    <div class="calculator dark">
        <div class="theme-toggler-active">
         <i class="toggler-icon"></i>   
        </div>
        <div class="display-screen">
            <div id="display"></div>
        </div>
        <div class="buttons">
             <tr>
                <td><button  class="btn-operator" id="clear">C</button></td>
                <td><button  class="btn-operator" id="/">&divide</button></td>
                <td><button  class="btn-operator" id="*">x</button></td>
                <td><button  class="btn-operator" id="backspace"><<</button></td>
             </tr>
             <br>
             <tr>
                <td><button class="btn-number" id="7">7</button></td>
                <td><button class="btn-number" id="8">8</button></td>
                <td><button class="btn-number" id="9">9</button></td>
                <td><button class="btn-operator" id="-">-</button></td>
             </tr>
             <br>
             <tr>
                <td><button class="btn-number" id="4">4</button></td>
                <td><button class="btn-number" id="5">5</button></td>
                <td><button class="btn-number" id="6">6</button></td>
                <td><button class="btn-operator" id="+">+</button></td>
             </tr>
             <br>
             <tr>
                <td><button class="btn-number" id="1">1</button></td>
                <td><button class="btn-number" id="2">2</button></td>
                <td><button class="btn-number" id="3">3</button></td>
                <td rowspan="2"><button class="btn-equal" id="equal">=</button></td>
             </tr>
             <br>
             <tr>
                <td><button class="btn-operator" id="(">(</button></td>
                <td><button class="btn-number" id="0">0</button></td>
                <td><button class="btn-operator" id=")">)</button></td>
             </tr>
        </div>
    </div>
  </div>
    <script >
      const display = document.querySelector('#display');
const buttons = document.querySelectorAll('button');
const themeToggleBtn = document.querySelector('.theme-toggler-active');
const calculator = document.querySelector('.calculator');
const toggleIcon =  document.querySelector('.toggler-icon');
buttons.forEach((item) =>{
    console.log(item.id)
    item.onclick = () => {
        if (item.id == "clear") {
            display.innerText = '';
        } else if (item.id == "backspace") {
            let string = display.innerText.toString();
            display.innerText = string.substr(0,string.length - 1);
        } else if (display.innerText != '' && item.id == 'equal') {
            display.innerText = eval(display.innerText);
        } else if (display.innerText == '' && item.id =='equal') {
            display.innerText = 'Empty!';
            setTimeout(() =>(display.innerText = ''), 2000)
        }else {
            display.innerText += item.id;
        }
    }
})
let isDark = true;
themeToggleBtn.onclick = () => {
    calculator.classList.toggle('dark');
    themeToggleBtn.classList.toggle('active');
    isDark =!isDark;
}
    </script>
</body>
</html>


    """)
