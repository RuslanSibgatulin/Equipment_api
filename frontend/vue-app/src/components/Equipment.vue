<template>
    <div class="container">
      <div class="row">
        <div class="col-md-8">
          <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="Search"
              v-model="query"/>
            <div class="input-group-append">
              <button class="btn btn-outline-secondary" type="button" @click="searchEquipment">Search</button>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-8">
          <h1>Equipment list</h1>
          <hr>
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">SN</th>
                <th scope="col">Type</th>
                <th scope="col">Description</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(item) in eq_items" v-bind:key="item.id" @click=editEquipment(item)>
                <td>{{ item.sn }}</td>
                <td>{{ getType(item.type).name }}</td>
                <td>{{ item.description }}</td>
                <td>
                  <div class="btn-group btn-group" role="group" aria-label="Item button group">
                    <button type="button" class="btn btn-danger btn-sm" @click="deleteEquipment(item)">
                      Del
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="col-sm-4">
          <h1>Editor</h1>
          <hr>
          <form>
          <label for="type" class="form-label">Type</label>            
          <select class="form-select" aria-label="Equipment type" v-model="eq_type" required>
            <option v-for="option in eq_types" v-bind:key="option" v-bind:value="option.id">
              {{ option.name }}
            </option>
          </select>

          <label for="sn_value" class="form-label">Serial number</label>
          <input type="text" class="form-control" id="sn_value"  v-model="eq_sn" placeholder="SN" required>
          <span v-if=eq_type>Use SN mask: {{ this.getType(eq_type).sn_mask }}</span>

          
          <div class="form-group">
            <label for="descriptioin">Description</label>
            <textarea class="form-control" id="descriptioin" v-model="eq_desc" rows="3"></textarea>
          </div>
          <br>
          <div class="form-group">
            <button  v-if=current_id class="btn btn-success" type="button" @click="updateEquipment">Modify</button>
            <button  v-else class="btn btn-success" type="button" @click="addEquipment">Add</button>
            <button class="btn btn-outline-secondary" type="button" @click="clearForm">Clear</button>
          </div>

        </form>
        </div>

      </div>
    </div>

  </template>
  
  <script>
  import EquipmentDataService from "../services/EquipmentDataService";
  
  export default {
    name: "items-list",
    data() {
      return {
        query: "",
        eq_items: [],
        eq_types: [],
        eq_type: "",
        eq_sn: "",
        eq_desc: "",
        current_id: "",
      };
    },
    methods: {
      retrieveitems() {
        EquipmentDataService.getAll()
          .then(response => {
            this.eq_items = response.data.results;
            // console.log(response.data);
          })
          .catch(e => {
            console.log(e);
          });        
      },

      retrievetypes() {
        EquipmentDataService.getAllTypes()
          .then(response => {
            this.eq_types = response.data.results;
            // console.log(response.data);
          })
          .catch(e => {
            console.log(e);
          });
      },
      
      searchEquipment() {
        EquipmentDataService.find(this.query)
          .then(response => {
            this.eq_items = response.data.results;
            console.log(response.data);
          })
          .catch(e => {
            console.log(e.message);
          });
      },
      addEquipment() {
        let new_item = {sn: this.eq_sn, description: this.eq_desc, type: this.eq_type}
        EquipmentDataService.create(new_item).then(response => {
            console.log(response.data);
            this.retrieveitems();
          })
          .catch(e => {
            if (e.response.data) {
              this.showError(e.response.data);
            }
          });
                
      },
      editEquipment(eq) {
        this.current_id = eq.id;
        this.eq_type = eq.type;
        this.eq_sn = eq.sn;
        this.eq_desc = eq.description;
      },
      clearForm() {
        this.current_id = "";
        this.eq_type = "";
        this.eq_sn = "";
        this.eq_desc = "";
      },

      updateEquipment() {
        let item = {sn: this.eq_sn, description: this.eq_desc, type: this.eq_type}
        EquipmentDataService.update(this.current_id, item).then(response => {
            console.log(response.data);
            this.retrieveitems();
          })
          .catch(e => {
            if (e.response.data) {
              this.showError(e.response.data);
            }
            console.error(e);
          });
                
      },

      deleteEquipment(eq) {
        let confirmation = `Delete an equipment ${eq.sn}?`;
        if (confirm(confirmation)) {
          EquipmentDataService.delete(eq.id)
          .then(response => {
            console.log(response.data);
            this.clearForm();
            this.retrieveitems();
          })
          .catch(e => {
            console.log(e);
          });
        }
      },
      showError(data) {
        alert(data.detail);
      },
      getType(id) {
        return this.eq_types.filter(item => item.id === id)[0];
      }

    },
    mounted() {
      this.retrieveitems();
      this.retrievetypes();
    },
  };
  </script>
  