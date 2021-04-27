<template>
<table>
    <tr>
        <div class="header">My timetables</div>
    </tr>
    <tr> 
        <div class="panel">
				<td style="width: 150px">Name</td>
				<td style="width: 150px">Type</td>
				<td style="width: 100px">Add teachers manually</td><br />
			<div class="table" style="height: 40px" v-for="timetable in added_timetables" v-bind:value="timetable">
				<td style="width: 150px">{{timetable.name}}</td>
				<td style="width: 150px">{{timetable.type}}</td style="width: 100px">
				<td style="width: 100px" v-if="timetable.add_manually == true"><img src="checkbox.png"/></td>
				<td style="width: 100px" v-else><img src="unchecked-checkbox.png"/></td>
				<td><button v-on:click="$router.push({name: 'edit_timetable', params: {timetable: timetable.name}})"><img src="pencil.png"/></button></td>
				<td><button v-on:click="deleteTimetable(timetable.name)"><img src="cross.png"/></button></td><br />
			</div>	
		<br />
		<br />
		<br />
		<br />
		<br />
		<button v-on:click="$router.push({name: 'menu', params: {user: $route.params.user}})">Back to menu</button>
		</div>	
    </tr>
</table>
</template>

<script>
    import axios from "axios";
    export default {
        name: "my_timetables",
        data() {
            return {
				added_timetables: [
				]
            }
		},
		created() {
			let request = {
                "method": "GET",
                "url": process.env.VUE_APP_BASE_URL + "/api/timetables?user=" + this.$route.params.user,
				"headers": {
                    "content-type": "application/json"
                }
            };
            axios(request).then(
                result => {
					this.added_timetables = result.data
                },
                error => {
                    console.error(error);
                }
            );
 	    },
        methods: {
			refreshTimetables() {
      	        let request = {
                    "method": "GET",
                    "url": process.env.VUE_APP_BASE_URL + "/api/timetables?user=" + this.$route.params.user,
                    "headers": {
                        "content-type": "application/json"
                    }
                };
                axios(request).then(
                    result => {
						axios.defaults.headers.common['Authorization'] = this.token;
						this.added_timetables = result.data;
                    },
                    error => {
                        console.error(error);
                    }
                );
            },
			deleteTimetable(timetable_name) {
				let request = {
                    "method": "DELETE",
                    "url": process.env.VUE_APP_BASE_URL + "/api/timetables?name=" + timetable_name,
                    "headers": {
                        "content-type": "application/json"
                    }
                };
                axios(request).then(
                    result => {
						this.refreshTimetables();
                    },
                    error => {
                        console.error(error);
                    }
                );
            }
        }
    }
</script>