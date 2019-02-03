var config = {
    openSocket: function(config) {
        var SIGNALING_SERVER = 'http://localhost:8888/';
        var SIGNALING_SERVER = 'https://webrtcweb.com:9559/';

        config.channel = config.channel || location.href.replace(/\/|:|#|%|\.|\[|\]/g, '');
        var sender = Math.round(Math.random() * 999999999) + 999999999;

        io.connect(SIGNALING_SERVER).emit('new-channel', {
            channel: config.channel,
            sender: sender
        });

        var socket = io.connect(SIGNALING_SERVER + config.channel);
        socket.channel = config.channel;
        socket.on('connect', function() {
            if (config.callback) config.callback(socket);
        });

        socket.send = function(message) {
            socket.emit('message', {
                sender: sender,
                data: message
            });
        };

        socket.on('message', config.onmessage);
    },
    onRemoteStream: function(media) {
        var video = media.video;
        video.classList.add('peer-video')
        participants.insertBefore(video, participants.firstChild);
        video.play();
    },
    onRoomFound: function(room) {
        var alreadyExist = document.getElementById(room.broadcaster);
        if (alreadyExist) return;

        if (typeof roomsList === 'undefined') roomsList = document.body;

        var tr = document.createElement('tr');
        tr.setAttribute('id', room.broadcaster);
        tr.innerHTML = '<td>' + room.roomName + '</td>' +
            '<td><button class="join" id="' + room.roomToken + '">Join Room</button></td>';
        roomsList.insertBefore(tr, roomsList.firstChild);

        tr.onclick = function() {
            tr = this;
            captureUserMedia(function() {
                broadcastUI.joinRoom({
                    roomToken: tr.querySelector('.join').id,
                    joinUser: tr.id
                });
            });
            hideUnnecessaryStuff();
        };
    }
};

function createButtonClickHandler() {
	console.log("HELLO");
    captureUserMedia(function() {
        broadcastUI.createRoom({
            roomName: (document.getElementById('conference-name') || { }).value || 'Anonymous'
        });
    });
    hideUnnecessaryStuff();
}

function captureUserMedia(callback) {
    var video = document.createElement('video');
    video.setAttribute('autoplay', true);
    video.setAttribute('controls', true);
    video.muted = true
    video.controls = false
    video.classList.add('self-video')
    var host = document.getElementById('self-video')
    
    host.appendChild(video);

    getUserMedia({
        video: video,
        onsuccess: function(stream) {
            config.attachStream = stream;
            callback && callback();
        },
        onerror: function() {
            alert('unable to get access to your webcam.');
            callback && callback();
        }
    });
}

/* on page load: get public rooms */
var broadcastUI = broadcast(config);

/* UI specific */
var participants = document.getElementById("participants") || document.body;
var startConferencing = document.getElementById('start-conferencing');
var roomsList = document.getElementById('rooms-list');

if (startConferencing) startConferencing.onclick = createButtonClickHandler;

function hideUnnecessaryStuff() {
    var visibleElements = document.getElementsByClassName('visible'),
        length = visibleElements.length;
    for (var i = 0; i < length; i++) {
        visibleElements[i].style.display = 'none';
    }
}