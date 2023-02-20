const SLOTS_PER_REEL = 14;
//radius = Math.round( ( panelWidth / 2) / Math.tan( Math.PI / SLOTS_PER_REEL ) ); 
// current settings give a value of 149, rounded to 150
const REEL_RADIUS = Math.round(149 * Math.tan( Math.PI / 12) /Math.tan( Math.PI / 14))
function createSlots (ring) {
	
	var slotAngle = 360 / SLOTS_PER_REEL;

	var seed = getSeed();

	for (var i = 0; i < SLOTS_PER_REEL; i ++) {
		var slot = document.createElement('div');
		
		slot.className = 'slot';

		// compute and assign the transform for this slot
		var transform = 'rotateX(' + (slotAngle * i) + 'deg) translateZ(' + REEL_RADIUS + 'px)';

		slot.style.transform = transform;

		// setup the number to show inside the slots
		// the position is randomized to
    
    var slotContent = ''
    switch((seed + i)%14) {
      case 0:
        slotContent = 'ㄱ';
        break;
      case 1:
        slotContent = 'ㄴ';
        break;
      case 2:
        slotContent = 'ㄷ';
        break;
      case 3:
        slotContent = 'ㄹ';
        break;  
      case 4:
        slotContent = 'ㅁ';
        break;
      case 5:
        slotContent = 'ㅂ';
        break;
      case 6:
        slotContent = 'ㅅ';
        break;
      case 7:
        slotContent = 'ㅇ';
        break; 
      case 8:
        slotContent = 'ㅈ';
        break; 
      case 9:
        slotContent = 'ㅊ';
        break; 
      case 10:
        slotContent = 'ㅋ';
        break; 
      case 11:
        slotContent = 'ㅌ';
        break; 
      case 12:
        slotContent = 'ㅍ';
        break;
      case 13:
        slotContent = 'ㅎ';
        break; 
    }
		var content = $(slot).append('<p>' + slotContent + '</p>');

	// add the poster to the row
		ring.append(slot);
	}
}

function getSeed() {
	// generate random number smaller than 13 then floor it to settle between 0 and 12 inclusive
	return Math.floor(Math.random()*(SLOTS_PER_REEL));
}

function spin(timer) {
	//var txt = 'seeds: ';
	for(var i = 1; i < 3; i ++) {
		var oldSeed = -1;
		/*
		checking that the old seed from the previous iteration is not the same as the current iteration;
		if this happens then the reel will not spin at all
		*/
		var oldClass = $('#ring'+i).attr('class');
    console.log(String(oldClass));
		if(oldClass > 4) {
			oldSeed = parseInt(oldClass.slice(10));
		}
		var seed = getSeed();
    console.log('ring spin-' + seed);
		while(String(oldClass).trim() == String('ring spin-' + seed).trim()) {
      console.log('repeat')
      seed = getSeed();
		}
		$('#ring'+i)
			.css('animation','back-spin 1s, spin-' + seed + ' ' + (timer + i*0.5) + 's')
			.attr('class','ring spin-' + seed);
	}

	console.log('=====');
}

$(document).ready(function() {

	// initiate slots 
 	createSlots($('#ring1'));
 	createSlots($('#ring2'));

 	// hook start button
 	$('.go').on('click',function(){
 		var timer = 2;
 		spin(timer);
 	})

 	// hook xray checkbox
 	$('#xray').on('click',function(){
 		//var isChecked = $('#xray:checked');
 		var tilt = 'tiltout';
 		
    if($(this).is(':checked')) {
 			tilt = 'tiltin';
 			$('.slot').addClass('backface-on');
 			$('#rotate').css('animation',tilt + ' 2s 1');

			setTimeout(function(){
			  $('#rotate').toggleClass('tilted');
			},2000);
 		} else {
      tilt = 'tiltout';
 			$('#rotate').css({'animation':tilt + ' 2s 1'});

			setTimeout(function(){
	 			$('#rotate').toggleClass('tilted');
	 			$('.slot').removeClass('backface-on');
	 		},1900);
 		}
 	})

 	// hook perspective
 	$('#perspective').on('click',function(){
 	  $('#stage').toggleClass('perspective-on perspective-off');
 	})	
 });