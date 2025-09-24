(function () {
  function initPlaylist(group) {
    var players = group.querySelectorAll('audio');
    var items = group.querySelectorAll('.audio-playlist li');
    if (!players.length || !items.length) {
      return;
    }

    function activate(index) {
      items.forEach(function (item, itemIndex) {
        if (itemIndex === index) {
          item.classList.add('is-active');
        } else {
          item.classList.remove('is-active');
        }
      });
    }

    items.forEach(function (item, index) {
      item.addEventListener('click', function () {
        var player = players[index];
        if (!player) return;
        players.forEach(function (other) {
          if (other !== player) {
            other.pause();
          }
        });
        player.currentTime = 0;
        player.play();
        activate(index);
      });
    });

    players.forEach(function (player, index) {
      player.addEventListener('play', function () {
        activate(index);
      });
      player.addEventListener('ended', function () {
        var nextIndex = (index + 1) % players.length;
        if (nextIndex !== index) {
          players[nextIndex].play();
        }
      });
    });

    activate(0);
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.audio-player-group').forEach(initPlaylist);
  });
})();
