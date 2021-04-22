<template>
<table>
    <tr>
        <div class="header">Add rooms</div>
    </tr>
    <tr>
        <div class="panel">
            Name: <input type="text" v-model="room.name"><br />
			<br />
			Capacity: <input type="text" v-model="room.capacity"><br />
			<br />
			Subjects (in the case of special room): <select :multiple="true" v-model="room.subjects" placeholder="Choose!">
				<option v-for="subject in available_subjects" v-bind:value="subject">
					{{subject.name}}
				</option>
			</select><br />
			<br />
            <button v-on:click="addRoom" class="ok">Add</button><br />
			<br />
            <br />
            <br />
			Added rooms:
			<ul>
				<li v-for="room in added_rooms"> 
					{{room.name}} ({{room.capacity}},
					<ul>
						<li v-for="subject in room.subjects">
							{{subject}},
						</li>
					</ul>
				<button v-on:click="deleteRoom(room.name)"><img src="cross.png"/></button></li>
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
        name: "room",
        data() {
            return {
                room: {
                    name: "",
					capacity: 0,
					subjects: [],
					timetable: ""
                },
				available_subjects: [
				],
				added_rooms: [
				]
			}
        },
		created() {
			this.room.timetable = this.$route.params.timetable;
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
						"url": process.env.VUE_APP_BASE_URL + "/api/rooms?timetable_name=" + this.$route.params.timetable,
						"headers": {
							"content-type": "application/json"
						}
					};
					axios(request).then(
						result => {
							this.added_rooms = result.data
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
        methods: {
            checkRoomDatas() {
      	        if (this.room.name == "") {
                    return false;
                }
                if (this.room.capacity == "") {
                    return false;
                }
                return true;
            },
			refreshRooms() {
      	        let request = {
                    "method": "GET",
                    "url": process.env.VUE_APP_BASE_URL + "/api/rooms?timetable_name=" + this.$route.params.timetable,
                    "headers": {
                        "content-type": "application/json"
                    }
                };
                axios(request).then(
                    result => {
						axios.defaults.headers.common['Authorization'] = this.token;
						this.added_rooms = result.data
                    },
                    error => {
                        console.error(error);
                    }
                );
            },
			addRoom(event) {
      	        if (this.checkRoomDatas() == false) {
                    console.log("Invalid data!");
                    return;
                }
      	        let request = {
                    "method": "POST",
                    "url": process.env.VUE_APP_BASE_URL + "/api/rooms",
                    "data": this.room,
                    "headers": {
                        "content-type": "application/json"
                    }
                };
                axios(request).then(
                    result => {
						this.refreshRooms();
                    },
                    error => {
                        console.error(error);
                    }
                );
            },
			deleteRoom(name) {
				let request = {
                    "method": "DELETE",
                    "url": process.env.VUE_APP_BASE_URL + "/api/rooms?name=" + name,
                    "headers": {
                        "content-type": "application/json"
                    }
                };
                axios(request).then(
                    result => {
						this.refreshRooms();
                    },
                    error => {
                        console.error(error);
                    }
                );
            }
        }
    }
</script>

