import { createStore } from 'vuex';

const store = createStore({
    state() {
        return {
            serverhost: 'http://192.168.1.36:5000'
        };
    },
    getters: {
        getServerHost: (state) => state.serverhost,
    }
});

export default store;
