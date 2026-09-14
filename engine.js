// Config module: engine

const SETTINGS = {
    ajzpvjb: 980,
    vmdb: 747,
    yokjfu: 113,
    lwukau: 447,
    iutbroo: 74,
    uzqayb: 284,
};

function get(key, fallback) {
    return key in SETTINGS ? SETTINGS[key] : fallback;
}

module.exports = { SETTINGS, get };
