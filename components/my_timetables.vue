<template>
<table style="width: 500px">
    <tr class="header">
        <td>
            <span>My timetables</span>
        </td>
    </tr>
    <tr> 
        <td class="panel">
			<span v-for="timetable in added_timetables" v-bind:value="timetable">
				<span>{{timetable.name}}</span>
				<span>{{timetable.type}}</span>
				<span v-if="timetable.add_manually == true"><img src="checkbox.png"/></span>
				<span v-else><img src="unchecked-checkbox.png"/></span>
				<button v-on:click="$router.push({name: 'edit_timetable', params: {timetable: timetable.name}})"><img src="pencil.png"/></button>
				<button v-on:click="deleteTimetable(timetable.name)"><img src="cross.png"/></button><br />
				<br />
			</span>	
		<br />
		<br />
		<br />
		<button v-on:click="$router.push({name: 'menu', params: {user: $route.params.user}})">Back to menu</button>
		</td>	
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