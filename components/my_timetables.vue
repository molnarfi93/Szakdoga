<template>
<table style="width: 500px">
    <tr class="header">
        <td>
            <span>My timetables</span>
        </td>
    </tr>
    <tr class="panel"> 
        <td v-for="timetable in added_timetables" v-bind:value="timetable">
			<span>{{timetable.name}}</span>
			<span>{{timetable.type}}</span>
			<span v-if="timetable.add_manually == true"><img src="checkbox.png"/></span>
			<span v-else><img src="unchecked-checkbox.png"/></span>
			<button v-on:click="getTimetable"><img src="pencil.png"/>Edit</button>
			<button v-on:click="destroyTimetable"><img src="cross.png"/>Delete</button><br />
    	</td>
		<br />
		<br />
		<br />
		<button v-on:click="$router.push('menu')">Back to menu</button>	
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
                "url": process.env.VUE_APP_BASE_URL + "/api/timetables",
                "headers": {
                    "content-type": "application/json"
                }
            };
            axios(request).then(
                result => {
					this.added_timetables = result
                },
                error => {
                    console.error(error);
                }
            );
 	    },
        methods: {
			getTimetable(event) {
      	        let request = {
                    "method": "GET",
                    "url": process.env.VUE_APP_BASE_URL + "/api/timetables/" + timetable.name,
                    "data": timetable,
                    "headers": {
                        "content-type": "application/json"
                    }
                };
                axios(request).then(
                    result => {
						this.$router.push({name: 'edit_timetable', params: {timetable: timetable.name}});
                    },
                    error => {
                        console.error(error);
                    }
                );
            },
			destroyTimetable(event) {
				let request = {
                    "method": "DELETE",
                    "url": process.env.VUE_APP_BASE_URL + "/api/timetables/" + timetable.name,
                    "data": timetable,
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