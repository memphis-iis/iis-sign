(function(module){
    module.keys = module.keys || {};

    var special_map = {
        32: 'space',
        33: 'page-up',
        34: 'page-down',
        35: 'end',
        36: 'home',
        37: 'left-arrow',
        38: 'up-arrow',
        39: 'right-arrow',
        40: 'down-arrow'
    };

    module.keys.special_map = special_map;

    module.keys.xlate = function(keyCode) {
        if (keyCode >= 65 && keyCode <= 90) {
            return String.fromCharCode(keyCode);
        }
        else {
            return special_map[keyCode];
        }
    };
})(window || this);
