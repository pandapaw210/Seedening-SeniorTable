let secretNumber = 20;
let score = 20;
let highestRecord = 0;

document.addEventListener('DOMContentLoaded', function (event) {
  document.querySelector('.score').textContent = '점수: ' + score;
  document.querySelector('.message').textContent = '숫자를 맞춰봐요!';
  secretNumber = Math.floor(Math.random() * 20 + 1);
  document.querySelector('.number').textContent = '?';
  document.querySelector('.record').textContent = '최고 점수: ' + 0;
  console.log(secretNumber);
});

document.querySelector('.check-btn').addEventListener('click', function () {
  let inputNumber = document.querySelector('.guess-number').value;
  console.log(inputNumber === secretNumber);
  console.log(secretNumber);
  if (inputNumber == secretNumber) {
    document.querySelector('.message').textContent = '축하해요!';
    document.querySelector('.number').textContent = secretNumber;
    document.querySelector('body').style.backgroundColor = '#7ef760e6';
    if (score > highestRecord) {
      document.querySelector('.record').textContent =
        '최고 점수: ' + score;
    }
    return;
  } else if (inputNumber < secretNumber) {
    document.querySelector('.message').textContent = '그 숫자보다는 훨씬 커요!';
    score--;
  } else {
    document.querySelector('.message').textContent = '그 숫자보다는 훨씬 작아요!';
    score--;
  }
  document.querySelector('.score').textContent = '점수 : ' + score;
});

document.querySelector('.again-btn').addEventListener('click', function () {
  score = 20;
  secretNumber = Math.floor(Math.random() * 20 + 1);
  document.querySelector('.score').textContent = '점수 : ' + score;
  document.querySelector('.message').textContent = '숫자를 맞춰봐요!';
  document.querySelector('.number').textContent = '?';
  document.querySelector('body').style.backgroundColor = 'rgb(20, 20, 20, 0.9)';
});
