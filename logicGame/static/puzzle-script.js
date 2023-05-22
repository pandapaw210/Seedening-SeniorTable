var img = ['https://mdl.artvee.com/sftb/517572ld.jpg',
'https://mdl.artvee.com/sftb/511886ld.jpg','https://mdl.artvee.com/sftb/517646ld.jpg',
'https://mdl.artvee.com/sftb/525631ld.jpg',
'https://mdl.artvee.com/sftb/510782ld.jpg','https://mdl.artvee.com/sftb/510311ld.jpg']
var old = 5
function randomize() {
  let root = document.documentElement
  root.style.setProperty('--image','url('+img[old]+')')
  old++
  if(old > 5) {
    old = 0
  }  
  var ul = document.querySelector('#puzz');
  for (var i = ul.children.length; i >= 0; i--) {
      ul.appendChild(ul.children[Math.random() * i | 0]);
  }
}
randomize()

function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.className);   
}

function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text")
  
  if(ev.target.className == data){
     ev.target.classList.add('dropped')
     document.querySelector('.'+data+"[draggable='true']").classList.add('done')
    
    if(document.querySelectorAll('.dropped').length == 9) {
      document.querySelector('#puz').classList.add('allDone')
      document.querySelector('#puz').style.border = 'none'  
      document.querySelector('#puz').style.animation = 'allDone 1s linear forwards'  
      
      setTimeout(function(){
        reload()
        randomize()
      },5500)
    }    
  }  
}

function reload() {
  document.body.innerHTML = "<div class='top'> <div class='title'> <div class='head_title'>명화 퍼즐 맞추기</div> <div class='sub_title'>아름다운 풍경 그림을 맞추며 감상해보세요~</div> </div> <a class='back_btn' href='/'><i class='fa-solid fa-house'></i></a> </div> <div id='puz'> <i class='first' ondrop='drop(event)' ondragover='allowDrop(event)'></i>  <i class='secon' ondrop='drop(event)' ondragover='allowDrop(event)'></i>  <i class='third' ondrop='drop(event)' ondragover='allowDrop(event)'></i>  <i class='fourt' ondrop='drop(event)' ondragover='allowDrop(event)'></i>  <i class='fifth' ondrop='drop(event)' ondragover='allowDrop(event)'></i>  <i class='sixth' ondrop='drop(event)' ondragover='allowDrop(event)'></i>  <i class='seven' ondrop='drop(event)' ondragover='allowDrop(event)'></i>  <i class='eight' ondrop='drop(event)' ondragover='allowDrop(event)'></i>  <i class='ninth' ondrop='drop(event)' ondragover='allowDrop(event)'></i></div><div id='puzz'>  <i class='third' draggable='true' ondragstart='drag(event)'></i>  <i class='first' draggable='true' ondragstart='drag(event)'></i>  <i class='secon' draggable='true' ondragstart='drag(event)'></i>  <i class='fourt' draggable='true' ondragstart='drag(event)'></i>  <i class='fifth' draggable='true' ondragstart='drag(event)'></i>  <i class='sixth' draggable='true' ondragstart='drag(event)'></i>  <i class='seven' draggable='true' ondragstart='drag(event)'></i>  <i class='eight' draggable='true' ondragstart='drag(event)'></i>  <i class='ninth' draggable='true' ondragstart='drag(event)'></i>  </div>";
}