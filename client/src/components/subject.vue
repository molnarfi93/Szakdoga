<template>
<table>
    <tr>
        <div class="header">Add subjects</div>
    </tr>
    <tr>
        <div class="panel">
            Name: <input type="text" v-model="subject.name"><br />
			<br />
            <button v-on:click="addSubject" class="ok">Add</button><br />
			<br />
            <br />
            <br />
			Added subjects:
			<ul>
				<li v-for="subject in added_subjects">
					{{subject.name}}
				<button v-on:click="deleteSubject(subject.name)"><img src="cross.png"/></button></li>
			</ul><br />
			<br />
			<button v-on:click="$router.push({name: 'edit_timetable', params: {timetable: $route.params.timetable}})">Go back</button>
        </div>
    </tr>
</table>
</template>

<script>
    import axios from "axios";
    export default {
        name: "subject",
        data() {
            return {
                subject: {
                    name: "",
					timetable: ""
                },
				added_subjects: [
				]
			}	
		},
		created() {
			this.subject.timetable = this.$route.params.timetable;
			let request = {
                "method": "GET",
                "url": process.env.VUE_APP_BASE_URL + "/api/subjects?timetable_name=" + this.$route.params.timetable,
                "headers": {
                    "content-type": "application/json"
                }
            };
            axios(request).then(
                result => {
					this.added_subjects = result.data
                },
                error => {
                    console.error(error);
                }
            );
 	    },
        methods: {
            checkSubjectDatas() {
      	        if (this.subject.name == "") {
                    return false;
                }
                return true;
            },
			refreshSubjects() {
      	        let request = {
                    "method": "GET",
                    "url": process.env.VUE_APP_BASE_URL + "/api/subjects?timetable_name=" + this.$route.params.timetable,
                    "headers": {
                        "content-type": "application/json"
                    }
                };
                axios(request).then(
                    result => {
						axios.defaults.headers.common['Authorization'] = this.token;
						this.added_subjects = result.data
                    },
                    error => {
                        console.error(error);
                    }
                );
            },
			addSubject(event) {
      	        if (this.checkSubjectDatas() == false) {
                    console.log("All fields must be fulfilled!");
                    return;
                }
      	        let request = {
                    "method": "POST",
                    "url": process.env.VUE_APP_BASE_URL + "/api/subjects",
                    "data": this.subject,
                    "headers": {
                        "content-type": "application/json"
                    }
                };
                axios(request).then(
                    result => {
						this.refreshSubjects();
                    },
                    error => {
                        console.error(error);
                    }
                );
            },
			deleteSubject(name) {
				let request = {
                    "method": "DELETE",
                    "url": process.env.VUE_APP_BASE_URL + "/api/subjects?name=" + name,
                    "headers": {
                        "content-type": "application/json"
                    }
                };
                axios(request).then(
                    result => {
						this.refreshSubjects();
                    },
                    error => {
                        console.error(error);
                    }
                );
            }
        }
    }
</script>

