<template>
    <form action="" @submit.prevent="uploadPhoto" id="uploadForm" method="POST" enctype="multipart/form-data">

    <div>
        <label for="description"> Description</label>
        <textarea name="description" id="" cols="30" rows="10"></textarea>

        <label for="photo">Photo Upload</label>
        <input type="file" name="photo" id="photo">
        <button type="submit">Upload</button>

    </div>
                    
    </form>
</template>


<script>
export default {
 data() {
 return {
            csrf_token: '', 
            errors: [],
            success: false
     }
 },
 methods: {
         uploadPhoto(){
            let uploadForm = document.getElementById('uploadForm');
            let form_data = new FormData(uploadForm);

            let self = this
            fetch("/api/upload", {
                method: 'POST',
                body: form_data,
                headers: {
                    'X-CSRFToken': this.csrf_token
                }
            })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                // display a success message
                console.log(data, "data");
                if('errors' in data){
                    self.errors = [...data.errors]
                    self.success = false
                } else {
                    self.errors = []
                    self.success = true
                }
            })
            .catch(function (error) {
                
                console.log(error, "error");
            });
        },
        getCsrfToken() {
            let self = this;
            fetch('/api/csrf-token')
                .then((response) => response.json())
                .then((data) => {
                console.log(data);
                self.csrf_token = data.csrf_token;
            })
        }
},
created() {
    this.getCsrfToken();
  }
}
</script>