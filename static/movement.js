class Movement {
    pressedKeys = [];

    onKeyDown = (e) => {
        this.onKeyPressed(e.code);
    }

    onKeyUp = (e) => {
        this.onKeyUnpressed(e.code);
    }

    onMouseDown = (e) => {
        this.pressedKeys = [];
        this.onBtnSwitch(e.srcElement.id, this.onKeyPressed);
    }

    onMouseUp = (e) => {
        this.onBtnSwitch(e.srcElement.id, this.onKeyUnpressed);
        this.pressedKeys = [];
    }

    onBtnSwitch = (btnId, func) => {
        switch (btnId) {
            case 'btnTL':
                func('ArrowUp');
                func('ArrowLeft');
                break;
            case 'btnT':
                func('ArrowUp');
                break;
            case 'btnTR':
                func('ArrowUp');
                func('ArrowRight');
                break;
            case 'btnL':
                func('ArrowLeft');
                break;
            case 'btnR':
                func('ArrowRight');
                break;
            case 'btnBL':
                func('ArrowDown');
                func('ArrowLeft');
                break;
            case 'btnB':
                func('ArrowDown');
                break;
            case 'btnBR':
                func('ArrowDown');
                func('ArrowRight');
                break;
        }
    }

    onKeyPressed = (key) => {
        const alreadyPressing = this.pressedKeys.some(k => k === key);
        if (alreadyPressing) {
            return;
        }

        this.pressedKeys.push(key);
        state.direction = this.defineCurrentDirection();
        console.log('direction');
        console.log(state.direction);
    }

    onKeyUnpressed = (key) => {
        this.pressedKeys = this.pressedKeys.filter(k => k !== key);
        state.direction = this.defineCurrentDirection();
    }

    defineCurrentDirection = () => {
        let direction = 0;
        if (this.pressedKeys.some(k => k === 'ArrowUp')) {
            direction += 1000;
        }
        if (this.pressedKeys.some(k => k === 'ArrowDown')) {
            direction += 100;
        }
        if (this.pressedKeys.some(k => k === 'ArrowLeft')) {
            direction += 10;
        }
        if (this.pressedKeys.some(k => k === 'ArrowRight')) {
            direction += 1;
        }

        return direction;
    }
}

(() => {
    const movement = new Movement();

    document.addEventListener('keydown', movement.onKeyDown);
    document.addEventListener('keyup', movement.onKeyUp);
    document.querySelectorAll('button').forEach(btn => btn.addEventListener('mousedown', movement.onMouseDown));
    document.querySelectorAll('button').forEach(btn => btn.addEventListener('mouseup', movement.onMouseUp));
})();