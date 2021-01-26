<template>
<table style="width: 500px">
    <tr>
        <td class="header">
            <span>Add teachers</span>
        </td>
    </tr>
    <tr>
        <td class="panel">
            Name: <input type="text" v-model="teacher.name"><br />
			<br />
			Subjects: <multiselect v-model="teacher.subjects" placeholder="Choose!">
				<option v-for="subject in available_subjects" v-bind:value="subject">
					{{subject}}
				</option>
			</multiselect><br />
            <br />
			Balance: <input type="range" v-model="teacher.balance"><br />
			<br />
			Extremisms: <input type="range" min="1" max="5" v-model="teacher.extremisms"><br />
			<br />
			Begin time (part-time teachers): <input type="number" min="0" max="23" v-model="teacher.begin_time"><br />
			<br />
			End time (part-time teachers): <input type="number" min="0" max="23" v-model="teacher.end_time"><br />
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
						<li v-for="subject in subjects">
							{{subject}},
						</li>
					</ul>
				</li>
			</ul><br />
			<br />
			<button v-on:click="$router.go(-1)">Go back</button><br />
			<br />
			Warning! In the case of teachers with same names, use of roman numbers is suggested!
        </td>
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
                    balance: 3,
					extremisms: 3,
					begin_time: timetable.begin_time,
					end_time: timetable.end_time,
					timetable: "",
					subjects: []
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
                "url": process.env.VUE_APP_BASE_URL + "/api/teachers",
                "headers": {
                "content-type": "application/json"
                }
            };
            axios(request).then(
                result => {
					this.added_teachers = result.teachers
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
            checkTeacherDatas() {
      	        if (this.teacher.name == "") {
                    return false;
                }
                if (this.teacher.subjects == []) {
                    return false;
                }
				if (this.timetable.end_time <= this.timetable.begin_time) {
					return false;
				}	
                return true;
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
                    },
                    error => {
                        console.error(error);
                    }
                );
            }
        }
    }
</script>


