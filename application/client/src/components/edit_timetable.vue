<template>
<table>
    <tr>
        <div class="header">Edit timetable</div>
    </tr>
    <tr>
        <div class="panel">
			<br />
            <div class="link"><router-link :to="{name: 'subject', params: {timetable: $route.params.timetable}}">+ Add subjects:</router-link></div><br />
            <div class="link"><router-link :to="{name: 'room', params: {timetable: $route.params.timetable}}">+ Add rooms:</router-link></div><br />
            <div class="link"><router-link :to="{name: 'teacher', params: {timetable: $route.params.timetable}}">+ Add teachers:</router-link></div><br />
            <div class="link"><router-link :to="{name: 'group', params: {timetable: $route.params.timetable}}">+ Add groups:</router-link></div><br />
			<br />
			<br />
			<br />
			<button v-on:click="generateTimetables" class="ok">Get it!</button><br />
			<br />
			<br />
			<button v-on:click="$router.push({name: 'my_timetables', params: {user: timetable.user}})">Go back</button>
        </div>
    </tr>
</table>
</template>

<script>
    import axios from "axios";
    export default {
        name: "edit_timetable",
        data() {
            return {
                timetable: {
                }
            }
        },
		created() {
    	    let request = {
                "method": "GET",
                "url": process.env.VUE_APP_BASE_URL + "/api/timetables?name=" + this.$route.params.timetable,
                "headers": {
                    "content-type": "application/json"
                }
            };
            axios(request).then(
                result => {
					this.timetable = result.data
				},
				error => {
					console.error(error);
				}
			);
		},
        methods: {
			generateTimetables(event) {
      	        let request = {
                    "method": "GET",
                    "url": process.env.VUE_APP_BASE_URL + "/api/generator/" + this.$route.params.timetable,
                    "headers": {
                        "content-type": "application/json"
                    }
                };
                axios(request).then(
                    result => {
						axios.defaults.headers.common['Authorization'] = this.token;
                    },
                    error => {
                        console.error(error);
                    }
                );
            }
        }
    }
</script>