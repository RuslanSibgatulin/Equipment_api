<template>
  <div id="app">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
      <router-link to="/" class="navbar-brand">K Telekom</router-link>
      <div class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link to="/equipment" class="nav-link">Equipment</router-link>
        </li>
        <li class="nav-item">
          <a class="nav-link" @click="logout">{{ getUser() }}</a>
        </li>
      </div>
    </nav>

    <div class="container mt-3">
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  name: "app",
  methods: {
    getUser() {
      return localStorage.username
    },
    logout() {
      let confirmation = `Logout?`;
      if (confirm(confirmation)) {
        localStorage.removeItem("token");
        localStorage.removeItem("username");
        localStorage.removeItem("refresh");
      }
    }
  }
};
</script>
