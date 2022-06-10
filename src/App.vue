<template>
  <div>
    <h1>Hello World</h1>
    <h2>Count {{ counter }} </h2>
    <input v-model="phoneNumber" type="tel" id="phone" name="phone" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}">
    <input v-model="textMessage" type="text">
    <button @click="sendTextMessage()">Send Message</button>

    <input type="password">
    <input type="checkbox">
    <br>
    <button @click="myBtn">Increase Count</button>
  </div>
</template>

<script>

export default {
  name: "App",
  data: function(){
    return { 
      counter: 0, 
      textMessage: '',
      phoneNumber: ''
      }
  },
  methods: {
    myBtn() {
      this.counter ++ 
      console.log(window.pywebview.api.showCount(this.counter));
      
    }, 
    sendTextMessage(){
      window.pywebview.api.sendImessage(this.phoneNumber, this.textMessage)
    }
  }
}
</script>

<style scoped>

</style>