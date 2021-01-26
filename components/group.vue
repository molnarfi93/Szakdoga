<template>
<table style="width: 500px">
    <tr>
        <td class="header">
            <span>Add groups</span>
        </td>
    </tr>
    <tr>
        <td class="panel">
            Name: <input type="text" v-model="group.name"><br />
            <br />
			Grade: <input type="text" v-model="group.grade"><br />
			<br />
			Headcount: <input type="text" v-model="group.headcount"><br />
			<br />
			Subjects:<br />
			<span v-for="i in num_subjects" :key="i">
				Name: <select multiple v-model="group.subjects[i].name" placeholder="Choose!"><br />
					<option v-for="subject in available_subjects" v-bind:value="subject">
						{{subject}}
					</option>
				</select>
				Type: <select v-model="group.subjects[i].type" placeholder="Choose!">
					<option v-for="type in types" v-bind:value="type">
						{{type}}
					</option>
				</select>
				Weekly periods: <input type="text" v-model="group.subjects[i].weekly_periods">
				<span v-if="timetable.add_manually == true">
					Teacher: <select v-model="group.subjects[i].teacher" placeholder="Choose!">
						<option v-for="teacher in available_teachers" v-bind:value="teacher">
							{{teacher}}
						</option>
					</select>
				</span><br />
			<span><br />	
			<button v-on:click="oneMoreSubject">One more subject</button><br />
			<br />
			<button v-on:click="addGroup" class="ok">Add</button><br />
			<br />
            <br />
            <br />
			Added groups:
			<ul>
				<li v-for="group in added_groups">
					{{group.name}} ({{group.grade}}, {{group.headcount}},
					<ul>
						<li v-for="subject in subjects">
							{{subject}},
						</li>
					</ul>
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
        name: "group",
        data() {
			num_subjects = 1;
			let subjects = []
			for (let i = 0; i < num_subjects; ++i) {
				subject = {
					name: "",
					type: "",
					weekly_periods: 0,
					teacher: ""
				}
			}	
			subjects.push(subject);
            return {
                group: {
                    name: "",
					grade: "",
                    headcount: 0,
					timetable: "",
					subjects: subjects
                },
				timetable: {
				},
				types: [
				],
				available_subjects: [
				],
				available_teachers: [
				],
				added_groups: [
				]
            }
        },
		created() {
			this.group.timetable = this.$route.params.timetable;
			if (this.timetable.type == "middle school") {
				this.group.types = [normal, language, special];
			}
			if (this.timetable.type == "high school") {
				this.group.types = [normal, language, fact];
			}
			if (this.timetable.type == "college/university") {
				this.group.types = [lecture, practice];
			}
    	    let request = {
                "method": "GET",
                "url": process.env.VUE_APP_BASE_URL + "/api/groups",
                "headers": {
                    "content-type": "application/json"
                }
            };
            axios(request).then(
                result => {
					this.added_groups = result.groups
                },
                error => {
                    console.error(error);
                }
            );
			let request = {
                "method": "GET",
                "url": process.env.VUE_APP_BASE_URL + "/api/subjects",
                "headers": {
                    "content-type": "application/json"
                }
            };
            axios(request).then(
                result => {
					this.available_subjects = result
                },
                error => {
                    console.error(error);
                }
            );
			let request = {
                "method": "GET",
                "url": process.env.VUE_APP_BASE_URL + "/api/teachers",
                "headers": {
                    "content-type": "application/json"
                }
            };
            axios(request).then(
                result => {
					this.available_teachers = result
                },
                error => {
                    console.error(error);
                }
            );
		},
		mounted() {
			let request = {
                "method": "GET",
                "url": process.env.VUE_APP_BASE_URL + "/api/timetables/" + timetable.name,
                "headers": {
                    "content-type": "application/json"
                }
            };
            axios(request).then(
                result => {
					this.timetable = result
                },
                error => {
                    console.error(error);
                }
            );
 	    },
        methods: {
            checkGroupDatas() {
      	        if (this.group.name == "") {
                    return false;
                }
                if (this.group.grade == "") {
                    return false;
                }
				if (this.group.headcount == "") {
                    return false;
                }
				if (this.group.subjects.length == 0) {
					return false;
				}
				for (let i = 0; i < this.group.subjects.length; ++i) {
					if (this.group.subjects[i].name == "") {
						return false;
					}
				}	
				if (this.group.subjects[i].type == "") {
					return false;
				}
				if (this.group.subjects[i].weekly_periods == "") {
					return false;
				}
				if (this.timetable.add_manually == true) {
					if (this.group.subjects[i].teacher == "") {
						return false;
					}
				}
				return true;
		    }, 
			addGroup(event) {
      	        if (this.checkGroupDatas() == false) {
                    console.log("All fields must be fulfilled, and you must add at least one subject!");
                    return;
                }
      	        let request = {
                    "method": "POST",
                    "url": process.env.VUE_APP_BASE_URL + "/api/groups",
                    "data": this.group,
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
			oneMoreSubject(event) {
				num_subjects = num_subjects + 1;
				return;
			}
        }
    }
</script>

