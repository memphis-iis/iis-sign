/* util.js - Some utilities we provide for our sign pages

* utils.isTrue - tests for boolean truth where the string true is translated
  to boolean true

* utils.getParameterByName - Return a URL Parameter (i.e. the query string)
  for the current URL. If the page is foo.html?a=&b=Here then
  utils.getParameterByName('a') returns '' and
  utils.getParameterByName('b') returns 'Here' and
  utils.getParameterByName('c') returns null

* keys.xlate - Translates keycodes into either the letter pressed or a string
  representing a key we're interested in. See ../sign.html for main usage
***************************************************************************/

(function(module){
    module.utils = module.utils || {};

    module.utils.isTrue = function(b) {
        if (_.isBoolean(b)) {
            return b;
        }
        else if (!b) {
            return false;
        }
        else {
            return _.trim('' + b).toLowerCase() === "true";
        }
    };

    module.utils.getParameterByName = function(name, url) {
        if (!url) {
            url = window.location.href;
        }

        name = name.replace(/[\[\]]/g, "\\$&");
        var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)", "i");
        var results = regex.exec(url);
        if (!results) {
            return null;
        }
        if (!results[2]) {
            return '';
        }
        return decodeURIComponent(results[2].replace(/\+/g, " "));
    };

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
