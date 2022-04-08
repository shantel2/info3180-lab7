<template>
    <form @submit.prevent="uploadPhoto" id="uploadForm" method="post" enctype="multipart/form-data">

        <div class="form-data">
            <h1>Upload Form</h1>

            <label for="description" class="description"> Description</label>
            <textarea name="description" id="" cols="45" rows="10"></textarea>

            <div  class="upload-area">
                <label for="photo" class="photo">Photo Upload</label>
                <input type="file" name="photo" id="photo">
            </div>
            
            <button type="submit">Upload</button>

        </div>
                    
    </form>
</template>


<script>
export default {
    data() {
        return {
            csrf_token: ''
        }
    },
    created() {
        this.getCsrfToken();
    },
     methods:{
        uploadPhoto(){
            let uploadForm = document.getElementById('uploadForm');
            let form_data = new FormData(uploadForm);
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
                console.log(data);
            })
            .catch(function (error) {
                console.log(error);
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
    }
}
</script>


<style>
.description, button, .upload-area{
    display: block;
}

textarea, .upload-area{
    margin-top: 1rem;
}

.photo{
    margin-right: 1rem;
}

button{
    background: rgb(74, 74, 161);
    border: 2px solid (157, 157, 193);
    border-radius: 5px;
    margin-top: 2rem;
}

#uploadForm{
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>