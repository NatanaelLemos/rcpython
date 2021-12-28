class Horn {
    pressedKeys = [];

    onKeyDown = (e) => {
        this.onKeyPressed(e.code);
    }

    onKeyUp = (e) => {
        this.onKeyUnpressed(e.code);
    }

    onKeyPressed = (key) => {
        const alreadyPressing = this.pressedKeys.some(k => k === key);
        if (alreadyPressing) {
            return;
        }

        this.pressedKeys.push(key);
        state.horn = this.hasPressedHorn();
    }

    onKeyUnpressed = (key) => {
        this.pressedKeys = this.pressedKeys.filter(k => k !== key);
        state.horn = this.hasPressedHorn();
    }

    hasPressedHorn = () => {
        return this.pressedKeys.some(k => k === 'Space');
    }
}

(() => {
    const horn = new Horn();

    document.addEventListener('keydown', horn.onKeyDown);
    document.addEventListener('keyup', horn.onKeyUp);
})();