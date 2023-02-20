var LeftSide = document.getElementById('left');
var RightSide = document.getElementById('right');
var CubeStart = 5;
var level = 1;
//generate the position
function GeneratePosition(max, min) {
    return Math.random() * (max - min) + min;
}

function GenerateCube(CubeNum) {
    clearFaces();
    var max = LeftSide.offsetWidth-55;
    for (var i = 0; i < CubeNum; i++) {
        var el = document.createElement('div');
        el.setAttribute("class", "cube");
        el.style.left = GeneratePosition(max, 0) + "px";
        el.style.top = GeneratePosition(max, 0) + "px";
        LeftSide.appendChild(el);
    }
    CopyToRightSide();
}

function clearFaces() {
    while (LeftSide.firstChild) {
        LeftSide.removeChild(LeftSide.firstChild);
    }
    while (RightSide.firstChild) {
        RightSide.removeChild(RightSide.firstChild);
    }
}
function CopyToRightSide() {
    var LeftSideCubes = LeftSide.cloneNode(true);
    LeftSideCubes.removeChild(LeftSideCubes.lastChild);
    LeftSideCubes.removeAttribute("id");
    RightSide.appendChild(LeftSideCubes);
    MakeActions();
    LeftSideCubes = "";
}

function MakeActions() {
    var LastSquare = document.getElementById('left').lastChild;
    var status = document.getElementById('status');
    LastSquare.onclick = function nextLevel(event) {
        event.stopPropagation();
        CubeStart = CubeStart + 5;
        level += 1;
        status.innerHTML = "Level " + level;
        GenerateCubes();
    }
}
document.body.onclick = function bodyClick() {
alert("게임 끝! 현재 레벨은: " + level);
CubeStart = 5;
level = 1;
clearFaces();

    if (confirm("다시 게임을 시작 하시겠습니까?")) {
        GenerateCube(CubeStart);
    }
}

function GenerateCubes(){
    GenerateCube(CubeStart);
}

window.onload = function () {
    GenerateCubes();
}




