<template>
<table style="width: 500px">
    <tr>
        <td class="header">
            <span>Add rooms</span>
        </td>
    </tr>
    <tr>
        <td class="panel">
            Name: <input type="text" v-model="room.name"><br />
			<br />
			Capacity: <input type="text" v-model="room.capacity"><br />
			<br />
			Subjects (in the case of special room): <multiselect v-model="room.subjects" placeholder="Choose!">
				<option v-for="subject in available_subjects" v-bind:value="subject">
					{{subject}}
				</option>
			</multiselect><br />
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
        name: "room",
        data() {
            return {
                room: {
                    name: "",
					capacity: 0,
					timetable: "",
                    subjects: []
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
                "url": process.env.VUE_APP_BASE_URL + "/api/rooms",
                "headers": {
                    "content-type": "application/json"
                }
            };
            axios(request).then(
                result => {
					this.added_rooms = result.rooms
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
                    },
                    error => {
                        console.error(error);
                    }
                );
            }
        }
    }
</script>

