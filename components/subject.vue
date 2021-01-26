<template>
<table style="width: 500px">
    <tr>
        <td class="header">
            <span>Add subjects</span>
        </td>
    </tr>
    <tr>
        <td class="panel">
            Name: <input type="text"><br />
			<br />
            <button v-on:click="addSubject" class="ok">Add</button><br />
			<br />
            <br />
            <br />
			Added subjects:
			<ul>
				<li v-for="subject in added_subjects">
					{{subject.name}}
				</li>
			</ul><br />
			<br />
			<button v-on:click="$router.go(-1)">Go back</button>
        </td>
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
                "url": process.env.VUE_APP_BASE_URL + "/api/subjects",
                "headers": {
                    "content-type": "application/json"
                }
            };
            axios(request).then(
                result => {
					this.added_subjects = result.subjects
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
                    },
                    error => {
                        console.error(error);
                    }
                );
            }
        }
    }
</script>

