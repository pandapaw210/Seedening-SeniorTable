var b=document.querySelector('.start');
var btn2 = document.querySelector('.hide-reload')
var count = -1;
let getTime = Date.now();

window.onload=(event)=>{
  setInterval(function(){
    b.style.transform="translate("+(Math.floor(Math.random()*100)-50)+"vw,"+(Math.floor(Math.random()*100)-50)+"vh)"
  }, 1075);
}

// 공튀어나가는거 수정

b.onclick = function () {
    count++;
    document.querySelector('h3').innerHTML=count;
    setInterval(function checkTime() {
      let gameTime = Date.now() - getTime;
      if (gameTime > 3000) {
        result = document.querySelector('h3');
        result.innerHTML = "You Lose";
        b.classList.add('hide-ball')
        btn2.classList.remove('hide-reload')
        btn2.classList.add('show-reload')
      }
    }, 3000)
    getTime = Date.now();
}

btn2.addEventListener('click', () => location.reload());
