<template>
    <div>
      <h1>Login</h1>
      <form @submit.prevent="login">
        <div class="form-group">
          <input
            type="text"
            class="form-control"
            v-model="username"
            placeholder="username"
          />
          <br />
          <input
            class="form-control"
            v-model="password"
            placeholder="password"
            type="password" 
          />
         <br />
          <button class="btn btn-success" type="submit">Login</button>
        </div>
      </form>
    </div>
  </template>

  <script>
  import EquipmentDataService from "../services/EquipmentDataService";

  export default {
    name: "login-form",
    data() {
      return {
        username: "",
        password: "",
      };
    },
    methods: {
      login() {
        EquipmentDataService.getJWT(this.username, this.password).then(response => {
            localStorage.username = this.username;
            localStorage.token = response.data.access;
            localStorage.refresh = response.data.refresh;
            this.$router.push("/")
          })
          .catch(e => {
            if (e.response.data) {
              alert(`Login failed!`);
            }
            console.error(e);
          });
      }
    }
  };

  </script>