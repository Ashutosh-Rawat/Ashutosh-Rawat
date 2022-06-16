var wavesurfer = WaveSurfer.create({
    container: '#waveform',
    waveColor:  '#333',
    progressColor: 'hsla(200, 100%, 30%, 0.5)',
    barHeight: 2
});


var microphone = Object.create(WaveSurfer.Microphone);

microphone.init({
    wavesurfer: wavesurfer
});

microphone.on('deviceReady', function(stream) {
    console.log('Device ready!', stream);
});
microphone.on('deviceError', function(code) {
    console.warn('Device error: ' + code);
});


const btn = document.querySelector('.btn');

btn.onmousedown = function () {
    console.log("Mouse Down")
    document.querySelector('.mic').src='on.svg';
    microphone.start();
    }

btn.onmouseup = function () {
    microphone.stop();
    console.log("Mouse Up");
    document.querySelector('.mic').src='off.svg';
    }

btn.addEventListener("mouseover", function( event ) {
    microphone.stop();
    console.log("Mouse Over");
    document.querySelector('.mic').src='off.svg';
    });

btn.addEventListener("mouseout", function( event ) {
    microphone.stop();
    console.log("Mouse Out");
    document.querySelector('.mic').src='off.svg';
    });

// pause rendering
//microphone.pause();

// resume rendering
//microphone.play();

// stop visualization and disconnect microphone
//microphone.stopDevice();

// same as stopDevice() but also clears the wavesurfer canvas
// microphone.stop();

// destroy the plugin
//microphone.destroy();