<template>
    <div v-if="show" class="popup">
        <div class="popup-content" @click="closePopup">
            <p>{{ message }}</p>
        </div>
    </div>
</template>
<script>
export default {
    props: {
        show: Boolean,
        message: String,
        autoCloseDelay: {
            type: Number,
            default: 4000,
        },
    },
    methods: {
        closePopup() {
            this.$emit('close');
        },
    },
    watch: {
        show(newVal) {
            if (newVal) {
                setTimeout(() => {
                    this.closePopup();
                }, this.autoCloseDelay);
            }
        },
    },
};
</script>
  
 
<style scoped>
.popup {
    background-color: rgb(252, 85, 85);
    color: black;
    padding: 1rem;
    position: absolute;
    z-index: 100;
    bottom: 0;
    right: 0;
    transition: transform 0.6s ease-in-out;
    
}


</style>