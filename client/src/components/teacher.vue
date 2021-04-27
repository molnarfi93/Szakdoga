<template>
<table>
    <tr>
        <div class="header">Add teachers</div>
    </tr>
    <tr>
        <div class="panel">
            Name: <input type="text" v-model="teacher.name"><br />
			<br />
			Subjects: <select :multiple="true" v-model="teacher.subjects" placeholder="Choose!">
				<option v-for="subject in available_subjects" v-bind:value="subject">
					{{subject.name}}
				</option>
			</select><br />
            <br />
			Balance: 1<input type="range" min="1" max="5" v-model="teacher.balance">5<br />
			<br />
			Extremisms: 1<input type="range" min="1" max="5" v-model="teacher.extremisms">5<br />
			<br />
			Begin time: <input type="number" min="0" max="23" v-model="teacher.begin_time"><br />
			<br />
			End time: <input type="number" min="0" max="23" v-model="teacher.end_time"><br />
			<br />
			<button v-on:click="addTeacher" class="ok">Add</button><br />
            <br />
			<br />
            <br />
			Added teachers:
			<ul>
				<li v-for="teacher in added_teachers">
					{{teacher.name}} ({{teacher.balance}}, {{teacher.extremisms}}, {{teacher.begin_time}}, {{teacher.end_time}},
					<ul>
						<li v-for="subject in teacher.subjects">
							{{subject}},
						</li>
					</ul>
				<button v-on:click="deleteTeacher(teacher.name)"><img src="cross.png"/></button></li>
			</ul><br />
			<br />
			<button v-on:click="$router.push({name: 'edit_timetable', params: {timetable: $route.params.timetable}})">Go back</button><br />
			<br />
			Warning! In the case of teachers with same names, distinction with roman numbers is suggested!
        </div>
    </tr>
</table>
</template>

<script>
    import axios from "axios";
    export default {
        name: "teacher",
        data() {
            return {
                teacher: {
                    name: "",
					subjects: [],
                    balance: 3,
					extremisms: 3,
					begin_time: 0,
					end_time: 0,
					timetable: ""
                },
				timetable: {
				},
				available_subjects: [	
				],
				added_teachers: [
				]
			}
        },
		created() {
			this.teacher.timetable = this.$route.params.timetable;
		    let request = {
                "method": "GET",
                "url": process.env.VUE_APP_BASE_URL + "/api/subjects?timetable_name=" + this.$route.params.timetable,
                "headers": {
					"content-type": "application/json"
                }
            };
            axios(request).then(
                result => {
					this.available_subjects = result.data
					let request = {
						"method": "GET",
						"url": process.env.VUE_APP_BASE_URL + "/api/teachers?timetable_name=" + this.$route.params.timetable,
						"headers": {
							"content-type": "application/json"
						}
					};
					axios(request).then(
						result => {
							this.added_teachers = result.data
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
                "url": process.env.VUE_APP_BASE_URL + "/api/timetables?name=" + this.teacher.timetable,
                "headers": {
					"content-type": "application/json"
                }
            };
            axios(request).then(
                result => {
					this.timetable = result.data
					this.teacher.begin_time = this.timetable.begin_time;
					this.teacher.end_time = this.timetable.end_time;
				},
				error => {
					console.error(error);
				}
			);
		},
        methods: {
            checkTeacherDatas() {
      	        if (this.teacher.name == "") {
                    return false;
                }
                return true;
            },
			refreshTeachers() {
      	        let request = {
                    "method": "GET",
                    "url": process.env.VUE_APP_BASE_URL + "/api/teachers?timetable_name=" + this.$route.params.timetable,
                    "headers": {
                        "content-type": "application/json"
                    }
                };
                axios(request).then(
                    result => {
						axios.defaults.headers.common['Authorization'] = this.token;
						this.added_teachers = result.data;
                    },
                    error => {
                        console.error(error);
                    }
                );
            },
	        addTeacher(event) {
      	        if (this.checkTeacherDatas() == false) {
                    console.log("All fields must be fulfilled, and end_time must be later than begin_time!");
                    return;
                }
      	        let request = {
                    "method": "POST",
                    "url": process.env.VUE_APP_BASE_URL + "/api/teachers",
                    "data": this.teacher,
                    "headers": {
                        "content-type": "application/json"
                    }
                };
                axios(request).then(
                    result => {
						this.refreshTeachers();
                    },
                    error => {
                        console.error(error);
                    }
                );
            },
			deleteTeacher(name) {
				let request = {
                    "method": "DELETE",
                    "url": process.env.VUE_APP_BASE_URL + "/api/teachers?name=" + name,
                    "headers": {
                        "content-type": "application/json"
                    }
                };
                axios(request).then(
                    result => {
						this.refreshTeachers();
                    },
                    error => {
                        console.error(error);
                    }
                );
            }
        }
    }
</script>


