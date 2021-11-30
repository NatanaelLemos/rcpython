state = {
    horn: false,
    direction: 0
};

(() => {
    postState = () => {
        post(JSON.stringify(state));
    }

    post = (content) => {
        const xhttp = new XMLHttpRequest();
        xhttp.open('POST', '/', true);
        xhttp.setRequestHeader('Content-Type', 'application/json');
        xhttp.send(content);
    }

    setInterval(postState, 150);
})();