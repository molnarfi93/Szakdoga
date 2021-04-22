<template>
<table>
    <tr>
        <div class="header">Add groups</div>
    </tr>
    <tr>
        <div class="panel">
            Name: <input type="text" v-model="group.name"><br />
            <br />
			Grade: <input type="text" v-model="group.grade"><br />
			<br />
			Headcount: <input type="text" v-model="group.headcount"><br />
			<br />
			Subjects:<br />
			<div v-for="(item, index) in group.subjects" :key="index">
				Name: <select v-model="item.name" placeholder="Choose!">
					<option v-for="subject in available_subjects" v-bind:value="subject.name">
						{{subject.name}}
					</option>
				</select>
				Type: <select v-model="item.type" placeholder="Choose!">
					<option v-for="type in types" v-bind:value="type">
						{{type}}
					</option>
				</select>
				Weekly periods: <input type="text" v-model="item.weekly_periods">
				<div v-if="timetable.add_manually == true">
					Teacher: <select v-model="item.teacher" placeholder="Choose!">
						<option v-for="teacher in available_teachers" v-bind:value="teacher">
							{{teacher.name}}
						</option>
					</select>
				</div><br />	
			</div><br />
			<button v-on:click="oneMoreSubject">One more subject</button><br />
			<br />
			<button v-on:click="addGroup" class="ok">Add</button><br />
			<br />
			<br />
			<br />
			Added groups:
			<ul>
				<li v-for="group in added_groups">
					{{group.name}} ({{group.grade}}, {{group.headcount}}, subjects:
					<ul>
						<li v-for="subject in group.subjects">
							{{subject.name}} ({{subject.type}}, {{subject.weekly_periods}}, {{subject.teacher}})
						</li>)
					</ul>
					<button v-on:click="deleteGroup(group.name)"><img src="cross.png"/></button>
				</li>
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
        name: "group",
        data() {
            return {
                group: {
                    name: "",
					grade: "",
                    headcount: 0,
					subjects: [],
					timetable: ""
                },
				num_subjects: 0,
				types: [
				],
				available_subjects: [
				],
				available_teachers: [
				],
				added_groups: [
				],
				timetable: {
				}
            }
        },
		created() {
			this.group.timetable = this.$route.params.timetable;
			let request = {
				"method": "GET",
				"url": process.env.VUE_APP_BASE_URL + "/api/subjects?timetable_name=" + this.group.timetable,
				"headers": {
					"content-type": "application/json"
				}
			};
			axios(request).then(
				result => {
					this.available_subjects = result.data
					let request = {
						"method": "GET",
						"url": process.env.VUE_APP_BASE_URL + "/api/teachers?timetable_name=" + this.group.timetable,
						"headers": {
							"content-type": "application/json"
						}
					};
					axios(request).then(
						result => {
							this.available_teachers = result.data
							let request = {
								"method": "GET",
								"url": process.env.VUE_APP_BASE_URL + "/api/groups?timetable_name=" + this.$route.params.timetable,
								"headers": {
									"content-type": "application/json"
								}
							};
							axios(request).then(
								result => {
									this.added_groups = result.data
								},
								error => {
									console.error(error);
								}
							);
						},
						error => {
							console.error(error);
						}
					);
				},
				error => {
					console.error(error);
				}
			);
		},
		mounted() {
			let request = {
				"method": "GET",
				"url": process.env.VUE_APP_BASE_URL + "/api/timetables?name=" + this.group.timetable,
				"headers": {
					"content-type": "application/json"
				}
			};
			axios(request).then(
				result => {
					this.timetable = result.data
					if (this.timetable.type == "middle school") {
						this.types = ["normal", "language", "special"];
					}
					if (this.timetable.type == "high school") {
						this.types = ["normal", "language", "fact"];
					}
					if (this.timetable.type == "college/university") {
						this.types = ["lecture", "practice"];
					}
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
					if (this.group.subjects[i].type == "") {
						return false;
					}
					this.group.subjects[i].weekly_periods = parseInt(this.group.subjects[i].weekly_periods);
					if (this.group.subjects[i].weekly_periods == 0) {
						return false;
					}
					if (this.timetable.add_manually == true) {
						if (this.group.subjects[i].teacher == "") {
							return false;
						}
					}
				}	
				return true;
		    },
			refreshGroups() {
				let request = {
					"method": "GET",
					"url": process.env.VUE_APP_BASE_URL + "/api/groups?timetable_name=" + this.$route.params.timetable,
					"headers": {
						"content-type": "application/json"
					}
				};
				axios(request).then(
					result => {
						axios.defaults.headers.common['Authorization'] = this.token;
						this.added_groups = result.data
					},
					error => {
						console.error(error);
					}
				);
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
						this.refreshGroups();
                    },
                    error => {
                        console.error(error);
                    }
                );
            },
			oneMoreSubject(event) {
				this.num_subjects = this.num_subjects + 1;
				for (let i = this.group.subjects.length; i < this.num_subjects; ++i) {
					let subject = {
						name: "",
						type: "",
						weekly_periods: 0,
						teacher: ""
					}
					this.group.subjects.push(subject);
				}
			},
			deleteGroup(group_name) {
				group_name = decodeURIComponent(group_name);
				let request = {
                    "method": "DELETE",
                    "url": process.env.VUE_APP_BASE_URL + "/api/groups?name=" + group_name,
                    "headers": {
                        "content-type": "application/json"
                    }
                };
                axios(request).then(
                    result => {
						this.refreshGroups();
                    },
                    error => {
                        console.error(error);
                    }
                );
            }
        }
    }
</script>

