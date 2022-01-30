<template>
  <div class="mydiv">
  <!-- Include a header DIV with the same name as the draggable DIV, followed by "header" -->
  <div class="mydivheader" @mousedown="dragMouseDown">{{title}}</div>
  <div class="mainbox">
      <input class="eq-input" type="text" placeholder="Enter equation"/>
    </div> 
  
</div>
</template>

<script>
export default {
    props: {
        title: String
    },

    data: ()=>({
        pos1: 0,
        pos2: 0,
        pos3: 0,
        pos4: 0
    }),

    methods: {
        dragMouseDown: function(e) {
            e = e || window.event;
            e.preventDefault();
            // get the mouse cursor position at startup:
            this.pos3 = e.clientX;
            this.pos4 = e.clientY;
            document.onmouseup = this.closeDragElement;
            // call a function whenever the cursor moves:
            document.onmousemove = this.elementDrag;
        },

        elementDrag: function(e) {
            e = e || window.event;
            e.preventDefault();
            // calculate the new cursor position:
            this.pos1 = this.pos3 - e.clientX;
            this.pos2 = this.pos4 - e.clientY;
            this.pos3 = e.clientX;
            this.pos4 = e.clientY;
            // set the element's new position:
            this.$el.style.top = (this.$el.offsetTop - this.pos2) + "px";
            this.$el.style.left = (this.$el.offsetLeft - this.pos1) + "px";
        },

        closeDragElement: function () {
            document.onmouseup = null;
            document.onmousemove = null;
        }
    }


}
</script>

<style>
.mydiv {
  position: absolute;
  z-index: 9;
  background-color: #f1f1f1;
  text-align: center;
  
}

.mydivheader {
  padding: 10px;
  cursor: move;
  z-index: 10;
  background-color: #500000;
  color: #FFFFFF;
}

.mainbox{
    height: 300px;
    width: 500px;
    border: 1px solid black;
    border-radius: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
}


.eq-input{
    margin-top: 40px;
    width: 70%;
}
</style>
