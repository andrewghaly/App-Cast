$(function () {
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/control');

    var videoContents = function (event) {
        var videoPlayer = document.querySelector('video')
        var file = this.files[0]
        var fileURL = URL.createObjectURL(file)
        videoPlayer.src = fileURL
    }

    var videoInput = document.querySelector('input')
    videoInput.addEventListener('change', videoContents, false)

    socket.on('control-update', function (msg) {
        if (msg.message == 'pause') {
            $('#cast-video').get(0).pause();
        } else if (msg.message == 'play') {
            $('#cast-video').get(0).play();
        }
    });
});